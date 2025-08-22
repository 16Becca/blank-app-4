import random
import streamlit as st

# 페이지 기본 설정 (가장 처음에 한 번만 실행)
st.set_page_config(
    page_title="교사용 응원 카드",
    page_icon="💌",
    layout="centered"
)

# --- 교사 응원 문구 리스트 ---
QUOTES = [
    "선생님의 열정이 아이들의 미래를 밝힙니다. 오늘도 응원합니다!",
    "아이들과 함께 웃는 선생님의 모습이 가장 아름답습니다.",
    "가르침은 두 번 배우는 것입니다. 오늘도 아이들과 함께 성장하는 하루 되세요.",
    "선생님의 따뜻한 말 한마디가 한 아이의 인생을 바꿀 수 있습니다.",
    "때로는 지치고 힘들어도, 선생님은 아이들에게 가장 큰 희망입니다.",
    "최고의 선생님은 정답을 알려주는 사람이 아니라, 질문을 던지는 사람입니다.",
    "선생님은 영원한 영향력을 안겨주는 사람입니다.",
    "아이들의 작은 변화를 발견하고 칭찬해주는 선생님, 정말 멋져요!",
    "교실 속 선생님의 노력이 세상을 바꾸는 가장 큰 힘입니다.",
    "오늘 하루도 수고 많으셨습니다. 잠시 차 한잔의 여유를 가지세요."
]

# --- 세션 상태(Session State) 초기화 ---
# 앱이 처음 실행될 때 딱 한 번만 실행되어 변수들을 준비합니다.
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = "버튼을 눌러 오늘의 응원을 받아보세요!"
if 'previous_quote' not in st.session_state:
    st.session_state.previous_quote = ""

# --- 앱 제목 및 화면 구성 ---
st.title("💌 교사용 응원 카드")
st.write("---")

# 현재 응원 문구를 화면에 크게 표시합니다.
st.markdown(f"### {st.session_state.current_quote}")

# --- 메인 기능: '오늘의 응원 받기' 버튼 ---
# type="primary"는 버튼을 더 눈에 띄게 만들어줍니다.
if st.button("🌟 오늘의 응원 받기", type="primary"):
    # ★ 수정된 부분 1: 버튼 안에서 모든 로직이 실행되도록 수정
    
    # 1. 현재 문구를 '이전 문구'로 저장합니다.
    st.session_state.previous_quote = st.session_state.current_quote
    
    # 2. QUOTES 리스트에서 새로운 문구를 무작위로 뽑습니다.
    new_quote = random.choice(QUOTES)
    
    # 3. ★ 핵심 수정: 뽑은 새 문구를 '현재 문구'로 업데이트합니다. 이 코드가 빠져있었습니다.
    st.session_state.current_quote = new_quote
    
    # 4. ★ 추가: st.rerun()을 실행하여 화면을 즉시 새로고침하고 새 명언을 보여줍니다.
    st.rerun()


st.write("---")

# --- 부가 기능: '최근 응원 다시보기' 버튼 ---
# 이전에 응원을 받은 적이 있을 때만 버튼이 보이도록 조건 설정
if st.session_state.previous_quote and st.session_state.previous_quote != "버튼을 눌러 오늘의 응원을 받아보세요!":
    if st.button("🤔 방금 전 응원 다시보기"):
        # 현재 문구와 이전 문구를 서로 교환합니다 (Swap)
        temp_quote = st.session_state.current_quote
        st.session_state.current_quote = st.session_state.previous_quote
        st.session_state.previous_quote = temp_quote
        
        # 화면을 즉시 새로고침하여 변경사항을 반영합니다.
        st.rerun()
