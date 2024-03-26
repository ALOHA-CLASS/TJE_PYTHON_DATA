# 파일 복사
path = 'E:/ALOHA/JOEUN/GIT/TJE_PYTHON_DATA/Day06/file/'
file = path + 'hello.txt'
copy = path + 'hello(복사).txt'

buffer_size = 1024      # 버퍼 용량 : 1024Byte(1KB)


# source        : 원본 파일 객체
# copyfile      : 복사 파일 객체
with open(file, 'rb') as source:
    with open(copy, 'wb') as copyfile:
        while True:
            # 원본 파일을 버퍼용량만 읽어와서 buffer 에 저장
            # buffer 에는 1KB 만큼의 파일 데이터가 저장
            buffer = source.read(buffer_size)
            if not buffer:
                break
            # 1KB 씩 파일 생성
            copyfile.write(buffer)
            

print(copy)
print('파일이 복사되었습니다.')