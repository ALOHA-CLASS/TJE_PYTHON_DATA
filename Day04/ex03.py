'''
    사용자 함수
    : 사용자가 직접 정의한 함수

    # 함수 정의 키워드 : def

    def 함수명( 매개변수1, 매개변수2, ... ):
        실행문
        실행문
        return 반환값
    
    return 
    1. 함수를 종료
    2. 반환값을 함수를 호출한 자리로 대입
'''

a = 10
b = 2

def plus(a, b):
    result = a + b
    return result

def minus(a, b):
    result = a - b
    return result

def mul(a, b):
    result = a * b
    return result

def div(a, b):
    result = a / b
    return result

# 함수 호출
print('a + b = {}'.format( plus(a,b) ))
print('a - b = {}'.format( minus(a,b) ))
print('a * b = {}'.format( mul(a,b) ))
print('a / b = {}'.format( div(a,b) ))