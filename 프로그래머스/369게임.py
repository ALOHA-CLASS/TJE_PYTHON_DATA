'''
    머쓱이는 친구들과 369게임을 하고 있습니다. 
    369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 
    숫자는 숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다. 
    머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때,
    머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.

    입력 : 386732
    출력 : 3
'''

def solution(order):
    answer = 0
    # 입력한 숫자를 한자리씩 접근
    text = str(order)

    # 반복을 통해서 한자리의 숫자가 3,6,9 인지 확인
    for ch in text:
        # print(ch + ' ')
        if ch == '3' or ch == '6' or ch == '9':
            # 3,6,9 이면 count 변수를 +1
            answer += 1
    return answer

print( solution(919230) )


