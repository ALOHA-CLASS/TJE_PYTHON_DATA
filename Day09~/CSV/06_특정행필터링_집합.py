import csv
import os

# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)

# 입력파일, 출력파일
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

important_dates = ['1/20/14', '1/30/14']    # 특정 날짜 집합을 리스트로 선인

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		filewriter.writerow(header)
		
		for row_list in filereader:
			a_date = row_list[4]            # 구매일자
			if a_date in important_dates:   # 특정 리스트에 포함 여부 반환
				filewriter.writerow(row_list)