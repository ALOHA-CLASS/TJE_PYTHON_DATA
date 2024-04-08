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

data_frame = pd.read_csv(input_file)

data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name']\
.str.contains('Z')) | (data_frame['Cost'] > 600.0), :]

data_frame_value_meets_condition.to_csv(output_file, index=False)



#	✅ 실행방법
#	python 파일명 "입력csv파일경로" "출력csv파일경로"
#	python .\05_pandas특정행필터링_조건.py "D:\ALOHA LABS\PYTHON\TJE_PYTHON_DATA\NEW\CSV\input\supplier_data.csv" "D:\ALOHA LABS\PYTHON\TJE_PYTHON_DATA\NEW\CSV\output\sample5.csv"