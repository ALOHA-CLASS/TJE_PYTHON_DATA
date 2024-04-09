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

std_id = input('학번 : ')

try:
    # 커서 생성
    with conn.cursor() as cursor:
        # 데이터 삭제 쿼리 
        sql = " DELETE FROM 학생 "\
            + " WHERE std_id = %s "
        
        result = cursor.execute(sql, (std_id))   # 파라미터 지정
        print('{}행의 데이터 삭제 완료'.format(result))

    # 변경사항 적용
    conn.commit()

except pymysql.MySQLError as e:
    print("데이터 삭제 중 에러 발생 : ", e)
finally:
    conn.close()
