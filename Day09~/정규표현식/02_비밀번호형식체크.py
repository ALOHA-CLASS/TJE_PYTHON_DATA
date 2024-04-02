import re

def check_password(password):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    # 분석
    # 1 - (?=.*[A-Za-z])    : 문자가 최소 1글자 이상
    # 2 - (?=.*\d)          : 숫자가 최소 1글자 이상
    # 3 - [A-Za-z\d]        : 영문자 + 숫자 가능
    # 4 - {8,}              : 8글자 이상

    # 조건
    # - 문자가 하나이상, 숫자도 하나이상 포함된 문자열
    # - 글자수 : 최소 8글자
    if re.match(pattern, password):
        return True
    else:
        return False

# 테스트
password = input("비밀번호 : ")
if check_password(password):
    print("유효한 비밀번호입니다.")
else:
    print("유효하지 않은 비밀번호입니다.")
