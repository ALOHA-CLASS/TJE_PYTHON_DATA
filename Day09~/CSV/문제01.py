"""
    supplier_data.csv 파일을 입력하여,
    Supplier Y 공급업체 또는 Supplier Z 공급업체라면 가격이 650 초과인
    데이터를 문제01.csv 파일로 출력하시오.

"""

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
		filereader = csv.reader(csv_in_file)        # csv 읽기 모드 객체 생성
		filewriter = csv.writer(csv_out_file)       # csv 쓰기 모드 객체 생성
		header = next(filereader)                   # 첫 행을 입력
		filewriter.writerow(header)                 # 첫 행을 출력
		for row_list in filereader:
			supplier = str(row_list[0]).strip()                 # 공급업체명
			cost = str(row_list[3]).strip('$').replace(',', '') # 가격
			# 조건으로 특정행 필터
			if supplier == 'Supplier Y' or (supplier == 'Supplier Z' and float(cost) > 650.0):
				filewriter.writerow(row_list)