-- Active: 1712576329756@@127.0.0.1@3306@joeun
CREATE TABLE address_book (
    no      INT PRIMARY KEY AUTO_INCREMENT,
    name    VARCHAR(100) NOT NULL,
    tel     VARCHAR(100) NOT NULL,
    address VARCHAR(100) NOT NULL,
    reg_date TIMESTAMP DEFAULT now(),
    upd_date TIMESTAMP DEFAULT now()
) COMMENT='주소록';