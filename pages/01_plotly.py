import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 1. 글로벌 시가총액 Top 10 기업 및 Yahoo 티커
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
    ("TSMC", "TSM"),  # 미국 ADR
]

st.set_page_config(page_title="글로벌 시가총액 TOP10 주가 추이", layout="wide")
st.title("🌐 글로벌 시가총액 TOP10 : 최근 1년간 주가 변화")
st.write("데이터 소스: Yahoo Finance (현지 통화 기준 종가)")

# 2. 날짜 범위 셋팅
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 3. 데이터프레임 만들기 (종가 기준)
price_df = pd.DataFrame()
for name, ticker in top10:
    try:
        data = yf.download(ticker, start=start_date, end=end_date, progress=False)
        if not data.empty:
            price_df[name] = data['Close']
        else:
            st.warning(f"⚠️ {name}({ticker}) : 데이터 없음")
    except Exception as e:
        st.warning(f"❌ {name}({ticker}) 오류: {e}")

# 4. Plotly를 활용하여 시각화
if not price_df.empty:
    fig = go.Figure()
    for company in price_df.columns:
        fig.add_trace(go.Scatter(
            x=price_df.index, y=price_df[company],
            mode='lines', name=company
        ))
    fig.update_layout(
        title="글로벌 시가총액 TOP10 - 최근 1년 종가 추이",
        xaxis_title="날짜",
        yaxis_title="주가 (현지 통화)",
        height=600,
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)

    # 추가: 데이터프레임 표도 함께 보여줌
    with st.expander("원본 데이터 확인"):
        st.dataframe(price_df)
else:
    st.error("모든 종목의 데이터를 불러올 수 없습니다. 네트워크, VPN, 티커명 등 환경을 점검하세요.")
