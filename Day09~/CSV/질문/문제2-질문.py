import pandas as pd
import re

def check_phone_number(phone_number):
    pattern = r'^\d{2,3}-\d{3,4}-\d{4}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False

import os
# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)

# 입력파일, 출력파일
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

pro2 = pd.read_csv(input_file)
pro2_new = pro2.copy()

for idx, phone_number in enumerate( pro2_new['전화번호'] ):
    if check_phone_number(phone_number):
        pass
    else :
        # 데이터프레임에서 특정 행 삭제
        pro2_new = pro2_new.drop(idx)          
        # pro2_new.drop(idx, inplace=True)          


pro2_new.to_csv(output_file, index=False)