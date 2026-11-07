from pathlib import Path

import streamlit as st
import pandas as pd

st.set_page_config(page_title="오늘 뭐 볼까?", layout="centered")
st.title("오늘 뭐 볼까?")
st.caption("10강 실습 과제 · 평점은 실제 관객 평점이 아닌 과제용 예시 값입니다.")

# 앱과 같은 폴더에 있는 영화 목록을 읽습니다.
df = pd.read_csv(Path(__file__).with_name("movies.csv"))

# 힌트의 사이드바와 선택박스, 슬라이더를 활용합니다.
st.sidebar.title("영화 선택")
장르 = st.sidebar.selectbox("장르", ["전체"] + df["장르"].unique().tolist())
최소_평점 = st.sidebar.slider("최소 평점", 0.0, 10.0, 0.0, 0.5)
표시할_영화_수 = st.sidebar.slider("목록에 표시할 영화 수", 1, len(df), min(10, len(df)))

# 힌트의 라디오 버튼으로 차트 종류를 선택합니다.
차트_종류 = st.sidebar.radio("차트 종류", ["막대", "꺾은선", "면적"])

# 선택한 장르와 최소 평점을 모두 만족하는 영화만 남깁니다.
결과 = df[df["예시 평점"] >= 최소_평점]
if 장르 != "전체":
    결과 = 결과[결과["장르"] == 장르]
결과 = 결과.sort_values("예시 평점", ascending=False)

st.metric("조건에 맞는 영화 수", f"{len(결과)}편")

if 결과.empty:
    st.info("조건에 맞는 영화가 없습니다. 장르나 최소 평점을 바꿔 보세요.")
else:
    # 표시 개수는 영화 목록에만 적용합니다.
    표시할_영화 = 결과.head(표시할_영화_수)
    st.caption(f"조건에 맞는 {len(결과)}편 중 평점이 높은 {len(표시할_영화)}편을 보여줍니다.")
    st.header("영화 목록")
    st.dataframe(표시할_영화, hide_index=True, alt="선택 조건과 표시 개수에 맞는 영화 목록")

    st.header("평점 구간별 영화 수")
    st.caption(f"목록 표시 개수와 관계없이 선택 조건에 맞는 전체 {len(결과)}편을 집계합니다.")

    # 0점대는 0점 이상 1점 미만입니다. 마지막 구간은 10점도 포함합니다.
    평점_구간 = [f"{점수}점대" for 점수 in range(9)] + ["9~10점"]
    구간별_영화_수 = []
    for 하한 in range(10):
        if 하한 == 9:
            구간 = 결과[(결과["예시 평점"] >= 9) & (결과["예시 평점"] <= 10)]
        else:
            구간 = 결과[(결과["예시 평점"] >= 하한) & (결과["예시 평점"] < 하한 + 1)]
        구간별_영화_수.append(len(구간))

    차트_데이터 = pd.DataFrame({"평점 구간": 평점_구간, "영화 수": 구간별_영화_수}).set_index("평점 구간")
    if 차트_종류 == "막대":
        st.bar_chart(차트_데이터, alt="평점 구간별 영화 수 막대그래프")
    elif 차트_종류 == "꺾은선":
        st.line_chart(차트_데이터, alt="평점 구간별 영화 수 꺾은선그래프")
    else:
        st.area_chart(차트_데이터, alt="평점 구간별 영화 수 면적그래프")
