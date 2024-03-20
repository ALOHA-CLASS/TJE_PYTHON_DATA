# 반복문

# for 반복문
# for 변수 in (리스트, 튜플 등 컬렉션):

li = [1,2,3,4,5]

for n in li:
    print(n, end=' ')
print()

# 리스트 요소 합계
sum = 0
for a in li:
    sum += a
    a += 1

print('sum = {}'.format(sum))
