import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import date, timedelta

# 1. 티커 리스트와 회사명 매핑
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
    "TSMC": "2330.TW"
}

# 2. Streamlit 기본 설정
st.set_page_config(page_title="글로벌 시가총액 TOP 10 🏦📈", layout="wide")
st.title("🪙 글로벌 시가총액 Top10 최근 1년 주가 변화 대시보드")

st.write("데이터: [Yahoo Finance](https://finance.yahoo.com/)")

# 3. 최근 1년 설정
end_date = date.today()
start_date = end_date - timedelta(days=365)

# 4. 데이터 수집 및 Plotly 시각화
fig = go.Figure()

for company, ticker in top10_tickers.items():
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data['Close'],
            mode='lines',
            name=company
        ))
    except Exception as e:
        st.warning(f"{company}({ticker}) 데이터 로드 실패: {e}")

fig.update_layout(
    title="글로벌 시가총액 TOP10 1년간 주가 변화 (종가 기준)",
    xaxis_title="날짜",
    yaxis_title="주가 (현지 통화)",
    legend_title="기업명",
    template="plotly_white",
    height=600
)

st.plotly_chart(fig, use_container_width=True)

# 5. 유저가 보기 원하는 기업만 선택하도록 해도 좋습니다.
with st.expander("직접 기업 선택하기 (기본: 전체 TOP10)"):
    selected = st.multiselect(
        label="기업(회사명) 선택",
        options=list(top10_tickers.keys()),
        default=list(top10_tickers.keys())
    )

    if selected:
        fig2 = go.Figure()
        for company in selected:
            ticker = top10_tickers[company]
            try:
                data = yf.download(ticker, start=start_date, end=end_date)
                fig2.add_trace(go.Scatter(
                    x=data.index,
                    y=data['Close'],
                    mode='lines',
                    name=company
                ))
            except Exception as e:
                st.warning(f"{company}({ticker}) 데이터 로드 실패: {e}")
        fig2.update_layout(
            title="선택한 기업의 최근 1년간 주가 변화 (종가 기준)",
            xaxis_title="날짜",
            yaxis_title="주가 (현지 통화)",
            legend_title="기업명",
            template="plotly_white",
            height=600
        )
        st.plotly_chart(fig2, use_container_width=True)
