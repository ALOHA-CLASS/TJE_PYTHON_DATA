"""
    문제02.csv 파일을 입력받아
    전화번호 컬럼의 데이터에 대하여
    전화번호 형식의 정규표현식으로 매칭되는
    데이터만 추출하시오.

"""

import pandas as pd
import re

import os
# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)

# 입력파일, 출력파일
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

data_frame = pd.read_csv(input_file)

# match(정규표현식) : 문자열에서 정규표현식에 따라 패턴 매칭
# 전화번호 형식을 매칭하는 정규표현식
# : ^\d{2,3}-\d{3,4}-\d{4}$
pattern = re.compile(r'(?P<my_pattern_group>^\d{2,3}-\d{3,4}-\d{4}$)', re.I)
condition = data_frame['전화번호'].str.match(pattern)

# (추가문제) 전화번호 형식이 매칭되지 않는 행의, 전화번호 열만 추출하시오.
# condition = ~data_frame['전화번호'].str.match(pattern)
# ✅ 시리즈 개체의 부정연산(NOT) 시에는 ~ 기호를 사용한다.

data_frame_value_matches_pattern = data_frame.loc[ condition, : ]

data_frame_value_matches_pattern.to_csv(output_file, index=False)