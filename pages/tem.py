import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------
# 페이지 설정
# -------------------
st.set_page_config(
    page_title="서울 기후 타임머신",
    page_icon="🌍",
    layout="wide"
)

# -------------------
# 데이터 로드
# -------------------
@st.cache_data
def load_data():

    df = pd.read_csv("ta_20260619190504.csv")

    df["날짜"] = (
        df["날짜"]
        .astype(str)
        .str.replace("\t", "")
    )

    df["날짜"] = pd.to_datetime(df["날짜"])

    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    return df

df = load_data()

# -------------------
# 타이틀
# -------------------
st.title("🌏 서울 기후 타임머신")
st.caption("1907 ~ 2026 서울 기온 데이터 분석")

# -------------------
# 사이드바
# -------------------
menu = st.sidebar.radio(
    "메뉴 선택",
    [
        "📈 기후 변화",
        "🎂 생일 분석",
        "🔥 극한 기온",
        "🕰️ 기후 타임머신"
    ]
)

# ==================================================
# 1. 기후 변화
# ==================================================
if menu == "📈 기후 변화":

    st.header("📈 서울 평균기온 변화")

    yearly = (
        df.groupby("연도")["평균기온(℃)"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        yearly,
        x="연도",
        y="평균기온(℃)",
        title="연도별 평균기온 변화"
    )

    st.plotly_chart(fig, use_container_width=True)

    first_temp = yearly.iloc[0]["평균기온(℃)"]
    last_temp = yearly.iloc[-1]["평균기온(℃)"]

    diff = last_temp - first_temp

    st.metric(
        "1907년 대비 상승",
        f"{diff:.2f} ℃"
    )

# ==================================================
# 2. 생일 분석
# ==================================================
elif menu == "🎂 생일 분석":

    st.header("🎂 내 생일 기후 분석")

    month = st.selectbox(
        "월",
        range(1,13)
    )

    day = st.selectbox(
        "일",
        range(1,32)
    )

    birthday = df[
        (df["월"] == month) &
        (df["일"] == day)
    ]

    if len(birthday):

        avg_temp = birthday["평균기온(℃)"].mean()

        hottest = birthday.loc[
            birthday["최고기온(℃)"].idxmax()
        ]

        coldest = birthday.loc[
            birthday["최저기온(℃)"].idxmin()
        ]

        col1,col2,col3 = st.columns(3)

        col1.metric(
            "평균기온",
            f"{avg_temp:.1f}℃"
        )

        col2.metric(
            "가장 더웠던 생일",
            f"{hottest['최고기온(℃)']:.1f}℃"
        )

        col3.metric(
            "가장 추웠던 생일",
            f"{coldest['최저기온(℃)']:.1f}℃"
        )

        st.write("### 🔥 가장 더웠던 해")
        st.write(
            hottest["날짜"].date(),
            f"({hottest['최고기온(℃)']}℃)"
        )

        st.write("### ❄ 가장 추웠던 해")
        st.write(
            coldest["날짜"].date(),
            f"({coldest['최저기온(℃)']}℃)"
        )

# ==================================================
# 3. 극한 기온
# ==================================================
elif menu == "🔥 극한 기온":

    st.header("🔥 서울 역사상 가장 극단적인 날")

    col1,col2 = st.columns(2)

    with col1:

        hottest = (
            df.sort_values(
                "최고기온(℃)",
                ascending=False
            )
            .head(10)
        )

        st.subheader("역대 최고기온 TOP10")

        st.dataframe(
            hottest[
                ["날짜","최고기온(℃)"]
            ],
            use_container_width=True
        )

    with col2:

        coldest = (
            df.sort_values(
                "최저기온(℃)"
            )
            .head(10)
        )

        st.subheader("역대 최저기온 TOP10")

        st.dataframe(
            coldest[
                ["날짜","최저기온(℃)"]
            ],
            use_container_width=True
        )

# ==================================================
# 4. 기후 타임머신
# ==================================================
elif menu == "🕰️ 기후 타임머신":

    st.header("🕰️ 특정 연도로 이동")

    year = st.slider(
        "연도 선택",
        int(df["연도"].min()),
        int(df["연도"].max()),
        2000
    )

    selected = df[
        df["연도"] == year
    ]

    monthly = (
        selected.groupby("월")["평균기온(℃)"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        monthly,
        x="월",
        y="평균기온(℃)",
        markers=True,
        title=f"{year}년 월별 평균기온"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    avg = selected["평균기온(℃)"].mean()

    st.metric(
        f"{year}년 평균기온",
        f"{avg:.2f}℃"
    )
