
import streamlit as st

st.set_page_config(
    page_title="🌍 MBTI 세계 탐험",
    page_icon="✈️",
    layout="wide"
)

st.markdown("""
<style>
.main{
background: linear-gradient(135deg,#E3F2FD,#FCE4EC);
}

.title{
text-align:center;
font-size:55px;
font-weight:bold;
background: linear-gradient(90deg,#2196F3,#9C27B0,#FF4081);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.card{
background:white;
padding:25px;
border-radius:20px;
box-shadow:0 4px 20px rgba(0,0,0,0.15);
margin-top:15px;
}

.country{
background:linear-gradient(135deg,#ffffff,#f5f5f5);
padding:15px;
border-radius:15px;
font-size:22px;
margin:10px;
text-align:center;
box-shadow:0 2px 10px rgba(0,0,0,0.1);
}

.stButton>button{
width:100%;
background:linear-gradient(90deg,#2196F3,#9C27B0);
color:white;
font-size:20px;
border-radius:15px;
border:none;
height:3em;
}
</style>
""", unsafe_allow_html=True)

country_data = {

"INTJ":{
"desc":"🧠 전략적 사고와 독립성을 중시하는 혁신가",
"countries":[
"🇸🇬 싱가포르",
"🇨🇭 스위스",
"🇩🇪 독일",
"🇫🇮 핀란드",
"🇯🇵 일본"
]
},

"INTP":{
"desc":"💡 탐구심과 지적 자유를 사랑하는 사색가",
"countries":[
"🇫🇮 핀란드",
"🇨🇦 캐나다",
"🇳🇱 네덜란드",
"🇸🇪 스웨덴",
"🇩🇰 덴마크"
]
},

"ENTJ":{
"desc":"👑 리더십과 성취를 추구하는 지도자",
"countries":[
"🇺🇸 미국",
"🇸🇬 싱가포르",
"🇨🇭 스위스",
"🇬🇧 영국",
"🇩🇪 독일"
]
},

"ENTP":{
"desc":"🚀 도전과 창의성을 즐기는 발명가",
"countries":[
"🇺🇸 미국",
"🇳🇱 네덜란드",
"🇨🇦 캐나다",
"🇦🇺 호주",
"🇸🇪 스웨덴"
]
},

"INFJ":{
"desc":"🌈 의미와 가치를 중요하게 생각하는 이상주의자",
"countries":[
"🇫🇮 핀란드",
"🇳🇴 노르웨이",
"🇨🇦 캐나다",
"🇳🇿 뉴질랜드",
"🇩🇰 덴마크"
]
},

"INFP":{
"desc":"🎨 감성과 창의성이 풍부한 몽상가",
"countries":[
"🇳🇿 뉴질랜드",
"🇨🇦 캐나다",
"🇮🇸 아이슬란드",
"🇳🇴 노르웨이",
"🇸🇪 스웨덴"
]
},

"ENFJ":{
"desc":"🤝 사람을 돕고 성장시키는 리더",
"countries":[
"🇨🇦 캐나다",
"🇩🇰 덴마크",
"🇫🇮 핀란드",
"🇳🇴 노르웨이",
"🇳🇿 뉴질랜드"
]
},

"ENFP":{
"desc":"🎉 자유롭고 창의적인 활동가",
"countries":[
"🇦🇺 호주",
"🇨🇦 캐나다",
"🇳🇿 뉴질랜드",
"🇳🇱 네덜란드",
"🇺🇸 미국"
]
},

"ISTJ":{
"desc":"📋 책임감 있고 체계적인 관리자",
"countries":[
"🇩🇪 독일",
"🇯🇵 일본",
"🇨🇭 스위스",
"🇸🇬 싱가포르",
"🇫🇮 핀란드"
]
},

"ISFJ":{
"desc":"💖 따뜻하고 헌신적인 보호자",
"countries":[
"🇩🇰 덴마크",
"🇳🇴 노르웨이",
"🇨🇦 캐나다",
"🇫🇮 핀란드",
"🇳🇿 뉴질랜드"
]
},

"ESTJ":{
"desc":"🏆 조직과 질서를 중시하는 관리자",
"countries":[
"🇸🇬 싱가포르",
"🇩🇪 독일",
"🇨🇭 스위스",
"🇯🇵 일본",
"🇬🇧 영국"
]
},

"ESFJ":{
"desc":"😊 협력과 공동체를 중요하게 생각하는 사람",
"countries":[
"🇨🇦 캐나다",
"🇩🇰 덴마크",
"🇳🇴 노르웨이",
"🇳🇿 뉴질랜드",
"🇦🇺 호주"
]
},

"ISTP":{
"desc":"🔧 실용적이고 문제 해결을 즐기는 탐험가",
"countries":[
"🇨🇦 캐나다",
"🇦🇺 호주",
"🇳🇿 뉴질랜드",
"🇸🇪 스웨덴",
"🇫🇮 핀란드"
]
},

"ISFP":{
"desc":"🎨 예술성과 감성을 가진 모험가",
"countries":[
"🇳🇿 뉴질랜드",
"🇮🇸 아이슬란드",
"🇨🇦 캐나다",
"🇳🇴 노르웨이",
"🇸🇪 스웨덴"
]
},

"ESTP":{
"desc":"⚡ 활동적이고 도전을 즐기는 사업가",
"countries":[
"🇺🇸 미국",
"🇦🇺 호주",
"🇸🇬 싱가포르",
"🇨🇦 캐나다",
"🇳🇱 네덜란드"
]
},

"ESFP":{
"desc":"🌞 즐거움과 경험을 사랑하는 엔터테이너",
"countries":[
"🇦🇺 호주",
"🇳🇿 뉴질랜드",
"🇨🇦 캐나다",
"🇪🇸 스페인",
"🇮🇹 이탈리아"
]
}
}

st.markdown(
'<div class="title">🌍 MBTI 세계 탐험 ✈️</div>',
unsafe_allow_html=True
)

st.markdown(
"### 🎓 MBTI를 바탕으로 나와 잘 맞을 것 같은 나라를 탐험해 보세요!"
)

st.info("📚 교육용 체험 콘텐츠입니다. 실제 이민·유학·취업 결정은 다양한 요소를 함께 고려해야 합니다.")

mbti = st.selectbox(
"🧠 MBTI를 선택하세요",
list(country_data.keys())
)

if st.button("🌟 추천 국가 보기 🌟"):

    st.balloons()

    data = country_data[mbti]

    st.markdown(
    f"""
    <div class="card">
    <h2>✨ {mbti}</h2>
    <h3>{data['desc']}</h3>
    </div>
    """,
    unsafe_allow_html=True
    )

    st.subheader("🌎 추천 국가 TOP 5")

    cols = st.columns(5)

    for i, country in enumerate(data["countries"]):
        with cols[i]:
            st.markdown(
            f'<div class="country">{country}</div>',
            unsafe_allow_html=True
            )

    st.success("🎉 새로운 나라를 탐험하며 미래 진로와 꿈을 상상해 보세요!")

    st.markdown("""
    ### 🚀 생각해보기

    ✅ 이 나라의 대표 산업은 무엇일까?

    ✅ 어떤 대학이 유명할까?

    ✅ 내가 좋아하는 직업과 연결될까?

    ✅ 어떤 언어를 사용할까?

    ✅ 어떤 문화가 있을까?
    """)
