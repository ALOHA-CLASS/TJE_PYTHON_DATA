import pandas as pd

# 입력 및 출력 파일 경로 정의
path = 'E:/ALOHA/JOEUN/GIT/TJE_PYTHON_DATA/Day09~/Excel'
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')


# read_excel() 함수를 사용하여 Excel 파일 읽기
data_frame = pd.read_excel(input_file, sheet_name='january_2013') 

# ExcelWriter() 함수로 출력 객체 생성 시에는
# 반드시 출력 후 close() 를 해야한다.  (with 구문을 쓰면 close() 자동으로 된다.)
with pd.ExcelWriter(output_file) as writer:
    data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)

print("Excel 파일이 성공적으로 생성되었습니다.")
