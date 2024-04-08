# 파일명을 담고 있는 리스트
file_names = [
    "01_엑셀입력.py",
    "02_엑셀입출력.py",
    "03_엑셀_날짜형식.py",
    "04_pandas_엑셀_날짜형식.py",
    "05_특정행_필터링.py",
    "06_pandas_특정행_필터링.py",
    "07_집합으로_필터링.py",
    "08_pandas_집합으로_필터링.py",
    "09_정규표현식으로_필터링.py",
    "10_pandas_정규표현식으로_필터링.py",
    "11_index로_열선택.py",
    "12_pandas_index로_열선택.py",
    "13_헤더로_열선택.py",
    "14_pandas_헤더로_열선택.py",
    "15_모든worksheet_특정행_필터링.py",
    "16_pandas_모든worksheet_특정행_필터링.py",
    "17_모든worksheet_특정열_선택.py",
    "18_pandas_모든worksheet_특정열_선택.py",
    "19_모든worksheet_집합으로_특정행_필터링.py",
    "20_pandas_모든worksheet_집합으로_특정행_필터링.py",
    "21_통합문서_행열개수.py",
    "22_여러통합문서_병합.py",
    "23_pandas_여러통합문서_병합.py",
    "24_통합문서_합계평균.py",
    "25_pandas_통합문서_합계평균.py"
]

# 파일을 생성하는 반복문
for file_name in file_names:
    with open(file_name, 'w') as f:
        pass  # 파일 내용이 없으므로 pass 문을 사용하여 빈 파일 생성

print("파일 생성이 완료되었습니다.")
