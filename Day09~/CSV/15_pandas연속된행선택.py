import pandas as pd
import sys

path = 'E:/ALOHA/JOEUN/GIT/TJE_PYTHON_DATA/Day09~/CSV'
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')


data_frame = pd.read_csv(input_file, header=None)

print('삭제 전')
print(data_frame)

header = data_frame.iloc[0]
# drop() 
# : 데이터프레임의 특정 행을 삭제하는 함수
data_frame = data_frame.drop([0,1,2,3,4])

print('삭제 후')
print(data_frame)


# iloc[0]
# : index를 기준으로 특정 행,열을 선택하는 함수
data_frame.columns = header

print('iloc[0] 이후')
print(data_frame)

# reindex()
# : 데이터프레임에서 행을 재구성하는 함수

# data_frame.reindex(data_frame.index.drop(3))
# - 인덱스 3인 행을 삭제 후, 삭제된 새로운 데이터프레임을 재구성하여 반환

# new_index = range( len(data_frame) )    # range( 8 ) -> (0:7)
# data_frame = data_frame.reindex([0,1,2,3,4,5,6,7])
# print('reindex() : 인덱스 재구성 후')
# print(data_frame)

# 인덱스 재구성
data_frame.reset_index(drop=True, inplace=True)
# data_frame.reset_index()
print('reset_index() ')
print(data_frame)


data_frame.to_csv(output_file, index=True)