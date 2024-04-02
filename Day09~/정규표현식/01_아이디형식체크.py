import re

def check_username(username):
    pattern = r'^[a-zA-Z0-9_-]{4,16}$'
    # 아이디 
    # 영어 대소문자 + 숫자 + 특수문자( _ - )
    # 글자수 : 4글자 이상 16글자 이하

    # re.match( 패턴, 확인할 문자열 )
    # 유효 ⭕ : True
    # 유효 ❌ : False
    if re.match(pattern, username):
        return True
    else:
        return False

# 테스트
username = input('아이디 : ')
if check_username(username):
    print("유효한 아이디입니다.")
else:
    print("유효하지 않은 아이디입니다.")
