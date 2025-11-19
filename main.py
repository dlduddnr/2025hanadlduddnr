import streamlit as st

st.set_page_config(page_title="🍦 베스킨라빈스 키오스크", page_icon="🍨", layout="wide")

st.title("🍦 베스킨라빈스 키오스크에 오신 걸 환영합니다! 🎉")

# -------------------------------
# 1️⃣ 매장/포장 선택
# -------------------------------
st.header("1️⃣ 드실 장소를 선택해 주세요!")
place = st.radio("선택하세요:", ["매장", "포장"])
if place == "매장":
    st.info("매장에서 드실거군요! 편안하게 즐기세요 😄")
else:
    st.info("포장 선택! 집에서 맛있게 즐기세요 🏠")

# -------------------------------
# 2️⃣ 용기 선택
# -------------------------------
st.header("2️⃣ 용기를 선택해 주세요!")
container_options = {
    "싱글 컵": (1, 3500, "🥤"),
    "싱글 콘": (1, 3500, "🍦"),
    "더블 컵": (2, 5900, "🥤🥤"),
    "파인트": (3, 8200, "🍨🍨🍨"),
    "쿼터": (4, 15500, "🍨🍨🍨🍨"),
    "패밀리": (5, 22000, "🍨🍨🍨🍨🍨")
}
container = st.selectbox("용기를 선택하세요:", list(container_options.keys()))
scoop_count, price, container_emoji = container_options[container]
st.write(f"선택하신 용기: {container_emoji} **{container}** (스쿱 {scoop_count}개 가능)")

# -------------------------------
# 3️⃣ 맛 선택
# -------------------------------
st.header("3️⃣ 아이스크림 맛을 골라주세요! 🍧")
flavors = [
    "아몬드 봉봉", "엄마는 외계인", "민트 초코", "바닐라", "초콜릿",
    "뉴욕치즈케이크", "레인보우 샤베트", "슈팅스타", "딸기", "사랑에 빠진 딸기"
]

chosen_flavors = []
for i in range(scoop_count):
    flavor = st.selectbox(f"{i+1}번 맛 선택:", flavors, key=f"flavor_{i}")
    chosen_flavors.append(flavor)

# -------------------------------
# 4️⃣ 토핑 선택
# -------------------------------
st.header("4️⃣ 토핑 추가 🍫🍪🍓 (개당 500원)")
toppings_list = ["초코칩", "시럽", "견과류", "과일"]
chosen_toppings = st.multiselect("원하는 토핑을 선택하세요:", toppings_list)
topping_price = 500 * len(chosen_toppings)

# -------------------------------
# 5️⃣ 결제 선택 (현금/카드/모바일/기프티콘)
# -------------------------------
st.header("5️⃣ 결제 방법 선택 💳💵📱🎁")
payment = st.radio("결제 수단:", ["현금", "카드", "모바일 결제", "기프티콘"])
if payment == "현금":
    st.info("현금 결제 선택! 계산대에서 결제해주세요 💵")
elif payment == "카드":
    st.info("카드 결제 선택! 카드 단말기로 결제하세요 💳")
elif payment == "모바일 결제":
    st.info("모바일 결제 선택! QR코드로 결제 가능 📱")
else:
    st.info("기프티콘 결제 선택! 휴대폰으로 전송된 기프티콘을 사용하세요 🎁")

# -------------------------------
# 6️⃣ 주문 완료 버튼 & 가격 계산
# -------------------------------
st.header("6️⃣ 주문 확인 및 완료 🍨")
if st.button("주문 완료! 🎉"):
    total_price = price + topping_price
    st.success("주문이 완료되었습니다! 😄🍦")
    st.write(f"🛍 포장/매장: **{place}**")
    st.write(f"🥄 용기: {container} ({scoop_count} 스쿱) {container_emoji}")
    st.write(f"🍧 선택한 맛: {', '.join(chosen_flavors)}")
    st.write(f"🍫 토핑: {', '.join(chosen_toppings) if chosen_toppings else '없음'}")
    st.write(f"💰 총 가격: **{total_price}원**")
    st.write(f"💳 결제 방식: **{payment}**")
    
    # 🚗 5000원 이상 구매 시 주차권 안내
    if total_price >= 5000:
        st.balloons()
        st.info("🎉 5000원 이상 구매하셨으므로, **자동차 주차권**이 발급됩니다! 🚗🅿️")
