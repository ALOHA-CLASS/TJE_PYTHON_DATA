#!/usr/bin/env python3
import pandas as pd
import sys

import os
# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)
# 입력파일, 출력파일
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

my_sheets = [0,1]
threshold = 1900.0

data_frame = pd.read_excel(input_file, sheet_name=my_sheets, index_col=None)

row_list = []
for worksheet_name, data in data_frame.items():
	row_list.append(data[data['Sale Amount'].replace('$', '').replace(',', '').astype(float) > threshold])
filtered_rows = pd.concat(row_list, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='set_of_worksheets', index=False)
writer.close()
