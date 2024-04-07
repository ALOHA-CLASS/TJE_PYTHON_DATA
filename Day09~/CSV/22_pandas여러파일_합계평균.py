import pandas as pd
import glob
import os

program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)

# 입력경로, 출력파일
input_path = path + '/input/' 
output_file = path + '/output/' + input('출력 파일 : ')

all_files = glob.glob(os.path.join(input_path,'sales_*'))
all_data_frames = []
for input_file in all_files:
	data_frame = pd.read_csv(input_file, index_col=None)
	
	# 합계
	# 1. 데이터 프레임에서 Sales Amount 열 선택
	# 2. 리스트 내포로 데이터에서 $ 및 , 기호 제거
	# 3. 판다스 DataFrame의 sum() 함수로 리스트의 합계 구함
	total_sales = pd.DataFrame([float(str(value).strip('$').replace(',','')) \
						for value in data_frame.loc[:, 'Sale Amount']]).sum()
	# 평균
	# 1. 데이터 프레임에서 Sales Amount 열 선택
	# 2. 리스트 내포로 데이터에서 $ 및 , 기호 제거
	# 3. 판다스 DataFrame의 mean() 함수로 리스트의 평균 구함
	average_sales = pd.DataFrame([float(str(value).strip('$').replace(',','')) \
						for value in data_frame.loc[:, 'Sale Amount']]).mean()

	# data 딕셔너리 선언
	data = {'file_name': os.path.basename(input_file),
			'total_sales': total_sales,
			'average_sales': average_sales}
	
	# data 딕셔너리로 컬럼명을 지정하여, 데이터 프레임 리스트에 한 CSV 파일의 합계 및 평균 추가
	all_data_frames.append(pd.DataFrame(data, columns=['file_name', 'total_sales', 'average_sales']))

# 데이터 프레임 리스트(각 CSV 파일의 합계평균 리스트)를 하나의 데이터 프레임으로 병합
data_frames_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)

# 데이터 프레임을 CSV 파일로 출력
data_frames_concat.to_csv(output_file, index = False)