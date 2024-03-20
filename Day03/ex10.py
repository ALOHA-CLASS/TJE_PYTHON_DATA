# 컬렉션 반복

# 리스트 반복
for a in [1,2,3,4,5]:
    print(a, end=' ')
print()

# 튜플 반복
for b in (1,2,3,4,5):
    print(b, end=' ')
print()

# 세트 반복
for c in {'a','b','c','d','e'}:
    print(c, end=' ')
print()

# 딕셔너리 반복
dic = {
    'coffee':   '커피',
    'star'  :   '별',
    'space' :   '우주',
    'apple' :   '사과'
}

for word in dic:
    print('{} 의 뜻 \t: {}'.format(word, dic.get(word) ))

# 딕셔너리.get(key)     : key 에 해당하는 값을 가져오는 함수






