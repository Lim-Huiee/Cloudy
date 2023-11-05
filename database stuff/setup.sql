DROP DATABASE IF EXISTS gitwellsoon;

CREATE DATABASE gitwellsoon;
USE gitwellsoon;

DROP TABLE IF EXISTS `accounts`;
CREATE TABLE `accounts` (
    `username` VARCHAR(100) NOT NULL,
    `password` VARCHAR(100) NOT NULL,
    `email` VARCHAR(100) NOT NULL,

    PRIMARY KEY (`email`)
);

DROP TABLE IF EXISTS `products`;
CREATE TABLE `products` (
    `pid` INT AUTO_INCREMENT NOT NULL,
    `pcat` VARCHAR(100) NOT NULL,
    `pname` VARCHAR(100) NOT NULL,
    `pdesc` VARCHAR(100) NOT NULL,
    `pprice` VARCHAR(100) NOT NULL,
    `img_src` VARCHAR(100) NOT NULL,
    `stock` VARCHAR(100) NOT NULL,
    `prod_date` DATE,
    `expiry_date` DATE,

    PRIMARY KEY (`pid`)
);

DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
    `oid` INT AUTO_INCREMENT NOT NULL,
    `email` VARCHAR(100) NOT NULL,
    `pid` INT NOT NULL,
    `quantity` INT NOT NULL,
    `status` VARCHAR(100) NOT NULL,
    
    constraint orders_fk1 foreign key (email) references accounts(`email`) ON DELETE CASCADE ON UPDATE CASCADE,    
    constraint orders_fk2 foreign key (pid) references products(`pid`) ON DELETE CASCADE ON UPDATE CASCADE,    

    PRIMARY KEY (`oid`)
);

LOAD DATA LOCAL INFILE 'C:/wamp64/tmp/gitwellsoon_login.csv'  -- replace with the directory where your csv is located
INTO TABLE accounts 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(username, password, email);

-- import gitwellsoon products table
LOAD DATA LOCAL INFILE 'C:/wamp64/tmp/gitwellsoon_products.csv'  -- replace with the directory where your csv is located
INTO TABLE products 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(pid, pcat, pname, pdesc, pprice, img_src, stock, prod_date, expiry_date);

-- import gitwellsoon orders table
LOAD DATA LOCAL INFILE 'C:/wamp64/tmp/gitwellsoon_orders.csv'  -- replace with the directory where your csv is located
INTO TABLE orders 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(oid, email, pid, quantity, status);
