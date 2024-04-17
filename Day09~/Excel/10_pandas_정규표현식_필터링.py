import os
import pandas as pd

# 파일 경로 입력
program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

# 엑셀 파일 입력
data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

# Customer Name 대문자 J 로 시작하는 행만 필터링
# condition = data_frame['Customer Name'].str.startswith('J')
condition = data_frame['Customer Name'].str.contains('^J')
data = data_frame[condition]

# 엑셀 파일 출력
writer = pd.ExcelWriter(output_file)
data.to_excel(writer, sheet_name='out_january_2013', index=False)
writer.close()