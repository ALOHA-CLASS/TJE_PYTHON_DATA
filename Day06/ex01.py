
# 텍스트 파일 생성

# 파일 저장 경로
path = 'E:/ALOHA/JOEUN/GIT/TJE_PYTHON_DATA/Day06/file/'
file = open(path + 'hello.txt', 'wt', encoding='UTF-8')

# 파일 내에서 출력 : write()
file.write('안녕하세요')
file.write('\n')
file.write('텍스트 파일 생성 실습입니다.')
# file.write('새로운 내용을 추가합니다.')

print('텍스트 파일이 생성되었습니다.')

# 파일 닫기
file.close()