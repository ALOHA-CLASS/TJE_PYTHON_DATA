import csv
import glob
import os

program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)
# 입력경로, 출력파일
input_path = path + '/input/'

file_counter = 0
# glob.glob() 함수로, input_path에서 sales_로 시작하는 모든 파일의 경로를 생성
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
    row_counter = 1  # 각 파일의 행 수를 세기 위한 변수 초기화
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader)  # 첫 번째 행은 헤더
        for row in filereader:
            row_counter += 1  # 각 행마다 행 수 증가
    # 파일 이름, 행 수, 열 수 출력
    print('{0!s}: \t{1:d} rows \t{2:d} columns'.format(\
        os.path.basename(input_file), row_counter, len(header)))
    file_counter += 1  # 파일 수 증가
print('Number of files: {0:d}'.format(file_counter))  # 총 파일 수 출력
