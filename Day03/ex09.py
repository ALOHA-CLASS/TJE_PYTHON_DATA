# continue
# : 뒤의 남은 실행문 건너뛰고, 다음 반복으로 점프

# 짝수의 합계
a = 0
sum = 0

while a <= 20:
    a = a + 1
    # 홀수인 경우
    if a % 2 == 1:
        continue
    sum += a            # sum = sum + a

print('1~20 사이의 합계 : {}'.format(sum))