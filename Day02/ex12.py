# 멤버쉽 연산자
# a in C    : 컬렉션 C 요소에 a 가 표함되어 있으면 True
#             그렇지않으면 False

a = [1,2,3]

x = 3 in a
y = 10 in a
z = 100 not in a

print('x : {}'.format(x))
print('y : {}'.format(y))
print('z : {}'.format(z))
