import csv
import os
import pymysql

# MySQL 서버에 접속
conn = pymysql.connect(
    host='127.0.0.1',
    user='joeun',
    password='123456',
    database='joeun',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)

# 입력 : CSV
input_file = path + '/input/' + input('입력 파일 : ')
# 출력 : DB

with open(input_file, 'r', newline='', encoding='UTF-8') as csv_in_file:
	
	# csv_in_file 파일을 ',' 구분자 읽기모드로 CSV 파일 객체 생성
	filereader = csv.reader(csv_in_file, delimiter=',')

	try:
		# 커서 생성
		with conn.cursor() as cursor:
			# 데이터 등록 쿼리 
			sql = " INSERT INTO sample (학번, 이름, 주소, 전화번호) "\
				+ " VALUES (%s, %s, %s, %s) "
			
			# 읽기모드의 파일 객체를 한 줄씩 읽어서 반복
			for index, row_list in enumerate( filereader ) :
				if index == 0:
					continue
				
				result = cursor.execute(sql, row_list )   # 파라미터 지정
				print('{}행의 데이터 등록 완료'.format(result))

		# 변경사항 적용
		conn.commit()

	except pymysql.MySQLError as e:
		print("데이터 등록 중 에러 발생 : ", e)
	finally:
		conn.close()

	
  

