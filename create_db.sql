CREATE TABLE Admin_Setting (
	company_name	VARCHAR(50)	NOT NULL,
	password_length INT		NOT NULL,
	require_caps	INT		NOT NULL,
	require_lowercase	INT	NOT NULL,
	require_number	INT		NOT NULL,
	require_special	INT		NOT NULL,
	expiration_time	INT		NOT NULL,
	PRIMARY KEY (company_name)
);

CREATE TABLE Users (
    ID				INT				NOT NULL,
	username		VARCHAR(50)		NOT NULL,
	curr_password	VARCHAR(50)		NOT NULL,
	is_admin		INT				NOT NULL,
	email			VARCHAR(50)		NOT NULL,
	company_name	VARCHAR(50)		NOT NULL,
	phone_number	CHAR(12),
	password_last_set	DATE		NOT NULL,
	PRIMARY KEY (ID),
	FOREIGN KEY (company_name) REFERENCES Admin_Setting(company_name)
);

CREATE TABLE Old_Password (
    ID				INT			NOT NULL,
	userID			INT		NOT NULL,
	hashedPassword VARCHAR(50)	NOT NULL,
	PRIMARY KEY (ID),
	FOREIGN KEY (userID) REFERENCES Users(ID)
);

CREATE TABLE Common_Passwords (
    ID				INT			NOT NULL,
	hashedPassword	VARCHAR(50)	NOT NULL,
	PRIMARY KEY (ID)
);