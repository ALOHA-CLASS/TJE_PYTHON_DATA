
print('#1 절댓값')
print( abs(-10) )

print('#2 몫과 나머지')
money = 10000
price = 3000

result = divmod(money, price)
print('커피를 {}개 사고, {}원이 남았습니다.'.format(result[0],result[1]))

print('#3 실수로 변환')
a = '3.14'
print( float(a) + 0.06 )

print('#4 정수로 변환')
b = '15'
print( int(b) + 5 )

print('#5 입력값을 분리')
# split()       : 입력값을 구분자를 기준으로 분리하는 함수
x, y, z = input('정수 3개를 입력하세요 : ').split()
x = int(x)
y = int(y)
z = int(z)

print('#6 최댓값')
print('최댓값: {} '.format( max(x,y,z) ))

print('#7 최댓값')
print('최솟값: {} '.format( min(x,y,z) ))

print('#8 제곱')
print('2^3 : {}'.format( pow(2,3) ))
print('2^4 : {}'.format( pow(2,4) ))


print('#9 반올림')
print('round(1.5) : {}'.format( round(1.5) ))
print('round(1.4) : {}'.format( round(1.4) ))
print('round(1.55,1) : {}'.format( round(1.55, 1) ))
print('round(2.675,2) : {}'.format( round(2.675, 2) ))

print('#10 합계')
li = [10,20,30,40,50]
print('sum(li) = {}'.format( sum(li) ))
