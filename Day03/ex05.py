# for 문과 range() 함수
# range()   : 범위를 생성하는 함수
# 구조      : range( 초기값, 종료값+1, 증감값 )

# range(5)      : 0,1,2,3,4
# range(1,11)   : 1,2,3,4,...,10
# range(1,10,2) : 1,3,5,7,9

# 단을 입력받아서 구구단을 출력하시오.
dan = input('단 : ')
dan = int(dan)
for n in range(1,10,1):
    print('{} x {} = {}'.format(dan, n, dan*n))