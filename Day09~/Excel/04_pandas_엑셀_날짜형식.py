import pandas as pd 
import os

# 현재 실행 파일 경로 가져오고, 입력파일 지정하기
program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')    

# 엑셀 통합 문서의 jaunary_2013 입력하여 데이터프레임으로 반환
data_frame = pd.read_excel(input_file, sheet_name='january_2013')

# yyyy-mm-dd ---> yyyy/mm/dd 형식으로 변환
dates = data_frame['Purchase Date']
dates = pd.to_datetime(dates).dt.strftime('%Y/%m/%d')
data_frame['Purchase Date'] = dates


# 엑셀 출력 객체
writer = pd.ExcelWriter(output_file)
# 데이터프레임을 엑셀 파일로 저장 *index는 미사용
data_frame.to_excel(writer, sheet_name='out_jaunary_2013', index=False)
# 출력 객체 해제
writer.close()
