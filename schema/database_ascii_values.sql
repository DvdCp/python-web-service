USE db;

CREATE TABLE evenvalues (
    id int not null AUTO_INCREMENT,
    decimalEvenValue int not null,
    PRIMARY KEY (id)
);

CREATE TABLE oddvalues (
    id int not null AUTO_INCREMENT,
    decimalOddValue int not null,
    PRIMARY KEY (id)
);

CREATE TABLE octvalues (
    id int not null AUTO_INCREMENT,
    octValue varchar(40) not null,
    PRIMARY KEY (id)
);

CREATE TABLE hexvalues (
    id int not null AUTO_INCREMENT,
    hexValue varchar(40) not null,
    PRIMARY KEY (id)
);

CREATE TABLE binvalues (
    id int not null AUTO_INCREMENT,
    binValue varchar(40) not null,
    PRIMARY KEY (id)
);

CREATE TABLE alphastrings (
    id int not null AUTO_INCREMENT,
    alphaValue varchar(40) not null,
    evenValueId int,
    oddValueId int,
    octValueId int,
    hexValueId int,
    binValueId int,
    PRIMARY KEY (id),
    FOREIGN KEY (evenValueId) REFERENCES evenvalues(id),
    FOREIGN KEY (oddValueId) REFERENCES oddvalues(id),
    FOREIGN KEY (octValueId) REFERENCES octvalues(id),
    FOREIGN KEY (hexValueId) REFERENCES hexvalues(id),
    FOREIGN KEY (binValueId) REFERENCES binvalues(id)
);
