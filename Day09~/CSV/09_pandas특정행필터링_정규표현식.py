import pandas as pd
import re


path = 'E:/ALOHA/JOEUN/GIT/TJE_PYTHON_DATA/Day09~/CSV'
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')


data_frame = pd.read_csv(input_file)

# ix[ , ]
# : deperecated (더 이상 사용 권장) ➡ 버전 업데이트 되면서 새로 다른 문법이 대체
#   ix[ , ]  ➡  loc[ , ]

# '001-' 로 시작하는 행을 선택하여 반환
# condition = data_frame['Invoice Number'].str.startswith("001-")
# 'Z' 로 끝나는 행을 선택하여 반환
# condition = data_frame['Supplier Name'].str.endswith('Z')

# match(정규표현식) : 문자열에서 정규표현식에 따라 패턴 매칭
pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)
condition = data_frame['Invoice Number'].str.match(pattern)

data_frame_value_matches_pattern = data_frame.loc[ condition, : ]

data_frame_value_matches_pattern.to_csv(output_file, index=False)