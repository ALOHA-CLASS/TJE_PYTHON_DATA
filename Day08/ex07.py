# 제너레이터
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # 출력: 1
print(next(gen))  # 출력: 2
print(next(gen))  # 출력: 3


print()
# 
def mygen():
    for i in range(1, 1000):
        result = i * 10
        yield result

gen = mygen()

print( next(gen) ) 
print( next(gen) ) 
print( next(gen) )