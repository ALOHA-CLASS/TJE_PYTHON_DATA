
# csv 파일 읽어오기

import csv

path = 'E:/ALOHA/JOEUN/GIT/TJE_PYTHON_DATA/Day06/file/'
file = path + 'test.csv'

with open(file, 'r', newline='', encoding='UTF-8') as file:
    # reader(파일객체, delimiter(구분기호), quotechar(문자열기호))
    # quotechar : 나뉘면 안되는 데이터를 어떤 기호로 묶을지 지정
    csv_reader = csv.reader(file, delimiter=',', quotechar="'")
    for line in csv_reader:
        print(line)
