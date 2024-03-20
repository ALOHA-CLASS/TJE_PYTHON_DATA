# 무한반복
#   : 무조건 계속 반복하는 반복문
#     반드시, 종료조건을 넣어주어야 한다.

# break
# : 가장 가까운 반복문을 벗어나는 키워드

while True:
    name = input('코딩을 제일 잘하시는 분?') 
    # 종료조건
    if name == '장석주' or name == '김조은':
        print('정답입니다.')
        break
    else:
        print('틀렸습니다.')