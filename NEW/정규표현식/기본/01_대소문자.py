import re

# 정규 표현식 
# - 문자열 apple 매치되는 경우를 전역에서 검색
pattern = r'(?i)apple'

text_list = ['apple', 'Apple', 'APPLE', 'aPPle', 'app']

for text in text_list:
    # re.match()로 패턴 확인
    match = re.match(pattern, text)

    if match:
        print("패턴 매치⭕ : ", match.group())
    else:
        print("패턴 매치❌")
