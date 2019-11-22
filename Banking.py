CREATE DATABASE Banking

USE Banking;

CREATE TABLE deposit (
	depositID int auto_increment NOT NULL UNIQUE,
	depositAmount float NOT NULL,
	PRIMARY KEY(depositID)
);


CREATE TABLE withdraw (
	withdrawID int auto_increment NOT NULL UNIQUE,
	withdrawAmount int NOT NULL,
	PRIMARY KEY(withdrawID)
);

CREATE TABLE accountDetail (
	aD_ID int auto_increment NOT NULL UNIQUE,
	withdrawID int NOT NULL UNIQUE,
	depositID int NOT NULL UNIQUE,
	firstName varchar(50) NOT NULL,
	lastName varchar(50) NOT NULL,
	PRIMARY KEY(aD_ID),
	FOREIGN KEY (withdrawID) REFERENCES withdraw(withdrawID),
	FOREIGN KEY (depositID) REFERENCES deposit(depositID)
);

INSERT INTO deposit VALUE ("1", "34.50");
INSERT INTO withdraw VALUE ("1", "5");
INSERT INTO accountDetail VALUE ("1", "1", "1", "Simon", "Chen");
