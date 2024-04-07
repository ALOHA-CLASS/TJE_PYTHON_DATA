import sys
import pandas as pd

import os
# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)

# 입력파일, 출력파일
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

# 데이터 프레임
data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=False) # index=False : index 열 제외
# data_frame.to_csv(output_file)










