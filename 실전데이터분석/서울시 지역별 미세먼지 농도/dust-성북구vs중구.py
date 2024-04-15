# 서울시 지역별 미세먼지 농도
# 필요한 라이브러리 설치
# !pip install pandas openpyxl
import os
import pandas as pd

program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)
input_file = path + '/dust.xlsx'

# 엑셀 파일 읽기
dust_data = pd.read_excel(input_file)

# 성북구, 중구 데이터만 추출
dust_data_select = dust_data[["날짜", "성북구", "중구"]]
print(dust_data_select.head())          # 데이터프레임의 처음 5개의 행을 가져와 출력
print('--------------------------------')


# 결측치 확인
print('결측치 : ')
print(dust_data_select.isna().sum())
print('--------------------------------')

# 지역별 미세먼지 농도 기술통계량
print('성북구 미세번지 기술통계량 : ')
print(dust_data_select["성북구"].describe())
print('--------------------------------')
print('중구 미세번지 기술통계량 : ')
print(dust_data_select["중구"].describe())
print('--------------------------------')



# 지역별 미세먼지 농도 등분산성 검정 및 평균 차이 검정
from scipy.stats import bartlett, levene, f_oneway

# Bartlett's test 또는 Levene's test를 사용하여 분산의 등분산성을 검정
print('중구-성북구 등분산성을 검정')
bartlett_statistic, bartlett_p_value = bartlett(dust_data_select["중구"], dust_data_select["성북구"])
levene_statistic, levene_p_value = levene(dust_data_select["중구"], dust_data_select["성북구"])

print("Bartlett's test - Statistic:", bartlett_statistic, "p-value:", bartlett_p_value)
print("Levene's test - Statistic:", levene_statistic, "p-value:", levene_p_value)
print('--------------------------------')

# f_oneway() (One-Way ANOVA): "일원분산분석"
# - ANOVA(Analysis of Variance)의 일원분산분석(One-Way ANOVA)을 수행하는 함수
# - 세 개 이상의 그룹 간의 평균 차이를 비교하는데 사용됩니다.

# 등분산성이 만족되면 ANOVA를 수행하여 그룹 간의 평균 차이 검정
# ANOVA(Analysis of Variance) : 그룹 간의 평균의 차이를 비교하는 통계적인 방법
if bartlett_p_value > 0.05 and levene_p_value > 0.05:
    print('중구-성북구 평균 차이 검정')
    f_statistic, f_p_value = f_oneway(dust_data_select["중구"], dust_data_select["성북구"])
    print("F-statistic:", f_statistic, "p-value:", f_p_value)
else:
    print("등분산성을 만족하지 않아 ANOVA를 수행할 수 없습니다.")
print('----------------------------------------------------------------')

# ttest_ind() (Independent Samples t-test):
# - 독립표본 t-검정(Independent Samples t-test)을 수행하는 함수
# - 독립표본 t-검정은 두 그룹의 평균 차이가 통계적으로 유의한지를 검정합니다.
# - 두 개의 그룹 간의 평균 차이를 비교하는데 사용됩니다.
# * equal_var= [True: 등분산성 가정, False: 등분산성 가정❌(분산이 다름을 가정)]

# # 지역별 평균 차이 검정하기
from scipy.stats import ttest_ind

t_statistic, p_value = ttest_ind(dust_data_select["중구"], dust_data_select["성북구"], equal_var=True)
print("T-statistic:", t_statistic)
print("p-value:", p_value)
print('----------------------------------------------------------------')
print('*** 결론 도출 ***')
if p_value > 0.05:
    print('귀무가설 채택 - "서울 중구와 성북구 지역은 미세먼지 농도의 평균에 차이가 없다."')
else: 
    print('대립가설 채택 - "서울 중구와 성북구 지역은 미세먼지 농도의 평균에 차이가 있다."')


# 성북구와 중구 미세먼지 농도 상자 그림 그리기
import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

plt.figure(figsize=(8, 6))
dust_data_select.boxplot(column=["성북구", "중구"])
plt.title("finedust")
plt.xlabel("AREA")
plt.ylabel("FINEDUST_PM")

plt.savefig(path + '/서울시 미세먼지 - 성북구vs중구.png')
plt.show()