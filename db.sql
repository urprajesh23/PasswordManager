CREATE DATABASE PwdDB;

USE PwdDB;

CREATE TABLE Passwords (
    id INT PRIMARY KEY AUTO_INCREMENT,
    platform VARCHAR(100),
    username VARCHAR(100),
    password TEXT
);
