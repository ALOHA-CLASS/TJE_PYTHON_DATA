"""
    supplier_data.csv 파일을 입력하여,
    Supplier Y 공급업체 또는 Supplier Z 공급업체라면 가격이 650 초과인
    데이터를 문제01.csv 파일로 출력하시오.

"""

import pandas as pd
import sys

path = 'E:/ALOHA/JOEUN/GIT/TJE_PYTHON_DATA/Day09~/CSV'
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

data_frame = pd.read_csv(input_file)

data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)

공급업체 = data_frame['Supplier Name'].str
가격 = data_frame['Cost']

# 행선택을 위한 조건
condition = 공급업체.contains('Y') | ( 공급업체.contains('Z') & (가격 > 650.0) )

# ✅ 시리즈 객체 각각의 데이터 끼리 |, & 연산하기때문에 ( ) 로 연산 우선순위에 주의할 것!


data_frame_value_meets_condition = data_frame.loc[condition, :]
data_frame_value_meets_condition.to_csv(output_file, index=False)