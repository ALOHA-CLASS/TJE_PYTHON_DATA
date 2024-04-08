import pandas as pd
import glob
import os

# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)
# 입력폴더, 출력파일
input_path = os.path.join(path, 'input')
output_file = os.path.join(path, 'output', input('출력 파일 : '))

# 모든 xlsx 파일 가져오기
all_workbooks = glob.glob(os.path.join(input_path, '*.xlsx'))

# 모든 파일의 Sale Amount의 합계와 평균 계산
total_sales = 0
total_sales_count = 0
for workbook in all_workbooks:
    df = pd.read_excel(workbook, sheet_name=None)  # 모든 워크시트를 읽어들임
    for sheet_name, data in df.items():
        total_sales += data['Sale Amount'].sum()
        total_sales_count += len(data)

average_sales = total_sales / total_sales_count

# 결과를 출력 파일에 저장
with open(output_file, 'w') as f:
    f.write(f'Total Sales: {total_sales}\n')
    f.write(f'Average Sales: {average_sales}\n')
