import sys
import pandas as pd

import os
# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)
# 입력파일, 출력파일
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=False)


#	✅ 실행방법
#	python 파일명 "입력csv파일경로" "출력csv파일경로"
#	python .\03_pandas입출력.py "D:\ALOHA LABS\PYTHON\TJE_PYTHON_DATA\NEW\CSV\input\sample3.csv" "D:\ALOHA LABS\PYTHON\TJE_PYTHON_DATA\NEW\CSV\output\sample3.csv"