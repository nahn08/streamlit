# simple_app.py 라는 이름으로 파일을 저장하세요.
import streamlit as st

# 1. 제목과 설명
st.title("나의 첫 Streamlit 앱")
st.write("이것은 매우 간단한 Streamlit 예제입니다.")

# 2. 텍스트 입력
name = st.text_input("이름을 입력하세요:", "여기에 이름을 입력")

# 3. 입력받은 텍스트 표시
if name and name != "여기에 이름을 입력": # 초기값과 다를 때만 인사
    st.write(f"안녕하세요, {name}님!")
else:
    st.write("이름을 입력해주세요.")

# 4. 슬라이더로 숫자 선택
age = st.slider("나이를 선택하세요:", min_value=0, max_value=100, value=25, step=1)

# 5. 선택한 숫자 표시
st.write(f"선택하신 나이는 {age}세 입니다.")

# 6. 버튼과 메시지
if st.button("메시지 보기"):
    st.success("버튼을 클릭하셨습니다! 🎉")
    st.balloons() # 재밌는 풍선 효과!

# 추가: 선택 상자 (Selectbox) 예제
st.subheader("좋아하는 과일 선택")
fruit_options = ["사과", "바나나", "딸기", "오렌지"]
selected_fruit = st.selectbox("가장 좋아하는 과일을 선택하세요:", fruit_options)

if selected_fruit:
    st.write(f"선택하신 과일은 {selected_fruit}입니다.")

# 추가: 체크박스 (Checkbox) 예제
st.subheader("옵션 선택")
if st.checkbox("추가 정보 보기"):
    st.info("이것은 체크박스를 선택했을 때 나타나는 추가 정보입니다.")

# 사이드바에 위젯 추가하기
st.sidebar.header("사이드바 설정")
sidebar_option = st.sidebar.selectbox(
    "사이드바에서 옵션을 선택하세요:",
    ("옵션 A", "옵션 B", "옵션 C")
)
st.sidebar.write(f"사이드바에서 선택한 옵션: {sidebar_option}")
