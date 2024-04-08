import sys

import os
# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)
# 입력파일, 출력파일
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

with open(input_file, 'r', newline='') as filereader:
	with open(output_file, 'w', newline='') as filewriter:
		header = filereader.readline()
		header = header.strip()
		header_list = header.split(',')
		print(header_list)
		filewriter.write(','.join(map(str,header_list))+'\n')
		for row in filereader:
			row = row.strip()
			row_list = row.split(',')
			print(row_list)
			filewriter.write(','.join(map(str,row_list))+'\n')


#	✅ 실행방법
#	python 파일명 "입력csv파일경로" "출력csv파일경로"
#	python .\01_csv파일입출력.py "D:\ALOHA LABS\PYTHON\TJE_PYTHON_DATA\NEW\CSV\input\sample.csv" "D:\ALOHA LABS\PYTHON\TJE_PYTHON_DATA\NEW\CSV\output\sample.csv"