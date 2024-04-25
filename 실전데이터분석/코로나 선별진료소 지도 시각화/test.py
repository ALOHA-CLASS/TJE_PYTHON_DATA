import pandas as pd
import ggmap
from ggmap import register_google

# 데이터 로드
data_raw = pd.read_csv('data.csv')  # 데이터 파일 경로에 맞게 수정해주세요

# 지역별(state) 선별 진료소 빈도 분석
state_counts = data_raw['state'].value_counts()
print(state_counts)

# 지역별(state) 선별 진료소 빈도 - 막대 그래프
state_counts.plot(kind='bar')

# 제주 선별 진료소 추출
jeju_data = data_raw[data_raw['state'] == "제주"]
print(jeju_data.head())
print(len(jeju_data))

# 제주 선별 진료소 - 위도, 경도 가져오기
api_key = "YOUR_API_KEY"  # 본인의 Google API 키를 넣어주세요
register_google(api_key)

jeju_data = ggmap.geocode(jeju_data, 'addr', source='google')
print(jeju_data.head())

# 제주 선별 진료소 지도 시각화 - 산점도로 표시
jeju_map = ggmap.get_googlemap('제주', maptype='roadmap', zoom=11)

ggmap.ggmap(jeju_map) + ggmap.geom_point(data=jeju_data, mapping=ggmap.aes(x='lon', y='lat', color='factor(name)'), size=10)

# 제주 선별 진료소 지도 시각화 - 구글 마커로 표시
jeju_marker = jeju_data[['lon', 'lat']]

jeju_map = ggmap.get_googlemap('제주', maptype='roadmap', zoom=11, markers=jeju_marker)

ggmap.ggmap(jeju_map) + ggmap.geom_text(data=jeju_data, mapping=ggmap.aes(x='lon', y='lat', label='name'), size=8, color='blue')
