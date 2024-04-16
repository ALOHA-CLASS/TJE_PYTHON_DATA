import pandas as pd 
import os

# 현재 실행 파일 경로 가져오고, 입력파일 지정하기
program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')    

# 엑셀 통합 문서의 jaunary_2013 입력하여 데이터프레임으로 반환
data_frame = pd.read_excel(input_file, sheet_name='january_2013')

# 데이터프레임에서 'Sale Amount' 컬럼(시리즈) 선택하여 
# 실수형으로 변환 후, 1500 보다 큰 경우의 논리값과 일치하는 행만 필터링
condition = data_frame['Sale Amount'].astype(float) > 1500.0
output_data = data_frame[ condition ]

# 파일 출력
writer = pd.ExcelWriter(output_file)
output_data.to_excel(writer, sheet_name='out_january_2013', index=False)
writer.close()