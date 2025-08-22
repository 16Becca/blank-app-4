import streamlit as st
# 기존 코드: st.title("My First App")
# 수정 코드:
st.title("🏫 우리반 알림장")
st.write("우리 반의 중요한 소식을 확인하세요!")
import streamlit as st
import random

# --- 페이지 설정 ---
st.set_page_config(
    page_title="교사용 응원 카드",
    page_icon="💌",
    layout="centered"
)

# --- 교사 응원 문구 리스트 ---
# 이 리스트에 원하시는 응원 문구를 자유롭게 추가하거나 수정하세요.
QUOTES = [
    "선생님의 열정이 아이들의 미래를 밝힙니다. 오늘도 응원합니다!",
    "아이들과 함께 웃는 선생님의 모습이 가장 아름답습니다.",
    "가르침은 두 번 배우는 것입니다. 오늘도 아이들과 함께 성장하는 하루 되세요.",
    "선생님의 따뜻한 말 한마디가 한 아이의 인생을 바꿀 수 있습니다.",
    "때로는 지치고 힘들어도, 선생님은 아이들에게 가장 큰 희망입니다.",
    "최고의 선생님은 정답을 알려주는 사람이 아니라, 질문을 던지는 사람입니다.",
    "선생님은 영원한 영향력을 안겨주는 사람입니다. [4]",
    "아이들의 작은 변화를 발견하고 칭찬해주는 선생님, 정말 멋져요!",
    "교실 속 선생님의 노력이 세상을 바꾸는 가장 큰 힘입니다.",
    "오늘 하루도 수고 많으셨습니다. 잠시 차 한잔의 여유를 가지세요."
]

# --- 세션 상태(Session State) 초기화 ---
# Streamlit 앱은 사용자가 상호작용할 때마다 코드가 다시 실행됩니다.
# st.session_state를 사용하면 변수 값을 유지할 수 있습니다.
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = "버튼을 눌러 오늘의 응원을 받아보세요!"
if 'previous_quote' not in st.session_state:
    st.session_state.previous_quote = ""

# --- 앱 제목 ---
st.title("💌 교사용 응원 카드")
st.write("---")

# --- 메인 기능 ---
# '오늘의 응원 받기' 버튼
if st.button("🌟 오늘의 응원 받기"):
    # 이전 문구를 previous_quote에 저장
    st.session_state.previous_quote = st.session_state.current_quote
    
    # QUOTES 리스트에서 무작위로 문구 하나를 선택
    new_quote = random.choice(QUOTES)
    
    # 현재 문구를 새 문구로 업데이트
    st.session_state.current_quote = new_quote

# 현재 응원 문구를 화면에 표시
st.markdown(f"### {st.session_state.current_quote}")

st.write("---")

# --- 부가 기능 ---
# '최근 응원 다시보기' 버튼. 단, 이전에 응원을 받은 적이 있어야 버튼이 보임
if st.session_state.previous_quote and st.session_state.previous_quote != "버튼을 눌러 오늘의 응원을 받아보세요!":
    if st.button("🤔 방금 전 응원 다시보기"):
        # 다시보기 버튼을 누르면 현재 문구를 이전 문구로 되돌림
        # (현재 문구와 이전 문구를 서로 교환)
        temp_quote = st.session_state.current_quote
        st.session_state.current_quote = st.session_state.previous_quote
        st.session_state.previous_quote = temp_quote
        
        # 화면을 즉시 새로고침하여 변경사항을 반영
        st.rerun()

st.markdown("---")

### **4. 실행 방법**

# 올바른 코드
st.markdown("1. `streamlit_app.py`와 `requirements.txt` 파일이 같은 폴더에 있는지 확인합니다.")
st.markdown("2. 해당 폴더 경로에서 터미널을 엽니다."
st.markdown("3.  아래 명령어를 입력하고 실행합니다."

```bash
streamlit run streamlit_app.py