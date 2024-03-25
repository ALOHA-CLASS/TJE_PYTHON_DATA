try:
    file = open('존재하지않는파일.txt')
    line = file.readline()
    print(line)
except OSError as err:
    print('예외 정보 : ', err.args)
    print('예외 번호 : ', err.args[0])
    print('예외 메시지 : ', err.args[1])
    print('예외 정보 : ', err)
except:
    print('알 수 없는 예외 발생...')
else:
    print('정상적으로 파일을 읽어왔습니다.')