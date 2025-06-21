import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import date, timedelta

# 1. 글로벌 시가총액 Top10 (2025년 중순 기준)
top10 = [
    ("Microsoft", "MSFT"),
    ("Apple", "AAPL"),
    ("Nvidia", "NVDA"),
    ("Alphabet (Google)", "GOOGL"),
    ("Amazon", "AMZN"),
    ("Saudi Aramco", "2222.SR"),
    ("Berkshire Hathaway", "BRK-B"),
    ("Eli Lilly", "LLY"),
    ("Meta Platforms", "META"),
    ("TSMC", "TSM"), # 나스닥 상장 ADR (미국내 거래)
]

st.set_page_config(page_title="글로벌 시가총액 TOP 10 주가 추이", layout="wide")
st.title("🌎 글로벌 시가총액 TOP10 - 최근 1년 주가 변화")
st.caption("데이터 출처: Yahoo Finance / 현지 통화 기준")

# 2. 날짜 설정
end = date.today()
start = end - timedelta(days=365)

fig = go.Figure()
plotted = 0  # 데이터 성공 count

for name, ticker in top10:
    try:
        df = yf.download(ticker, start=start, end=end, progress=False)
        if not df.empty:
            fig.add_trace(go.Scatter(
                x=df.index, y=df['Close'],
                mode='lines', name=name))
            plotted += 1
        else:
            st.warning(f"⚠️ {name}({ticker}) 데이터 없음")
    except Exception as e:
        st.warning(f"❌ {name}({ticker}) 불러오기 오류: {e}")

fig.update_layout(
    title="글로벌 시가총액 TOP10 최근 1년간 주가 (종가 기준)",
    xaxis_title="날짜",
    yaxis_title="주가 (현지 통화)",
    legend_title="기업명",
    template="plotly_white",
    height=600,
)

if plotted:
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("모든 기업의 데이터를 불러오지 못했습니다. 네트워크나 해외티커 제한을 확인하세요.")

