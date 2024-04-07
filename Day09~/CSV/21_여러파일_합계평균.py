import csv
import glob
import os

program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)

# 입력경로, 출력파일
input_path = path + '/input/' 
output_file = path + '/output/' + input('출력 파일 : ')

output_header_list = ['file_name', 'total_sales', 'average_sales']

csv_out_file = open(output_file, 'a', newline='')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_header_list)

# "sales_" 로 시작하는 여러 파일 경로 생성
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	# salse_2013.csv, salse_2014.csv, ... 차례로 읽어옴
	with open(input_file, 'r', newline='') as csv_in_file:
		filereader = csv.reader(csv_in_file)
		output_list = [ ]
		# 읽어온 CSV 파일경로를 출력 데이터 리스트에 추가
		output_list.append(os.path.basename(input_file))
		header = next(filereader)
		# 합계, 개수 변수 선언
		total_sales = 0.0
		number_of_sales = 0.0
		for row in filereader:
			sale_amount = row[3]
			# 합계 계산
			total_sales += float(str(sale_amount).strip('$').replace(',',''))
			# 개수 카운팅
			number_of_sales += 1.0
		# 평균 계산
		average_sales = '{0:.2f}'.format(total_sales / number_of_sales)
		# 출력 데이터 리스트에 합계 추가
		output_list.append(total_sales)
		# 출력 데이터 리스트에 평균 추가
		output_list.append(average_sales)
		# [입력파일명.csv,합계,평균] 형식으로 한 줄 출력
		filewriter.writerow(output_list)
csv_out_file.close()
