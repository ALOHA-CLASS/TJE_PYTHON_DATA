# 웹 크롤링
# : 웹 사이트로부터 데이터를 수집하는 과정

# 라이브러리 설치
# 터미널 > 
# pip install requests
# pip install beautifulsoup4
# pip install lxml

import requests
from bs4 import BeautifulSoup

# 특정 사이트의 html(웹 사이트 문서) 가져오기
url = "https://movie.naver.com/movie/bi/mi/basic.naver?code=74977"
html = requests.get(url)

# 상태코드
# 200 : 응답 성공
# 404 : 페이지 없음
# 500 : 서버 에러
print(html)

# html 분석
soup = BeautifulSoup(html.text, 'lxml')

# 영화 제목
span = soup.find('span', class_='area_text_title')
print(span)
'''
    <span class="area_text_title">
        <strong class="_text">아바타: 물의 길</strong>
    </span>
'''
strong = span.find('strong', class_='_text')
print(strong)
'''
    <strong class="_text">아바타: 물의 길</strong>
'''

movie_title = strong.get_text()
print(movie_title)              # 아바타: 물의 길