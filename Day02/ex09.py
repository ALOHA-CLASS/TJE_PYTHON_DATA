# f-strings 형식 문자열
# f'{변수명}' 형식으로 문자열 안에 표현식을 바로 사용하여 출력한다.

age = 20
print(f'2023년엔 {age} 살이 됩니다')
print(f'2024년엔 {age+1} 살이 됩니다')
print(f'2025년엔 {age+2} 살이 됩니다')
print(f'2026년엔 {age+3} 살이 됩니다')


print( type(f'2026년엔 {age+3} 살이 됩니다') )