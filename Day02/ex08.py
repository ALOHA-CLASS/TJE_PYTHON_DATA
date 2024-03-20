# format() 메소드
# {} 괄호 기호를 변수나 값이 표시될 위치(형식)을
# 지정하여 출력하는 메소드

print('내 이름은 {}'.format('김조은'))


a = 10
b = 20
print('a  : {}, b : {}'.format(a, b))

# index를 지정하여 사용할 수 있다
print('b  : {1}, a : {0}'.format(a, b))


print('{0}하세요, 저는 김조은 {1}. 과목은 파이썬{1} 다시 만나요~ {0}~'.format('안녕', '입니다'))

tel1,tel2,tel3 = '02', '1234', '3688'
print('연락처 : {0}-{1}-{2}'.format(tel1, tel2, tel3))

academy = '더조은'
print('name : {name}, age : {age}'.format(age=20, name=academy))



