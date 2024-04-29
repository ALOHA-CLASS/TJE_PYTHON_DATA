# 코로나 선별진료소 지도 시각화
# pip install pandas
# pip install googlemaps
# pip install folium
# pip install xlrd==2.0.1
import os               # 현재 프로그램 경로를 가져오기
import pandas as pd     # 엑셀 파일 입력 및 출력

# 프로그램 경로의 데이터 파일 경로 입력
program_path = os.path.abspath(__file__)    # 프로그램 경로
path = os.path.dirname(program_path)        # 폴더(디렉토리)  경로
input_file = path + '/covid.xls'            # 분석 엑셀 파일 경로

# 엑셀 파일 입력
covid_data = pd.read_excel(input_file)      # 엑셀 ➡ 데이터프레임

# 지도 시각화를 위한 구글맵 라이브러리
import googlemaps

# GCP 구글 클라우드 플랫폼 
# 1. 구글 로그인
# 2. API KEY 발급

# API KEY 선언
gmaps_api_key = 'AIzaSyDa_9XcZixmykF2y95JyJCZravaIvqdPPU'

# 구글 맵 객체 생성
gmaps = googlemaps.Client(key=gmaps_api_key)

# 요청한 주소의 위치정보를 받아오기
address = input('주소 : ')

# 지정한 주소 및 언어를 기반으로 위치정보 반환
# * 주요 정보 : 위도 및 경도 값
# JSON 데이터 형식으로 반환 -- [ { } ] 
g_result = gmaps.geocode(address, language='ko')

# 위치 정보로 부터 위도/경도 추출
latitude = g_result[0]['geometry']['location']['lat']   # 위도
longitude = g_result[0]['geometry']['location']['lng']  # 경도

print('위도 : ', latitude)
print('경도 : ', longitude)

# 지도 라이브러리
# pip install folium
import folium

# 지도 객체 생성
# zoom_start= ( 20 : 상세 지역, 8 : 대한민국 전체)
map = folium.Map(location=[latitude, longitude], zoom_start=8)


# covid.xls (코로나 선별진료소 데이터) 로부터 주소를 추출
# covid_data 데이터 프레임을 한 행씩 반복
for index, row in covid_data.iterrows():
    # 의료기관명, 주소 추출
    name = row['의료기관명']
    address = row['주소']
    lat = 0
    lng = 0
    h_result = gmaps.geocode(address, language='ko')
    if h_result:
        lat = h_result[0]['geometry']['location']['lat']
        lng = h_result[0]['geometry']['location']['lng']

    print('의료기관명 : ', name)
    print('주소 : ', address)
    print('위도 : ', lat)
    print('경도 : ', lng)
    print('------------------------------------------')

    if lat != 0 and lng != 0:
        pick = [lat, lng]   # 위도, 경도를 리스트로 생성
        # 마커 추가
        folium.Marker(pick, popup=address).add_to(map)

        # 라벨 추가
        style = "font-size: 14px; padding: 10px; text-align: center;"
        style += "width: 120px; height: 40px; line-height: 20px;"
        style += "background-color: white;"
        style += "transform: translate(-50%, 14px);"
        title = '<div style="{}"><b>{}</b><div>'.format(style, name)

        icon = folium.DivIcon(html=title)
        label = folium.Marker(pick, icon=icon)
        label.add_to(map)

# 마지막에 지도 시각화
# 지도 파일 저장 (웹 파일 html)
map.save(path + "/covid.html")

# 브라우저 라이브러리
import webbrowser
webbrowser.open(path + "/covid.html")




