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
name = input('이름 : ')
tel = input('전화번호 : ')

try:
    # 커서 생성
    with conn.cursor() as cursor:
        # 데이터 수정 쿼리 
        sql = " UPDATE 학생 "\
            + " SET std_id = %s "\
            + "    ,name = %s "\
            + "    ,tel = %s "\
            + "    ,upd_date = now() "\
            + " WHERE std_id = %s "
            
            # + " VALUES ('B2401', '홍길동', '010-1234-1234') "
        
        # result = cursor.execute(sql)                              # 쿼리 실행 요청
        result = cursor.execute(sql, (std_id, name, tel, std_id))   # 파라미터 지정
        print('{}행의 데이터 수정 완료'.format(result))

    # 변경사항 적용
    conn.commit()

except pymysql.MySQLError as e:
    print("데이터 수정 중 에러 발생 : ", e)
finally:
    conn.close()
