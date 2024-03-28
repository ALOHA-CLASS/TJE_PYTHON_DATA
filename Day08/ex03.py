
# 데코레이터 함수 정의
def my_decorator(func):
    # 내부 함수 정의
    def wrapper():
        print('함수가 호출되기전...')
        func()      # 입력받은 함수 호출
        print('함수 호출 후...')

    return wrapper

# 데코레이터를 사용하여 sample() 함수에 장식
@my_decorator       
def sample():
    print('데코레이터 함수로 장식된 함수...')

sample()