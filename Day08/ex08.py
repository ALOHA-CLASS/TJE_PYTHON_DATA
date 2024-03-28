
def greet(name: str) -> str:
    return "Hello, " + name

# 출력: Hello, Alice
print(greet("Alice"))  
# 출력: TypeError: Argument 'name' must be str
print(greet(123))      
