import pandas as pd
import os

# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)

# 입력파일, 출력파일
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

data_frame = pd.read_csv(input_file)

important_dates = ['1/20/14', '1/30/14']    # 특정 날짜 집합을 리스트로 선언

# 데이터프레임.loc[ 행라벨, 열라벨 ]
# : 데이터프레임의 특정 행 및 열을 선택하는 함수
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date']\
.isin(important_dates), :]

# data_frame['Purchase Date']  :  Series 객체
# -> 데이터 프레임에서 특정 열을 선택하면 그 구조는 시리즈가 된다.

# isin()
# : 해당 Series 객체의 특정 값이나 집합에 속하는지 여부를 반환 (True, False)

data_frame_value_in_set.to_csv(output_file, index=False)