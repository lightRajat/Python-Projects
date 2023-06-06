DROP DATABASE IF EXISTS rajatbms;
CREATE DATABASE rajatbms;
USE rajatbms;

CREATE TABLE login_credentials (
	serial_no INT UNSIGNED AUTO_INCREMENT,
    post VARCHAR(20) NOT NULL,
    id VARCHAR(20) NOT NULL,
    pass VARCHAR(20) NOT NULL,
    PRIMARY KEY (serial_no)
);

INSERT INTO login_credentials (post, id, pass)
VALUES
	('Clerk', 'stud_clerk_op', 'clerk@123'),
    ('Manager', 'manager_boss', 'hardboss075'),
    ('Personal Banker', 'frustrated_banker', 'xneedpromotionx');

CREATE TABLE user_accounts (
	record_id INT UNSIGNED AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    dob DATE NOT NULL,
    mobile BIGINT NOT NULL,
    mail VARCHAR(30) NOT NULL,
    address VARCHAR(100) NOT NULL,
    idtype VARCHAR(20) NOT NULL,
    idnumber BIGINT NOT NULL,
    nominee VARCHAR(30) NOT NULL,
    nominee_no BIGINT NOT NULL,
    account_number BIGINT NOT NULL UNIQUE,
    balance FLOAT NOT NULL DEFAULT (0.00),
    PRIMARY KEY (record_id)
)