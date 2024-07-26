import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
file_path = 'daily_temp.csv'  # 업로드한 파일 이름
data = pd.read_csv(file_path)

# 날짜를 datetime 형식으로 변환하고 연도 추출
data['날짜'] = pd.to_datetime(data['날짜'])
data['연도'] = data['날짜'].dt.year

# 연도별 평균, 최저, 최고 기온 계산
yearly_data = data.groupby('연도').agg({
    '평균기온(℃)': 'mean',
    '최저기온(℃)': 'min',
    '최고기온(℃)': 'max'
}).reset_index()

# Streamlit 앱
st.title("연도별 기온 변화 추이")

# 그래프 선택
chart_type = st.selectbox("그래프 유형을 선택하세요", ["꺾은선 그래프", "막대 그래프"])

fig, ax = plt.subplots(figsize=(12, 6))

if chart_type == "꺾은선 그래프":
    ax.plot(yearly_data['연도'], yearly_data['평균기온(℃)'], label='평균기온(℃)', marker='o')
    ax.plot(yearly_data['연도'], yearly_data['최저기온(℃)'], label='최저기온(℃)', marker='o')
    ax.plot(yearly_data['연도'], yearly_data['최고기온(℃)'], label='최고기온(℃)', marker='o')
    ax.set_title('연도별 기온 변화 추이 (꺾은선 그래프)')
else:
    bar_width = 0.25
    index = yearly_data['연도']
    bar1 = ax.bar(index - bar_width, yearly_data['평균기온(℃)'], bar_width, label='평균기온(℃)')
    bar2 = ax.bar(index, yearly_data['최저기온(℃)'], bar_width, label='최저기온(℃)')
    bar3 = ax.bar(index + bar_width, yearly_data['최고기온(℃)'], bar_width, label='최고기온(℃)')
    ax.set_title('연도별 기온 변화 추이 (막대 그래프)')

ax.set_xlabel('연도')
ax.set_ylabel('기온 (℃)')
ax.legend()
ax.grid(True)

st.pyplot(fig)
