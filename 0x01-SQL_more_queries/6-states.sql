-- creates database and table


CREATE DATABASE if not EXISTS hbtn_0d_usa;
CREATE TABLE if not EXISTS hbtn_0d_usa.states (id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
