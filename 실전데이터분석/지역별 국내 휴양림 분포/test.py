import pandas as pd
import matplotlib.pyplot as plt

# 엑셀 파일 가져오기
path = "C:/KHM/R/code/source/"
file = path + "forest.xls"
forest_data = pd.read_excel(file)

# 변수명 변경
forest_data.columns = ["name", "city", "gubun", "area", "number", "stay", "city_new", "code", "codename"]

# 데이터 구조 및 앞부분 확인
print(forest_data.info())
print(forest_data.head())

# 시도별 휴양림 빈도분석 - value_counts() 함수
city_counts = forest_data['city'].value_counts()
print(city_counts)
city_counts.plot(kind='bar', title='city')
plt.show()

# 시도별 휴양림 수 구하고 내림차순 정렬하기
city_counts_sorted = forest_data['city'].value_counts().sort_values(ascending=False)
print(city_counts_sorted)

# 시도별, 소재지_시도명, 제공기관명 별로 분포 확인하기
print(forest_data['city'].value_counts().sort_values(ascending=False))
print(forest_data['city_new'].value_counts().sort_values(ascending=False))
print(forest_data['codename'].value_counts().sort_values(ascending=False))
