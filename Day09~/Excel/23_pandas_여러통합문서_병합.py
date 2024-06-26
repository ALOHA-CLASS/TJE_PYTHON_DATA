#!/usr/bin/env python3
import pandas as pd
import glob
import os
import sys


# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)
# 입력폴더, 출력파일
input_path = path + '/input/'
output_file = path + '/output/' + input('출력 파일 : ')

all_workbooks = glob.glob(os.path.join(input_path,'*.xls*'))
data_frames = []
for workbook in all_workbooks:
	all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
	for worksheet_name, data in all_worksheets.items():
		data_frames.append(data)
all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='all_data_all_workbooks', index=False)
writer.close()