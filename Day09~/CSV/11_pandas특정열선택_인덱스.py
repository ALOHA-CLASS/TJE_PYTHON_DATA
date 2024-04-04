import pandas as pd
import sys

path = 'E:/ALOHA/JOEUN/GIT/TJE_PYTHON_DATA/Day09~/CSV'
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')


data_frame = pd.read_csv(input_file)

# loc[ 행라벨 , 열라벨 ]
# : 행라벨, 열라벨으로 데이터 선택

# iloc[ 행index, 열index ]
# index + location - index 를 기반으로 데이터프레임의 행과 열을 선택하는 함수

# iloc[ 행 , 열 [0,3] ]
# : 0, 3 번 index 에 해당하는 열을 선택
# data_frame_column_by_index = data_frame.iloc[:, [0, 3]]

# 1~3열 (Supplier Name,Invoice Number,Part Number)를 선택
# - 리스트에 지정할 index 를 담아서 선택
# data_frame_column_by_index = data_frame.iloc[:, [0, 1, 2] ]

# - index 범위로 선택
data_frame_column_by_index = data_frame.iloc[:, 0:3 ]

data_frame_column_by_index.to_csv(output_file, index=False)