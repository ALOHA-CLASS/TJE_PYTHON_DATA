import re

pattern = r'apple'
text = '''An apple a day keeps the doctor away.
I love apples.
'''

# re.findall()로 패턴 검색 (전역 검색)
matches = re.findall(pattern, text, re.DOTALL)

if matches:
    for match in matches:
        print("패턴 매치⭕ : ", match)
else:
    print("패턴 매치❌")
