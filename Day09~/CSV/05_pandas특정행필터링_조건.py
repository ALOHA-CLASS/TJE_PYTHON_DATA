import pandas as pd
import sys

path = 'E:/ALOHA/JOEUN/GIT/TJE_PYTHON_DATA/Day09~/CSV'
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

# csv 읽어서 데이터프레임으로 가져온다
data_frame = pd.read_csv(input_file)

# Cost 열에서 $ 기호를 제거, float(숫자) 타입으로 변환 (비교연산을 위해서)
data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)

# 특정행 필터링
# loc[ 행 라벨, 열 라벨 ]
# : 데이터 프레임에서 지정한 행과 열을 선택한 함수

data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name']\
.str.contains('Z')) | (data_frame['Cost'] > 600.0), :]
# ❓ OR  :  |,   AND  :  & 


# data_frame.loc[ (A | B), : ]
# : A 또는 B 조건을 만족하는 행을 선택하고, 모든 열을 선택 한다.
#   loc[ 행라벨, 열라벨 ]
#   ✅ 특정 행 또는 열을 선택하지 않는다면  :  으로 생략가능 

# | : OR 연산 ( A 또는 B )

# (data_frame['Supplier Name']\.str.contains('Z'))
# 1 - 데이터 프레임에서 'Supplier Name' 열을 문자열로 가져온다
# 2 - 'Supplier Name' 열에서 'Z' 가 포함된 여부를 반환한다. (True, False)

# (data_frame['Cost'] > 600.0)
# 1 - 데이터 프레임에서 'Cost' 열을 가져온다. (float)
# 2 - 600.0 초과인 여부를 반환한다. (True, False)

# 데이터프레임을 csv 파일로 출력
data_frame_value_meets_condition.to_csv(output_file, index=False)