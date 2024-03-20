# 논리 연산자
# and   : A and B 와 같은 조건에서, 모두 참일 때 결과가 참       
#  * 쇼트 서킷 : A 가 False 이면, B 를 검사하지 않는다. 

# or    : A or B 와 같은 조건에서, 둘중에 하나만이라도 참이면 결과가 참
#  * 쇼트 서킷 : A 가 True 이면, B 를 검사하지 않는다.

# not   : true->false, false->true

a = 10
b = 5

print('{} > 7 and {} > 7 : {}'.format(a, b, a>7 and b>7))
print('{} > 7 or {} > 7 : {}'.format(a, b, a>7 or b>7))

print('not : {} : {}'.format(a, not a))
print('not : {} : {}'.format(0, not 0))


