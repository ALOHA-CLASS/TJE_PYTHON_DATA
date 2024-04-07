import pandas as pd
import glob
import os

program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)

# 입력경로, 출력파일
input_path = path + '/input/' 
output_file = path + '/output/' + input('출력 파일 : ')

# glob.glob() 함수로, input_path에서 sales_로 시작하는 모든 파일의 경로를 생성
all_files = glob.glob(os.path.join(input_path,'sales_*'))

all_data_frames = []
# 여러 파일 경로들을 반복하여 csv 파일을 입력
for file in all_files:
	data_frame = pd.read_csv(file, index_col=None)	# CSV 파일 입력
	all_data_frames.append(data_frame)				# 리스트에 데이터 프레임 추가

# concat() 함수로 데이터프레임 리스트를 하나의 데이터프레임으로 병합
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)	

# 데이터프레임을 CSV 파일로 출력
data_frame_concat.to_csv(output_file, index = False)