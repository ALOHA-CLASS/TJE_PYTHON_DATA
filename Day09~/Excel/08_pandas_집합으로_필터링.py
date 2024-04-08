#!/usr/bin/env python3
import pandas as pd

import os
# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)
# 입력파일, 출력파일
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

# 엑셀 파일을 읽을 때 'Purchase Date' 열을 datetime 형식으로 변환
data_frame = pd.read_excel(input_file, 'january_2013', index_col=None, parse_dates=['Purchase Date'])

important_dates = ['01/24/2013','01/31/2013']
# 'Purchase Date' 열을 datetime64[ns]로 명시적으로 캐스팅
important_dates = pd.to_datetime(important_dates, format='%m/%d/%Y')
# isin 함수 호출 전에 'Purchase Date' 열을 datetime 형식으로 캐스팅
data_frame_value_in_set = data_frame[data_frame['Purchase Date'].isin(important_dates)]

writer = pd.ExcelWriter(output_file)
data_frame_value_in_set.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.close()
