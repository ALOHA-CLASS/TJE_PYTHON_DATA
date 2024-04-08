# pip install pymysql
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

# try:
#     if conn.ping(reconnect=True):
#         print('접속 성공!')
#     else:
#         print('접속 실패!')
# except pymysql.MySQLError as e:
#     print('MySQL 에러 : ', e)
# finally:
#     conn.close()


try:
    with conn.cursor() as cursor:
        sql = "SELECT * FROM 학생"
        cursor.execute(sql)             # DB에 쿼리 요청

        students = cursor.fetchall()    # 결과 

        for student in students:
            print( student )
except pymysql.MySQLError as e:
    print('MySQL 에러 : ', e)
finally:
    conn.close()
