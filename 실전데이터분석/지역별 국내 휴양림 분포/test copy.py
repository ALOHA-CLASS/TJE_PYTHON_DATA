import os
import pandas as pd

program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)
input_file = path + '/forest_map.xls'

# 엑셀 파일 입력
forest_data = pd.read_excel(input_file)




# 구글맵 라이브러리 - 대한민국 위도,경도
import googlemaps
gmaps_api_key = 'AIzaSyDa_9XcZixmykF2y95JyJCZravaIvqdPPU'




gmaps = googlemaps.Client(key=gmaps_api_key)
location = "대한민국"
g_result = gmaps.geocode(location, language='ko')
latitude = g_result[0]['geometry']['location']['lat']       # 위도
longitude = g_result[0]['geometry']['location']['lng']      # 경도

# folium 모듈로 지도 객체 생성, html 저장, 지도 실행
import folium
map = folium.Map(location=[latitude, longitude], zoom_start=9)

# 마커, 라벨 추가
for index, row in forest_data.iterrows():
    # 휴양림명, 위도, 경도
    name = row['휴양림명']
    lat = row['위도']
    lon = row['경도']
    pick = [lat, lon]
    # print("{} : {}, {}".format(name, lat, lon))
    # 마커 추가
    marker = folium.Marker(pick, popup=name)
    marker.add_to(map)
    # 라벨 추가
    title = '<div style = "width: 200px; height: 30px; line-height: 30px; \
                            font-size: 16px; background-color: white; \
                            text-align: center; transform: translate(-50%, 20px); \
                            border-radius: 20px; border: 1px solid black;" \
    ><b>{}</b></div>'.format(name)
    icon = folium.DivIcon(html=title)
    label = folium.Marker(pick, icon=icon)
    label.add_to(map)




map.save(path + "/forest_map.html")
import webbrowser
webbrowser.open(path + "/forest_map.html")

