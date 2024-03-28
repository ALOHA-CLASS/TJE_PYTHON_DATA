# 이터레이터

list = [1,2,3,4,5]
# 방법 1
iter_obj = iter(list)
i = 0
while i < len(list):
    print( next(iter_obj) )
    i += 1
# 방법 2
iter_obj = iter(list)
while True:
    next_element = next(iter_obj, None) # 다음요소가 없으면 None
    if next_element is None:
        print('마지막')
        break
    print(next_element)

# 응용
iter_obj = iter(list)
while True:
    next_element = next(iter_obj, None)
    print(next_element, end="")
    if next_element is None:
        break
    
    if next_element is not None:
        print(',', end='')
    