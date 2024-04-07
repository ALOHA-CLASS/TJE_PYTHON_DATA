from openpyxl import load_workbook
import os

program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)
input_file = path + '/input/' + input('입력 파일 : ')
# sales_2013.xlsx

# 엑셀 파일 로드
# load_workbook : 지정한 엑셀 파일 읽어와서 WorkBook 객체로 가져온다.
workbook = load_workbook( input_file )

# 첫 번째 시트 선택
sheet = workbook.active

# 시트 내용 출력
# iter_rows() : 시트에서 행들을 반복가능한 객체로 반환 
for row in sheet.iter_rows(values_only=True):
    print(row)
