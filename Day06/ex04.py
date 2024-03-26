# 파일 삭제
# os 모듈에 파일 삭제 기능이 정의되어 있다.
import os

path = 'E:/ALOHA/JOEUN/GIT/TJE_PYTHON_DATA/Day06/file/'
file = input('삭제할 파일명 : ')
file = path + file

# 파일 존재 여부
if os.path.exists(file):
    # 파일 삭제
    os.remove(file)
    print('파일이 삭제되었습니다.')
else:
    print('파일이 존재하지 않습니다.')
