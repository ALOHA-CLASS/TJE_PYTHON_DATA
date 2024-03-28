def mul(m):
    # 클로저
    def wrapper(n):
        return m * n
    return wrapper

mul3 = mul(3)   # wrapper() m:3
mul5 = mul(5)   # wrapper() m:5

print(mul3(10))
print(mul5(10))