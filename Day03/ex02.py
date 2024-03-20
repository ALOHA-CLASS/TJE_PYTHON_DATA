# 반복문
# : 조건을 만족할 때까지, 실행문을 반복하는 문장
# while 문
# while 조건식:
#       반복 실행할 문장1
#       반복 실행할 문장2

# 1~10 까지 반복하여 출력
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1       # i = i + 1

print()

# 1~50 까지 반복하여 합계
a = 1
sum = 0
while a <= 50:
    sum = sum + a
    print(a, end='')
    if a != 50:
        print('+', end='')
    a += 1

print('={}'.format(sum))
print('sum = {}'.format(sum))

