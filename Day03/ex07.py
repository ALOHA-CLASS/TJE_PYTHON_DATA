# 리스트 내포
# : 리스트 내부에 for 문을 사용하여
#   리스트 요소를 효율적으로 저장하는 방식

# 문법
#       리스트 = [표현식 for 변수 in 컬렉션]

# [1,2,3,4,5] --> [2,4,6,8,10]
li = [1,2,3,4,5]

# 리스트 내포 사용 ❌
newList = []
for i in li:
    newList.append(i*2)
print('newList : ',newList)


# 리스트 내포 사용 ⭕
a = [ n * 2 for n in li ]
print('a : ',a)

b = [ n * 10 for n in li if n%2==0 ]
print('b : ',b)

