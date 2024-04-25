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
map = folium.Map(location=[latitude, longitude], zoom_start=20)

popup = folium.Popup(address, max_width=300, max_height=120,)
# 마커 추가
folium.Marker([latitude, longitude], popup=popup).add_to(map)

# 라벨 추가
title = '<div style = "width: 200px; height: 50px; line-height: 50px; font-size: 20px; background-color: white; text-align: center; transform: translate(-50%, 20px); border-radius: 20px; border: 1px solid black;" \
><b>{}</b></div>'.format(name)

icon = folium.DivIcon(html=title)
label = folium.Marker([latitude, longitude], icon=icon)
label.add_to(map)

# 현재 프로그램 경로 
import os
program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)

# 구글 맵 html(웹) 파일 저장
map.save(path + "/map.html")

import webbrowser
webbrowser.open(path + "/map.html")
