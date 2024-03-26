
# 텍스트 파일 내용 추가

# 파일 저장 경로
path = 'E:/ALOHA/JOEUN/GIT/TJE_PYTHON_DATA/Day06/file/'
file = open(path + 'hello.txt', 'at', encoding='UTF-8')
# at : 추가모드 + 텍스트모드

# 추가할 내용
file.write('새로운 내용을 추가합니다.')
print('텍스트 파일에 새로운 내용이 추가되었습니다.')

# 파일 닫기
file.close()