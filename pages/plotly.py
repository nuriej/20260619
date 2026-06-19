import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Global Top 10 Market Cap Stocks",
    layout="wide"
)

st.title("🌍 Global Market Cap Top 10 Stocks")
st.caption("최근 1년 주가 수익률 비교")

# 글로벌 시총 상위 기업
stocks = {
    "NVIDIA": "NVDA",
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Alphabet": "GOOGL",
    "Amazon": "AMZN",
    "Meta": "META",
    "Broadcom": "AVGO",
    "TSMC": "TSM",
    "Tesla": "TSLA",
    "Berkshire Hathaway": "BRK-B"
}

@st.cache_data(ttl=3600)
def load_data():
    df = yf.download(
        list(stocks.values()),
        period="1y",
        auto_adjust=True,
        progress=False
    )["Close"]

    return df

prices = load_data()

# 기준값 100으로 정규화
normalized = prices.div(prices.iloc[0]).mul(100)

fig = go.Figure()

for company, ticker in stocks.items():
    fig.add_trace(
        go.Scatter(
            x=normalized.index,
            y=normalized[ticker],
            mode="lines",
            name=company,
            hovertemplate=
            "<b>%{fullData.name}</b><br>" +
            "Date: %{x}<br>" +
            "Index: %{y:.2f}<extra></extra>"
        )
    )

fig.update_layout(
    height=700,
    template="plotly_white",
    title="Top 10 Global Stocks Performance (Base = 100)",
    xaxis_title="Date",
    yaxis_title="Performance Index",
    hovermode="x unified",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    )
)

st.plotly_chart(fig, use_container_width=True)

# 수익률 계산
returns = ((prices.iloc[-1] / prices.iloc[0]) - 1) * 100

ranking = pd.DataFrame({
    "Company": stocks.keys(),
    "Return (%)": returns.values
}).sort_values("Return (%)", ascending=False)

st.subheader("📈 1년 수익률 순위")
st.dataframe(
    ranking.style.format({
        "Return (%)": "{:.2f}%"
    }),
    use_container_width=True
)
