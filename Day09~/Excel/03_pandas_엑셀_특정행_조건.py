#!/usr/bin/env python3
import pandas as pd
import sys

path = 'E:/ALOHA/JOEUN/GIT/TJE_PYTHON_DATA/Day09~/Excel'
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

# 엑셀 파일 ➡ 데이터프레임
data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

# 헤더 없을 때 : header=None
# data_frame = pd.read_excel(input_file, 'january_2013', index_col=None, header=None)

print(data_frame)

# 조건 : Sale Amount 판매액이 1400 초과인 데이터
# astype(float) : float 타입으로 변환
condition = data_frame['Sale Amount'].astype(float) > 1400.0

# 헤더 없을 때 : index 로 컬럼 선택 
# condition = data_frame.loc[:, 3].astype(float) > 1400.0

data_frame_condition = data_frame[condition]

writer = pd.ExcelWriter(output_file)
data_frame_condition.to_excel(writer, sheet_name='jan_13_output', index=False)

# ✅ save() ❌  ➡ close() ⭕
writer.close()