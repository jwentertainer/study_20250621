import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import date, timedelta

# 1. 글로벌 시가총액 TOP 10 티커 (2025년 최신 반영)
top10_tickers = {
    "Microsoft": "MSFT",
    "Apple": "AAPL",
    "Nvidia": "NVDA",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Saudi Aramco": "2222.SR",
    "Berkshire Hathaway": "BRK-B",
    "Eli Lilly": "LLY",
    "Meta Platforms": "META",
    "TSMC": "2330.TW"  # 또는 "TSM" (나스닥 ADR), 데이터 없음시 교체
}

st.title("🌐 글로벌 시가총액 Top10 최근 1년 주가 변동")

end_date = date.today()
start_date = end_date - timedelta(days=365)

fig = go.Figure()
at_least_one = False  # 그래프 하나라도 출력됐는지 체크

for company, ticker in top10_tickers.items():
    try:
        df = yf.download(ticker, start=start_date, end=end_date, progress=False)
        if df is not None and not df.empty:
            fig.add_trace(go.Scatter(x=df.index, y=df['Close'],
                                     mode='lines',
                                     name=company))
            at_least_one = True
        else:
            st.warning(f"[{company}] 데이터가 비어 있습니다. (불러오기 실패)")
    except Exception as e:
        st.warning(f"[{company}] 데이터 불러오기 중 오류: {str(e)}")

fig.update_layout(
    title="글로벌 시가총액 Top 10 기업 1년간 주가 변화 (종가)",
    xaxis_title="날짜",
    yaxis_title="주가 (현지 통화)",
    legend_title="기업명",
    template="plotly_white",
    height=600
)

if at_least_one:
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("모든 티커의 데이터를 불러오는데 실패했습니다. 네트워크 연결, VPN, Streamlit 서버상 이슈, 또는 yfinance 라이브러리 버전을 확인하세요.")

