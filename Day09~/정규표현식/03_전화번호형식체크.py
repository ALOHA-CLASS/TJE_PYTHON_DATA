import re

def check_phone_number(phone_number):
    pattern = r'^\d{2,3}-\d{3,4}-\d{4}$'
    # pattern = r'^\d{9,11}$'
    # 분석
    # \d{3}     : 숫자 3글자
    # \d{3,4}   : 숫자 3~4글자
    # \d{4}     : 숫자 4글자
    if re.match(pattern, phone_number):
        return True
    else:
        return False

# 테스트
phone_number = input('전화번호 : ')
if check_phone_number(phone_number):
    print("유효한 전화번호입니다.")
else:
    print("유효하지 않은 전화번호입니다.")
