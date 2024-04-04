import sys
from xlrd import open_workbook

path = 'E:/ALOHA/JOEUN/GIT/TJE_PYTHON_DATA/Day09~/Excel'
input_file = path + '/input/' + input('입력 파일 : ')
# input_file = sys.argv[1]

# open_workbook( 파일 경로 ) : 지정한 엑셀 파일을 열어서 WorkBook 객체로 가져온다.
workbook = open_workbook(input_file)    

# workbook.nsheets : 엑셀 파일 내의 시트 개수
print('시트 개수 : ', workbook.nsheets)

# sheets() : 모든 시트를 리스트로 반환
# - name    : 시트 이름
# - nrows   : 행 수
# - ncols   : 열 수
for worksheet in workbook.sheets():
	print("시트 이름 :", worksheet.name, "\t행 수:", \
			worksheet.nrows, "\열 수:", worksheet.ncols)
