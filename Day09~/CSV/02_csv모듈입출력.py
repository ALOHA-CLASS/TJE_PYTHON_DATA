import csv
# import sys

import os
# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)

# 입력파일, 출력파일
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

with open(input_file, 'r', newline='', encoding='UTF-8') as csv_in_file:
	with open(output_file, 'w', newline='', encoding='UTF-8') as csv_out_file:
		# csv_in_file 파일을 ',' 구분자 읽기모드로 CSV 파일 객체 생성
		filereader = csv.reader(csv_in_file, delimiter=',')
		# csv_out_file 파일을 ',' 구분자 쓰기모드로 CSV 파일 객체 생성
		filewriter = csv.writer(csv_out_file, delimiter=',')
		
        # 읽기모드의 파일 객체를 한 줄씩 읽어서 반복
		for row_list in filereader:
			# 쓰기모드의 파일 객체를 통해서 writerow() 함수로 한 줄 씩 출력
			filewriter.writerow(row_list)