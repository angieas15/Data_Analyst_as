SELECT * FROM products.bakery_products_new;

RENAME TABLE products.bakery_products_new TO products.bakery_products_new_pucon;

USE products;
CREATE TABLE bakery_products_new(
    ID int not null auto_increment,
    DATE text,
    Category_name text,
    Product_name text,
    Quantity int default null,
    Unit_price int default null,
    Revenue int default null,
    Promotion int default null,
    primary key (ID)
) ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SELECT DISTINCT Category_name FROM bakery_products_new;


INSERT INTO bakery_products_new (ID, Date, Category_name, Product_name, Quantity, Unit_price, Revenue, Promotion)
SELECT ID, Date, Category_name, Product_name, Quantity, Unit_price, Revenue, Promotion FROM bakery_products_new_pucon;

SELECT * FROM bakery_products_new;
DROP TABLE bakery_products_new_pucon;

-- change values 
ALTER TABLE bakery_products_new
MODIFY COLUMN Category_name varchar (200);

ALTER TABLE bakery_products_new
MODIFY COLUMN Product_name varchar (200);

-- INDEX
ALTER TABLE bakery_products_new 
ADD INDEX (Category_name);

-- SEARCH DATA
SELECT * FROM bakery_products_new LIMIT 1;
SELECT * FROM bakery_products_new WHERE Quantity > 8;
SELECT * FROM bakery_products_new WHERE Quantity >= 9;
SELECT * FROM bakery_products_new WHERE Category_name = 'Desserts' and Promotion =1;
SELECT * FROM bakery_products_new WHERE Category_name = 'Desserts' or Product_name = 'Cheesecake';
SELECT * FROM bakery_products_new WHERE Quantity != 7 ;
SELECT * FROM bakery_products_new WHERE Quantity between 1 and 3;

SELECT * FROM bakery_products_new WHERE Product_name like '%burguer%';
SELECT * FROM bakery_products_new WHERE Product_name like '%juce';
SELECT * FROM bakery_products_new WHERE Product_name like 'tea%';

SELECT * FROM bakery_products_new ORDER BY Quantity ASC;
SELECT * FROM bakery_products_new ORDER BY Quantity DESC;

SELECT MAX(Promotion) as mayor FROM  bakery_products_new;
SELECT MIN(Promotion) as menor_promotion FROM  bakery_products_new;

SELECT ID, Category_name FROM  bakery_products_new;

