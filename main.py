import streamlit as st

st.title("🍨 나만의 아이스크림 주문 웹앱")

# 1. 사이즈 선택
size = st.selectbox("아이스크림 사이즈를 선택하세요:", ["Small", "Medium", "Large"])

# 사이즈별 가격
size_price = {
    "Small": 2000,
    "Medium": 3000,
    "Large": 4000}

# 2. 아이스크림 맛 선택
menu = st.selectbox(
    "좋아하는 아이스크림 맛을 선택하세요:",
    ["아몬드 봉봉", "엄마는 외계인", "민트 초코", "바닐라", "초코", "딸기", "뉴욕치즈케이크"])

# 3. 이름 입력
name = st.text_input("이름을 입력해 주세요:")

# 4. 버튼 클릭 시 결과 출력
if st.button("주문하기"):
    total_price = size_price[size]
    st.write(f"### {name}님 주문 완료!")
    st.write(f"- 선택한 사이즈: **{size}**")
    st.write(f"- 선택한 맛: **{menu}**")
    st.write(f"### 총 가격: **{total_price}원**")

# 5. 민트초코 선택 시 장난 출력
if menu == "민트 초코":
    st.write("🤢 민트초코 좋아하는 사람이었군요...")
