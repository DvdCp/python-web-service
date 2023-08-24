USE db;

CREATE TABLE evenasciivalues (
    id int not null AUTO_INCREMENT,
    literal_string varchar(40) not null,
    ascii_decimal_value int not null,
    PRIMARY KEY (id)
);

CREATE TABLE oddasciivalues (
    id int not null AUTO_INCREMENT,
    literal_string varchar(40) not null,
    ascii_decimal_value int not null,
    PRIMARY KEY (id)
);