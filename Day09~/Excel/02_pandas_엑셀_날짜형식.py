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
# read_excel( ) : 엑셀 파일 읽어드려서, 데이터프레임으로 반환
data_frame = pd.read_excel(input_file, sheet_name='january_2013') 

# ExcelWriter() : 쓰기 모드로 엑셀 파일 출력 객체 생성
writer = pd.ExcelWriter(output_file)

# to_excel( 출력객체, sheet_name=시트이름, index=여부 )
# : 데이터프레임을 엑셀 파일로 변환하여 저장하는 함수
data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)

# 파일 출력 후, 메모리 해제 close() 함수를 호출해주어야한다.
writer.close()