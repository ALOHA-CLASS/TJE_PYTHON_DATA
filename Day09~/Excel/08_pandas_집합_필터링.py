import os
import pandas as pd

# 파일 경로 입력
program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

# 엑셀 파일 입력
# pd.read_excel(파일명, 시트명, index_col=None, parse_dates=['컬럼'])
# * parse_dates=['컬럼'] : 지정한 컬럼을 datetime 형식으로 변환
data_frame = pd.read_excel(input_file, 'january_2013', \
                           index_col=None, parse_dates=['Purchase Date'])

# 집합으로 필터링
important_dates = ['01/06/2013', '01/11/2013']
# 문자열형식('01/06/2013')을 datatime 형식으로 변환
important_dates = pd.to_datetime(important_dates, format='%m/%d/%Y')

# 필터링
data = data_frame[data_frame['Purchase Date'].isin(important_dates)]

# 날짜 형식 지정
dates = data_frame['Purchase Date']
dates = dates.dt.strftime('%Y/%m/%d')
data['Purchase Date'] = dates

# 파일 출력
writer = pd.ExcelWriter(output_file)
data.to_excel(writer, sheet_name='out_january_2013', index=False)
writer.close()





