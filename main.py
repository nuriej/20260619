```python
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="✨ MBTI 진로 탐험관 ✨",
    page_icon="🚀",
    layout="wide"
)

# CSS 꾸미기
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg,#FFE5EC,#E0F7FA);
}

.title {
    text-align:center;
    font-size:55px;
    font-weight:bold;
    background: linear-gradient(90deg,#ff4d6d,#7209b7,#4361ee);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtitle{
    text-align:center;
    font-size:22px;
    color:#555;
}

.result-box{
    background:linear-gradient(135deg,#ffffff,#f3f8ff);
    padding:25px;
    border-radius:20px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.15);
    margin-top:15px;
}

.job-card{
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.1);
    text-align:center;
    font-size:20px;
    margin:10px;
}

.stButton>button{
    width:100%;
    background:linear-gradient(90deg,#ff4d6d,#7209b7);
    color:white;
    border:none;
    border-radius:15px;
    height:3em;
    font-size:20px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# 데이터
mbti_jobs = {
    "INTJ": {
        "desc":"🧠 전략적 사고와 계획 수립 능력이 뛰어난 혁신가",
        "jobs":["👨‍💻 AI 개발자","📊 데이터 과학자","🏗️ 건축가","🔬 연구원","📈 경영 컨설턴트"]
    },
    "INTP": {
        "desc":"💡 논리적이고 창의적인 아이디어 뱅크",
        "jobs":["💻 프로그래머","🔬 과학자","🤖 로봇공학자","📚 교수","🧩 게임 기획자"]
    },
    "ENTJ": {
        "desc":"👑 강력한 리더십과 추진력을 가진 지휘관",
        "jobs":["🏢 CEO","📈 경영 컨설턴트","⚖️ 변호사","💰 투자 분석가","🚀 창업가"]
    },
    "ENTP": {
        "desc":"🔥 창의적이고 도전을 즐기는 발명가",
        "jobs":["🚀 스타트업 대표","📢 마케터","🎮 기획자","💡 발명가","📺 방송인"]
    },
    "INFJ": {
        "desc":"🌈 사람들에게 긍정적인 영향을 주는 이상주의자",
        "jobs":["🧑‍🏫 교사","🩺 상담사","📖 작가","🌍 사회복지사","🎨 디자이너"]
    },
    "INFP": {
        "desc":"💖 공감 능력이 뛰어난 창의적 몽상가",
        "jobs":["✍️ 작가","🎨 일러스트레이터","🎬 영화감독","🎵 작곡가","🩺 심리상담사"]
    },
    "ENFJ": {
        "desc":"🌟 사람들을 이끄는 따뜻한 리더",
        "jobs":["👨‍🏫 교사","🎤 강연가","🤝 인사담당자","🩺 상담사","🌍 NGO 활동가"]
    },
    "ENFP": {
        "desc":"🎉 에너지 넘치고 창의적인 아이디어 메이커",
        "jobs":["📢 광고기획자","🎭 배우","📺 유튜버","✈️ 여행기획자","🎨 콘텐츠 크리에이터"]
    },
    "ISTJ": {
        "desc":"📋 책임감 있고 꼼꼼한 관리자",
        "jobs":["👮 경찰관","⚖️ 공무원","📊 회계사","🏦 은행원","📑 행정가"]
    },
    "ISFJ": {
        "desc":"💝 배려심 많고 성실한 보호자",
        "jobs":["🩺 간호사","👩‍🏫 교사","🏥 의료기사","🤝 사회복지사","📚 사서"]
    },
    "ESTJ": {
        "desc":"🏆 체계적이고 실행력이 뛰어난 관리자",
        "jobs":["🏢 관리자","👨‍✈️ 군 장교","📈 경영인","⚖️ 판사","🏦 금융인"]
    },
    "ESFJ": {
        "desc":"😊 친절하고 협력적인 조정자",
        "jobs":["👩‍🏫 교사","🤝 HR 담당자","🩺 간호사","🏨 호텔리어","🎉 이벤트 플래너"]
    },
    "ISTP": {
        "desc":"🔧 문제 해결 능력이 뛰어난 장인",
        "jobs":["✈️ 항공정비사","🚗 자동차 엔지니어","👨‍💻 개발자","🛠️ 기술자","🚒 소방관"]
    },
    "ISFP": {
        "desc":"🎨 감각적이고 예술적인 탐험가",
        "jobs":["🎨 디자이너","📸 사진작가","🎵 음악가","🧑‍🍳 셰프","🎭 배우"]
    },
    "ESTP": {
        "desc":"⚡ 행동력이 뛰어난 모험가",
        "jobs":["💼 영업전문가","🎤 방송인","🚓 경찰","🏅 스포츠 선수","🚀 창업가"]
    },
    "ESFP": {
        "desc":"🌞 밝고 사교적인 엔터테이너",
        "jobs":["🎭 배우","🎤 가수","📺 방송인","✈️ 승무원","🎉 행사기획자"]
    }
}

# 제목
st.markdown('<div class="title">🚀 MBTI 진로 탐험관 🚀</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">✨ 나의 MBTI로 어울리는 미래 직업을 찾아보세요! ✨</div>',
    unsafe_allow_html=True
)

st.write("")
st.write("")

mbti = st.selectbox(
    "🧠 당신의 MBTI를 선택하세요!",
    list(mbti_jobs.keys())
)

if st.button("🌟 직업 추천 받기 🌟"):

    data = mbti_jobs[mbti]

    st.balloons()

    st.markdown(
        f"""
        <div class="result-box">
            <h2>🎯 {mbti} 유형 분석</h2>
            <h3>{data['desc']}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.subheader("💼 추천 직업 TOP 5")

    col1, col2, col3 = st.columns(3)

    jobs = data["jobs"]

    for i, job in enumerate(jobs):
        if i % 3 == 0:
            with col1:
                st.markdown(
                    f'<div class="job-card">{job}</div>',
                    unsafe_allow_html=True
                )
        elif i % 3 == 1:
            with col2:
                st.markdown(
                    f'<div class="job-card">{job}</div>',
                    unsafe_allow_html=True
                )
        else:
            with col3:
                st.markdown(
                    f'<div class="job-card">{job}</div>',
                    unsafe_allow_html=True
                )

    st.write("")
    st.success("🎉 진로 탐색은 참고 자료입니다. 자신의 흥미와 적성을 함께 고려해 보세요!")

    st.info("🌈 꿈은 MBTI보다 더 넓습니다! 다양한 경험을 통해 자신만의 길을 찾아보세요!")
```
