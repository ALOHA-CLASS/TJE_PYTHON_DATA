-- Active: 1712576329756@@127.0.0.1@3306@joeun
CREATE TABLE sample (
    -- 컬럼명 데이터타입 NULL여부 기본값 제약조건
    학번 INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    이름 VARCHAR(45) NOT NULL,
    주소 VARCHAR(100) NOT NULL,
    전화번호 VARCHAR(20) NOT NULL
) COMMENT = '샘플 학생 테이블';