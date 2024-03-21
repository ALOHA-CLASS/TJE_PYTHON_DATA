# 모듈
'''
    모듈이란?
    : 변수나 함수 또는 클래스를 모아놓은 파이썬 파일
    - 하나의 파이썬 파일(.py)
    
    모듈 사용
    : import 모듈명
'''

import converter as c
# from converter import *

# 150km --> miles 단위로 변환
miles = c.kilometer_to_miles(150)
print('150km = {} miles'.format( miles ))

# 1000g --> pound 로 변환
pound = c.gram_to_pound(1000)
print('1000g = {} pound'.format( pound ))