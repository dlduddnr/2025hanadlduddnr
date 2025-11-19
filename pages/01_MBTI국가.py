import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -----------------------------
# 1. 가상 데이터 생성
# -----------------------------
np.random.seed(42)
countries = ["Auroria", "Borealia", "Cascadia", "Deltora", "Eldoria"]
mbti_types = ["INTJ","INTP","ENTJ","ENTP","INFJ","INFP","ENFJ","ENFP"]

data = []
for country in countries:
    total_population = np.random.randint(100, 501)
    mbti_distribution = np.random.dirichlet(np.ones(len(mbti_types)), size=1).flatten()
    mbti_counts = (mbti_distribution * total_population).astype(int)
    for mbti, count in zip(mbti_types, mbti_counts):
        data.append([country, mbti, count])

df = pd.DataFrame(data, columns=["Country", "MBTI", "Count"])

# 국가별 MBTI 비율
df["Proportion"] = df.groupby("Country")["Count"].apply(lambda x: x / x.sum())

# -----------------------------
# 2. Streamlit 인터페이스
# -----------------------------
st.title("🌏 가상 나라별 MBTI 비율 시각화")

selected_country = st.selectbox("국가 선택", countries)

# 선택 국가 데이터 필터링
country_data = df[df["Country"] == selected_country].sort_values(by="Proportion", ascending=False)

# -----------------------------
# 3. 색상 설정 (1등 빨간색, 나머지 그라데이션)
# -----------------------------
colors = ["red"] + px.colors.sequential.Blues[len(mbti_types)-1]

# -----------------------------
# 4. Plotly 막대그래프
# -----------------------------
fig = px.bar(
    country_data,
    x="MBTI",
    y="Proportion",
    text="Count",
    color="MBTI",
    color_discrete_sequence=colors
)

fig.update_layout(
    title=f"{selected_country}의 MBTI 비율",
    yaxis_title="비율",
    xaxis_title="MBTI 유형",
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)
