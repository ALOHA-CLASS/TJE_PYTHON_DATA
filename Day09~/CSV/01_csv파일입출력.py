import sys

path = 'E:/ALOHA/JOEUN/GIT/TJE_PYTHON_DATA/Day09~/CSV'
input_file = path + '/input/' + input('입력 파일 : ')
output_file = path + '/output/' + input('출력 파일 : ')

# with : 파일 객체를 자동으로 close() 하는 키워드

# 읽기모드로 input_file 파일 열어서 filereader 객체로 사용
with open(input_file, 'r', newline='', encoding='UTF-8') as filereader:
	# 쓰기모드로 output_file 파일 열어서 filewriter 객체로 사용
	with open(output_file, 'w', newline='', encoding='UTF-8') as filewriter:
		# header  예시 :  학번,이름,전화번호,학년  
		header = filereader.readline()  # 첫 행 읽기
		header = header.strip()         # strip() : 양쪽 공백 제거
		# header_list 예시 : [학번,이름,전화번호,학년]
		header_list = header.split(',') # , 기준으로 문자열 분리
		print(header_list)
		# map(str,header_list) 
		# : header_list 리스트를 반복하여 str 문자열로 변환한다
		# 문자열.join( 추가문자열 )
		# : 문자열에 추가 문자열을 사이사이에 넣어준다.
		# 학번 이름 전화번호 학년
		# '학번,이름,전화번호,학년'   - ','.join(map(str,header_list)) : T
		# '학번,이름,전화번호,학년\n' - T + '\n' 
		filewriter.write(','.join(map(str,header_list))+'\n')
		
		for row in filereader:
			row = row.strip()
			row_list = row.split(',')
			print(row_list)
			filewriter.write(','.join(map(str,row_list))+'\n')
			

# 실행하기
# python .\01_csv파일입출력.py "입력파일경로" "출력파일경로"
# python .\01_csv파일입출력.py "E:\ALOHA\JOEUN\GIT\TJE_PYTHON_DATA\Day09\CSV\input\sample.csv" "E:\ALOHA\JOEUN\GIT\TJE_PYTHON_DATA\Day09\CSV\output\sample.csv"