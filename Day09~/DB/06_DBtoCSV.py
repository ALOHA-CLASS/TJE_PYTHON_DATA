# pip install pymysql
import pymysql
import csv
import os

# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 디렉터리 경로 - 이 안의 input, output 폴더에서 입출력한다.
path = os.path.dirname(program_path)

output_file = path + '/output/' + input('출력 파일 : ')


# MySQL 서버에 접속
conn = pymysql.connect(
    host='127.0.0.1',
    user='joeun',
    password='123456',
    database='joeun',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        sql = "SELECT * FROM sample"
        cursor.execute(sql)             # DB에 쿼리 요청

        sampleList = cursor.fetchall()    # 결과 

        with open(output_file, 'w', newline='', encoding='UTF-8') as csv_out_file:
            filewriter = csv.writer(csv_out_file, delimiter=',')

            header = ('학번','이름','주소','번화번호')
            filewriter.writerow( header )
                
            for sample in sampleList:
                std_id = sample.get('학번')
                name = sample.get('이름')
                address = sample.get('주소')
                tel = sample.get('전화번호')
                row = ( std_id, name, address, tel )
                filewriter.writerow( row )

except pymysql.MySQLError as e:
    print('MySQL 에러 : ', e)
finally:
    conn.close()


