import re

# (?m) 다중 행모드(MULTILINE)가 아닌 경우
pattern = r'^apple'
text = '''apple - 첫째 줄의 사과
apple - 둘째 줄의 사과
'''

# re.findall()로 패턴 검색 (전역 검색)
matches = re.findall(pattern, text)

if matches:
    for match in matches:
        print("패턴 매치⭕ : ", match)
else:
    print("패턴 매치❌")
