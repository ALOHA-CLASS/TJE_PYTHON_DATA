import csv
import sys

import os
# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)
# 입력파일, 출력파일
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file, delimiter=',')
		filewriter = csv.writer(csv_out_file, delimiter=',')
		for row_list in filereader:
			filewriter.writerow(row_list)
			



#	✅ 실행방법
#	python 파일명 "입력csv파일경로" "출력csv파일경로"
#	python .\02_csv모듈입출력.py "D:\ALOHA LABS\PYTHON\TJE_PYTHON_DATA\NEW\CSV\input\sample2.csv" "D:\ALOHA LABS\PYTHON\TJE_PYTHON_DATA\NEW\CSV\output\sample2.csv"