# 국내 휴양림 분포
# pip install xlrd==2.0.1
import os
import pandas as pd
import matplotlib.pyplot as plt
# 한글 폰트 설정
plt.rcParams['font.family'] ='Malgun Gothic'

program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)
input_file = path + '/forest_map.xls'

# 엑셀 파일 입력
forest_data = pd.read_excel(input_file)



# 구글맵 라이브러리
# pip install googlemaps
import googlemaps

# GCP 구글 클라우드 플랫폼
# - API KEY 발급
gmaps_api_key = 'AIzaSyDa_9XcZixmykF2y95JyJCZravaIvqdPPU'

# 구글 맵 객체 생성 - API KEY 지정
gmaps = googlemaps.Client(key=gmaps_api_key)

# address = '대한민국 인천광역시 부평구 경원대로 1366'
address = input('주소 : ')
name = input('위치 이름 : ')

g_result = gmaps.geocode(address, language='ko')
print(g_result)


# 요청한 위치 정보에 대하여 위도/경도 추출
latitude = g_result[0]['geometry']['location']['lat']
longitude = g_result[0]['geometry']['location']['lng']

print('위도 : ', latitude)
print('경도 : ', longitude)

# pip install folium
import folium

# 지도 객체 생성
map = folium.Map(location=[latitude, longitude], zoom_start=9)


# forest_data를 반복하며 휴양림을 지도에 표시
for index, row in forest_data.iterrows():
    # 휴양림명과 위도, 경도 추출
    name = row['휴양림명']
    lat = row['위도']
    lon = row['경도']
    pick = [lat, lon]
    # 마커 추가
    folium.Marker(pick, popup=address).add_to(map)
    # 라벨 추가
    title = '<div style = "width: 200px; height: 50px; line-height: 50px; font-size: 20px; background-color: white; text-align: center; transform: translate(-50%, 20px); border-radius: 20px; border: 1px solid black;" \
    ><b>{}</b></div>'.format(name)
    icon = folium.DivIcon(html=title)
    label = folium.Marker(pick, icon=icon)
    label.add_to(map)

# 현재 프로그램 경로 
import os
program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)

# 구글 맵 html(웹) 파일 저장
map.save(path + "/map.html")

import webbrowser
webbrowser.open(path + "/map.html")
