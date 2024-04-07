import csv
import re
import os

# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)

# 입력파일, 출력파일
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

# 정규 표현식 패턴 설정
pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)
#  re.I   : 대소문자 구분 없이 매칭

print('pattern : {}'.format( pattern ))

# ^001-.* 
# 1 - ^001- : 001- 로 시작하는 패턴 매칭
# 2 - .*	: . 은 한문자 대체, * 0 회이상 ➡ 한 문자 이상 매칭
# ➡ 001- 뒤에 한 문자 이상인 패턴을 매칭


with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			invoice_number = row_list[1]			# invoice_number
			if pattern.search(invoice_number):		# 패턴 확인
				filewriter.writerow(row_list)