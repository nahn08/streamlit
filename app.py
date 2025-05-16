# data_viz_app.py 라는 이름으로 파일을 저장하세요.
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px # Plotly Express 임포트

# 1. 제목
st.title("간단한 데이터 시각화 예제")

# --- 데이터 생성 ---
st.sidebar.header("데이터 설정")
num_points = st.sidebar.slider("데이터 포인트 수:", min_value=10, max_value=200, value=50, step=10)

# np.random.seed(0) # 재현성을 위해 시드 고정 (선택 사항)

# Pandas DataFrame 생성
data = pd.DataFrame({
    '날짜': pd.date_range(start='2023-01-01', periods=num_points, freq='D'),
    '온도 (°C)': np.random.normal(loc=15, scale=5, size=num_points).cumsum() / np.arange(1, num_points + 1) + np.random.randn(num_points) * 2, # 약간의 추세와 노이즈
    '판매량': np.abs(np.random.normal(loc=100, scale=20, size=num_points) + np.sin(np.arange(num_points)/10) * 30).astype(int)
})
data = data.set_index('날짜') # '날짜' 컬럼을 인덱스로 설정

# --- 데이터 표시 ---
st.subheader("생성된 데이터 샘플")
st.dataframe(data.head())

# --- Streamlit 내장 차트 ---
st.subheader("Streamlit 내장 라인 차트")
st.line_chart(data)

st.subheader("Streamlit 내장 바 차트 (판매량)")
# 바 차트는 많은 데이터 포인트에 적합하지 않을 수 있으므로, 일부만 선택하거나 집계하는 것이 좋습니다.
# 여기서는 '판매량' 컬럼만 간단히 표시합니다.
st.bar_chart(data['판매량'])

# --- Plotly Express를 사용한 인터랙티브 차트 ---
st.subheader("Plotly Express 인터랙티브 라인 차트")

# 사용자가 y축으로 사용할 컬럼 선택
plot_column = st.selectbox(
    "Plotly 차트에 표시할 컬럼을 선택하세요:",
    data.columns
)

if plot_column:
    fig_plotly = px.line(
        data,
        y=plot_column,
        title=f"{plot_column} 시계열 데이터 (Plotly)",
        labels={'value': plot_column, '날짜': '시간'} # 축 레이블 변경
    )
    fig_plotly.update_layout(
        xaxis_title="날짜",
        yaxis_title=plot_column,
        legend_title_text='범례'
    )
    st.plotly_chart(fig_plotly, use_container_width=True) # use_container_width=True 로 차트 폭을 컨테이너에 맞춤

st.markdown("---")
st.write("사이드바에서 데이터 포인트 수를 조절해보세요!")

# 추가: 데이터 설명을 위한 Expander
with st.expander("데이터 생성 방식 보기"):
    st.markdown("""
    - **날짜**: 2023년 1월 1일부터 시작하여 `데이터 포인트 수`만큼 일별로 생성됩니다.
    - **온도 (°C)**: 평균 15도, 표준편차 5도의 정규분포를 따르는 값에 누적 평균과 약간의 노이즈를 추가하여 생성됩니다.
    - **판매량**: 평균 100, 표준편차 20의 정규분포를 따르는 값에 사인파형 변동을 추가하여 생성되며, 음수는 절댓값 처리됩니다.
    """)
