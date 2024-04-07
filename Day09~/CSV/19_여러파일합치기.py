import csv
import glob
import os

# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)

# 입력파일, 출력파일
input_path = path + '/input/' 
output_file = path + '/output/' + input('출력 파일 : ')

 
first_file = True
# glob 모듈을 사용해서, * 등의 와일드카드로 여러 파일을 매치해서 가져온다
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	print(os.path.basename(input_file))
	with open(input_file, 'r', newline='') as csv_in_file:
		with open(output_file, 'a', newline='') as csv_out_file:
			filereader = csv.reader(csv_in_file)
			filewriter = csv.writer(csv_out_file)
			if first_file:
				for row in filereader:
					filewriter.writerow(row)
				first_file = False
			else:
				header = next(filereader)
				for row in filereader:
					filewriter.writerow(row)