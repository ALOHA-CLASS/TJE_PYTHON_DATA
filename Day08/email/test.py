'''
    파이썬으로 이메일 전송하기
    
    * 준비하기
    - 라이브러리 설치
    - 이메일 로그인해서 IMAP, POP3 설정하기
    
    
    1. 라이브러리 설치
    * smtplib   : 이메일을 전송하기 위한 모듈
    * email     : 이메일 메시지, 첨부파일 등 관리하기 위한 모듈
    - 기본 라이브러리라서, 별도 설치 필요X
    
    
    2. 이메일 SMTP 설정하기
    - (네이버 메일)
      > 환경 설정 > IMAP/POP3 설정 
        > SMTP/POP3 사용함 
        > 네이버 메일이 원본 저장
      
      
    3. 네이버 로그인 2단계 인증 > 해제
    
    4. stmp_port : 587
    
'''

import smtplib
from email.mime.text import MIMEText # 이메일 텍스트 형식 모듈

print('네이버 이메일 보내기')
print('로그인')


smtp_info = dict({"smtp_server" : "smtp.naver.com",         # SMTP 서버 주소
                  "smtp_user_id" : input('네이버 메일주소 : '),
                  "smtp_user_pw" : input('비밀번호 : '),
                  "smtp_port" : 587})                       # SMTP 서버 포트

def send_email(smtp_info, msg):
    with smtplib.SMTP(smtp_info["smtp_server"], smtp_info["smtp_port"]) as server:
        # TLS 보안 연결
        server.starttls()
        # 로그인
        server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])
        
        
        # 로그인 된 서버에 이메일 전송
        response = server.sendmail(msg['from'], msg['to'], msg.as_string()) # 메시지를 보낼때는 .as_string() 메소드를 사용해서 문자열로 바꿔줍니다.
        
        # 이메일을 성공적으로 보내면 결과는 {}
        if not response:
            print('이메일을 성공적으로 보냈습니다.')
        else:
            print('응답결과: ')
            print(response)
            
# 이메일 내용

receiver = input('받는 사람 : ')          # 받는 사람
sender = smtp_info['smtp_user_id']      # 보내는 사람
title = input('제목 : ')
content = input('내용 : ')


# 메일 객체 생성
msg = MIMEText(_text = content, _charset = "utf-8")
msg['Subject'] = title
msg['From'] = sender
msg['To'] = receiver

# 이메일 전송
send_email(smtp_info, msg)