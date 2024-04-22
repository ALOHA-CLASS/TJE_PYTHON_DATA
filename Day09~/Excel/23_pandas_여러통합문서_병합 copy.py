
import pandas as pd 

import tkinter as tk
from tkinter import filedialog

import os
import glob

# 입력 파일 선택 버튼 클릭 시,
def open_input_file():
    print('입력 파일 선택...')
    # 파일 선택 상자에서 파일이름 가져오기
    directory_name = filedialog.askdirectory()
    if directory_name:
        # 파일명 지정
        input_file.set(directory_name)


# 출력 파일 선택 버튼 클릭 시,
def open_output_file():
    print('출력 파일 선택...')
    # 파일 선택 상자에서 파일이름 가져오기
    filename = filedialog.asksaveasfilename()
    if filename:
        # 파일명 지정
        output_file.set(filename)

# 실행 버튼
def run():
    print('입력 파일 경로 : ' + input_file.get())
    print('출력 파일 경로 : ' + output_file.get())
    print('데이터 분석을 시작합니다...')
    work()

# 데이터 분석
def work():
    # 여러 엑셀 파일 가져오기
    input_path = input_file.get()
    all_workbooks = glob.glob(os.path.join(input_path, '*.xlsx'))

    data_frames = []
    for workbook in all_workbooks:
        all_worksheets = pd.read_excel(workbook, sheet_name=None, \
                                       index_col=None)
        for worksheet_name, data in all_worksheets.items():
            data_frames.append(data)
    all_data = pd.concat(data_frames, axis=0, ignore_index=True)

    # 엑셀 출력 객체
    writer = pd.ExcelWriter(output_file.get())
    # 데이터프레임을 엑셀 파일로 저장 *index는 미사용
    all_data.to_excel(writer, sheet_name='모든 엑셀 통합', index=False)
    # 출력 객체 해제
    writer.close()



# 윈도우 화면 생성
window = tk.Tk()
window.title('GUI 프로그램')

# 창 크기 지정
window.geometry('600x300')

# 라벨 생성
label = tk.Label(window, text="GUI 프로그램 라벨", padx=20, pady=10)
label.pack()

# 입력 상자 생성 - 입력 파일 경로
input_file = tk.StringVar()         # 문자열 변수 
input_entry = tk.Entry(window, textvariable=input_file, width=100)
input_entry.pack()

# 버튼 - 입력 파일 선택 버튼
input_button = tk.Button(window, text="입력 파일 선택", command=open_input_file)
input_button.pack()


# 입력 상자 생성 - 출력 파일 경로
output_file = tk.StringVar()         # 문자열 변수 
output_entry = tk.Entry(window, textvariable=output_file, width=100)
output_entry.pack()

# 버튼 - 입력 파일 선택 버튼
output_button = tk.Button(window, text="출력 파일 선택", command=open_output_file)
output_button.pack()

# 실행 버튼
run_button = tk.Button(window, text="실행", padx=10, pady=10, command=run)
run_button.pack()

window.mainloop()