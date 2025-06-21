import streamlit as st

st.set_page_config(
    page_title="🌈 MBTI 별 직업 추천! 🚀",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="auto"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gamja+Flower&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Gamja Flower', cursive;
    }
    .stApp {
        background: linear-gradient(to bottom, #fff0f5 0%, #ccecfb 100%);
        color: #222;
    }
    .mbti-box {
        background: #fff8fc;
        border-radius: 25px;
        border: 2px solid #ffb6c1;
        padding: 2rem 1rem;
        margin-bottom: 2rem;
        box-shadow: 0 6px 20px 0 rgba(245, 184, 255, 0.10), 0 1.5px 3px #f5b8ff;
        text-align: center;
    }
    .result-box {
        background: #ffffffcc;
        border-radius: 36px;
        border: 3px dashed #6EDCD9;
        margin-top: 20px;
        margin-bottom: 20px;
        padding: 2em 1em;
        text-align: center;
        animation: appear 1s ease;
    }
    @keyframes appear {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    h1, h2, h3 {
        color: #5b87fa;
        font-weight: bold;
        letter-spacing: 1.5px;
        text-shadow: 0 2px 8px #ffe4ff50;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🌟 내 MBTI 별<br>찰떡 직업 추천! 💡</h1>", unsafe_allow_html=True)
st.write("___")
st.markdown("<h3 style='text-align:center;'>✨ 나의 성향에 딱! 맞는 진로를 찾아보자 ✨</h3>", unsafe_allow_html=True)
st.write("🎈 아래의 드롭다운에서 자신의 MBTI를 선택하면, 성향에 맞는 직업과 멋진 한마디가 나옵니다! 👇")

mbti_list = [
    "ENFP", "INFP", "ENFJ", "INFJ",
    "ENTP", "INTP", "ENTJ", "INTJ",
    "ESFJ", "ISFJ", "ESTJ", "ISTJ",
    "ESFP", "ISFP", "ESTP", "ISTP"
]

mbti_emojis = ['✨','🌈','⭐','🎶','🌼','🐬','🚀','🥰','💡','🎨','🌻','🦄','🧩','🦋','🦸‍♂️','🐾']

mbti_jobs = {
    "ENFP": ("🎨 크리에이티브 디렉터, 📰 기자, 💬 마케팅 전문가",
             "✨ 매력뿜뿜! 사람과 소통하며 세상에 긍정의 에너지를 전파해요! 🌈"),
    "INFP": ("📚 작가, 🎨 일러스트레이터, 🌱 상담가",
             "🌷 상상력과 따스함으로 세상에 희망을 심는 당신!"),
    "ENFJ": ("👩‍🏫 교사, 🗣️ 커뮤니케이터, 🏢 인사담당자",
             "🤝 모두를 이끄는 리더십! 당신과 함께면 모두가 행복해요♥"),
    "INFJ": ("🧠 심리상담가, 📖 연구자, 🎭 작가",
             "🔮 깊은 통찰력! 남들이 쉽게 보지 못하는 걸 보는 멋진 사람"),
    "ENTP": ("💡 창업가, 📣 기획자, 🎮 게임 기획",
             "🌪️ 끝없는 아이디어! 새로운 트렌드는 당신 손에서 시작~"),
    "INTP": ("💻 프로그래머, 🧬 과학자, 🔬 데이터 분석가",
             "✨ 지적 호기심으로 세상을 분석하는 당신, 천재 그 자체!"),
    "ENTJ": ("📊 경영컨설턴트, 💼 CEO, ⚖️ 변호사",
             "👑 나는 계획대로 된다! 목표를 향해 시원하게 전진~"),
    "INTJ": ("🧑‍🔬 연구개발자, 💻 AI 개발자, 🧠 전략가",
             "🎯 천리안 전략가! 미래를 설계하는 마스터플래너"),
    "ESFJ": ("🤗 사회복지사, 🏥 간호사, 🍳 요리사",
             "🍀 모두의 행복메이커! 당신과 있으면 마음이 든든해요~"),
    "ISFJ": ("👨‍👩‍👧‍👦 보육교사, 🏦 은행원, 🏥 의료행정",
             "💖 섬세한 배려왕! 주변 모두를 편하게 만들어주는 데이님"),
    "ESTJ": ("📈 관리자, 🏢 공무원, 🔧 엔지니어",
             "🦸‍♂️ 책임감 만렙! 체계와 질서를 잡는 해결사!"),
    "ISTJ": ("📊 회계사, 📚 사서, 👨‍✈️ 군인",
             "🧩 차분하고 믿음직! 신뢰를 주는 든든한 존재"),
    "ESFP": ("🎤 연예인, 🎧 공연기획자, 🏖️ 여행가이드",
             "🎉 지금 이 순간이 가장 좋아! 긍정 에너지가 모두를 웃게 해요~"),
    "ISFP": ("🎨 디자이너, 📸 사진작가, 🌳 플로리스트",
             "🍃 감성아티스트! 자연과 예술을 사랑하는 순수한 마음"),
    "ESTP": ("💼 영업사원, ⚽ 운동선수, 🚑 응급구조사",
             "🚀 도전의 아이콘! 에너지 넘치고 눈치 백단!"),
    "ISTP": ("🛠️ 엔지니어, 🚗 자동차정비사, 🏍️ 모험가",
             "🔥 문제해결 능력자! 실전 경험과 멋짐의 끝판왕~"),
}

# expander 없이 바로 드롭박스만!
selected_mbti = st.selectbox(
    "🌟 내 MBTI를 선택하세요",
    mbti_list,
    format_func=lambda x: f"{x} {mbti_emojis[mbti_list.index(x)]}"
)
if selected_mbti:
    idx = mbti_list.index(selected_mbti)
    emoji = mbti_emojis[idx]
    job, message = mbti_jobs[selected_mbti]
    st.markdown(f"""
    <div class="result-box">
        <h2>{selected_mbti} {emoji}</h2>
        <span style="font-size:30px;">{job}</span>
        <br><br>
        <span style="font-size:22px;">{message}</span>
    </div>
    """, unsafe_allow_html=True)
