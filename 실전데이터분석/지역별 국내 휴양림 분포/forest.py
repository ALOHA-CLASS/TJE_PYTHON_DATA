# 국내 휴양림 분포
# pip install xlrd==2.0.1
import os
import pandas as pd
import matplotlib.pyplot as plt
# 한글 폰트 설정
plt.rcParams['font.family'] ='Malgun Gothic'

program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)
input_file = path + '/forest.xls'

# 엑셀 파일 입력
forest_data = pd.read_excel(input_file)


# 데이터 구조 및 헤더 행 확인
print( forest_data.info() )
print( forest_data.head() )

# 변수명 변경
forest_data.columns \
    = ["name", "city", "gubun", "area", "number", "code", "codename", "new_city"]


# 시도별 휴양림 빈도분석
# - value_counts() 함수
city_counts = forest_data['city'].value_counts()
print(city_counts)

# 막대 그래프로 데이터 시각화
city_counts.plot(kind='bar', title='city')
plt.show()

# 시도별 휴양림 수, 내림차순 정렬
# sort_values() : 정렬 함수 (*ascending=True: 오름차순, False: 내림차순)
print("시도별 휴양림 수, 내림차순 정렬")
city_counts_sorted = forest_data['city'].value_counts() \
                                        .sort_values(ascending=False)

print(city_counts_sorted)

# 소재지_시도명, 제공기관명 별로 분포 확인
print("소재지_시도명")
print(forest_data['new_city'].value_counts().sort_values(ascending=False))
print("제공기관명")
print(forest_data['codename'].value_counts().sort_values(ascending=False))



