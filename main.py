
import streamlit as st

st.set_page_config(
    page_title="👁️ 황반변성 환자를 위한 국가 추천",
    page_icon="🌍",
    layout="wide"
)

st.markdown("""
<style>
.main{
background:linear-gradient(135deg,#E3F2FD,#F3E5F5);
}

.title{
text-align:center;
font-size:50px;
font-weight:bold;
background:linear-gradient(90deg,#1976D2,#7B1FA2);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.card{
background:white;
padding:20px;
border-radius:20px;
box-shadow:0 4px 15px rgba(0,0,0,0.15);
margin-top:10px;
}

.country{
background:linear-gradient(135deg,#ffffff,#f8f9fa);
padding:15px;
border-radius:15px;
margin-bottom:10px;
box-shadow:0 2px 8px rgba(0,0,0,0.1);
}

.score{
font-size:28px;
font-weight:bold;
color:#1976D2;
}

.stButton>button{
width:100%;
background:linear-gradient(90deg,#1976D2,#7B1FA2);
color:white;
font-size:20px;
border-radius:12px;
border:none;
}
</style>
""", unsafe_allow_html=True)

countries = [
{
"name":"🇫🇮 핀란드",
"score":98,
"reason":"🏥 우수한 의료 시스템, 높은 삶의 질, 시각장애 지원 서비스"
},
{
"name":"🇩🇰 덴마크",
"score":97,
"reason":"🚇 이동 편의성, 복지 수준, 안과 치료 접근성"
},
{
"name":"🇳🇴 노르웨이",
"score":96,
"reason":"💙 강력한 사회보장제도와 의료 혜택"
},
{
"name":"🇨🇦 캐나다",
"score":95,
"reason":"👁️ 전문 안과 치료와 접근성 우수"
},
{
"name":"🇳🇿 뉴질랜드",
"score":94,
"reason":"🌿 깨끗한 환경과 안정적인 의료 체계"
},
{
"name":"🇨🇭 스위스",
"score":93,
"reason":"🏆 세계 최고 수준의 의료 인프라"
},
{
"name":"🇸🇪 스웨덴",
"score":92,
"reason":"♿ 장애 지원 정책과 높은 복지"
},
{
"name":"🇳🇱 네덜란드",
"score":91,
"reason":"🚴 접근성 높은 도시 환경"
}
]

st.markdown(
'<div class="title">👁️ 황반변성 환자를 위한 살기 좋은 나라 🌍</div>',
unsafe_allow_html=True
)

st.write("")
st.info(
"📚 참고용 정보입니다. 실제 이주·유학·취업 결정은 의료보험, 비자, 생활비, 언어 등을 함께 고려해야 합니다."
)

if st.button("🌟 추천 국가 보기"):

    st.balloons()

    st.subheader("🏆 추천 국가 순위")

    for country in countries:

        st.markdown(
        f"""
        <div class="country">
            <h3>{country['name']}</h3>
            <div class="score">⭐ {country['score']}점</div>
            <p>{country['reason']}</p>
        </div>
        """,
        unsafe_allow_html=True
        )

    st.markdown("""
    ### 👁️ 황반변성 환자가 고려할 요소

    ✅ 안과 전문병원 수

    ✅ 항VEGF 주사 치료 접근성

    ✅ 건강보험 적용 범위

    ✅ 대중교통 이용 편의성

    ✅ 시각장애 지원 정책

    ✅ 안전한 보행 환경

    ✅ 삶의 질
    """)

    st.success(
    "🌍 의료 수준과 복지가 좋은 북유럽 국가들이 일반적으로 높은 평가를 받습니다."
    )

