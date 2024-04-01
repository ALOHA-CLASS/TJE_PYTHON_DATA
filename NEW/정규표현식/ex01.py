import re

def check_username(username):
    pattern = r'^[a-zA-Z0-9_-]{4,16}$'
    if re.match(pattern, username):
        return True
    else:
        return False

# 테스트
username = input("아이디 : ")
if check_username(username):
    print("유효한 아이디입니다.")
else:
    print("유효하지 않은 아이디입니다.")
