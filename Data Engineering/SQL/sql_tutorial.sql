-- SELECT in SQL
SELECT first_name, last_name FROM customers;
SELECT * FROM customers;                    -- Select the entire table
SELECT DISTINCT country FROM customers;     -- Select the unique values
-- ================================================================================================

-- WHERE in SQL
SELECT * FROM orders WHERE total_amount > 100;
SELECT * FROM products WHERE category != 'Cars';
SELECT * FROM orders WHERE total_amount BETWEEN 200 AND 300;
SELECT * FROM products WHERE product_name LIKE 's%';       -- Using a wildcard chars
SELECT * FROM customers WHERE country IN ('Canada', 'Egypt');
-- ================================================================================================

-- ORDER BY in SQL (can order numerical and alphabitical)
SELECT * FROM customers ORDER BY first_name, age;
SELECT * FROM customers ORDER BY first_name DESC;           -- ordered descending
SELECT * FROM customers ORDER BY age ASC, first_name DESC;  -- Using ascending and descending
-- ================================================================================================

-- AND, OR, NOT

-- AND
SELECT * FROM insurance WHERE age<= 25 AND Smoker='no';
SELECT * FROM insurance WHERE age >= 30 AND (bmi > 25 OR region LIKE 'S%');

-- OR
SELECT * FROM insurance WHERE bmi > 30 OR age > 30;
SELECT * FROM insurance WHERE sex = 'male' and Smoker = 'no' OR charges > 3000;

-- NOT
SELECT * FROM insurance WHERE NOT smoker = 'no';
SELECT * FROM insurance WHERE age NOT BETWEEN 25 AND 40; -- NOT BETWEEN
SELECT * FROM insurance WHERE region NOT IN ('southeast', 'northeast'); -- NOT IN
-- ================================================================================================

-- NULL VALUES in SQL
SELECT id FROM customers WHERE age IS NULL;
SELECT id FROM customers WHERE age IS NOT NULL;
-- ================================================================================================

-- INSERT INTO in SQL

-- Insert into speceifed columns
INSERT INTO customers (id, first_name, last_name, county, age)
VALUES (35, 'Ahmed', 'Hazem', 'Egypt', 18);

-- Insert into all columns (must remember the arrangement of columns)
INSERT INTO customers
VALUES (35, 'Ahmed', 'Hazem', 'Egypt', 18);

-- Insert multiple rows
INSERT INTO customers (id, first_name, last_name, county, age)
VALUES (35, 'Ahmed', 'Hazem', 'Egypt', 18),
       (36, 'Mohamed', 'Hamza', 'Canada', 20),
       (37, 'Yousef', 'hady', 'USA', 'northwest', 30);
-- ================================================================================================

-- UPDATE in SQL
UPDATE customers
SET age = 18 WHERE id = 3;
-- ================================================================================================
-- DELETE in SQL
DELETE FROM customers WHERE age < 18;

DELETE FROM customers; -- Delete all the elements in the table
DROP TABLE customers;  -- Delete the entire table
-- ================================================================================================

-- SELECT TOP & LIMIT in SQL
SELECT * FROM orders LIMIT 5;           -- Read first 5 rows
SELECT * FROM orders LIMIT 10 OFFSET 5; -- Skip first 5 rows and read 10 rows
-- ================================================================================================

-- Agregation functions in SQL

-- MIN(), MAX()
SELECT MIN(total_amount) FROM orders;
SELECT MAX(total_amount) FROM orders;

-- COUNT()
SELECT COUNT(*) FROM orders;            -- Get number of rows
SELECT COUNT(total_amount) FROM orders; -- Get number of total_amount column(null values will not be counted)

-- SUM()
SELECT SUM(total_amount) FROM orders;
SELECT Sum(total_amount / 10) FROM orders; -- Sum with expression

-- AVG()
SELECT AVG(total_amount) FROM orders;

-- LENGTH()
SELECT LENGTH(country) FROM customers;
-- ================================================================================================
-- LIKE & WILDCARDS
SELECT * FROM customers WHERE first_name LIKE 'y%';     -- Select all rows which name column starts with 'y'
SELECT * FROM customers WHERE first_name LIKE '%o';     -- Select all rows which name column ends with 'o'
SELECT * FROM customers WHERE first_name LIKE '%e%';    -- Select all rows which name column contians letter 'e'
SELECT * FROM customers WHERE first_name LIKE 'f%e';    -- Select all rows which name column starts with f and ends with e

SELECT * FROM customers WHERE first_name LIKE 'm_l_';   -- Select all rows which name column has m - char - l - char

-- combine wildcards
SELECT * FROM customers WHERE first_name LIKE 's__%';   -- Select all rows which name column starts with 's' at least three chars length
SELECT * FROM customers WHERE first_name LIKE '__r%';   -- Select all rows which name columns has letter 'r' in third position
-- ================================================================================================

-- Alias in SQL
SELECT COUNT(order_id) AS num_orders
FROM orders

-- concat columns
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM customers;

-- Alias from tables
SELECT * FROM customers AS "customer_table";

-- ** Alias from tables useful if you handled with subquery
-- ================================================================================================

-- JOINS in SQL

-- INNER JOIN
SELECT
    c.id, c.first_name,
    c.age, c.country,
    o.total_amount, o.order_date
FROM customers c
INNER JOIN orders o ON o.customer_id = c.customer_id; 

-- ** Another type of JOINS: LEFT, RIGHT, FULL OUTER

-- SELF JOIN
SELECT
    A.customer_name AS customer1,
    B.customer_name AS customer2,
    A.city
FROM customers A, customers B
WHERE A.customer_id < B.customer_id
AND A.city = B.city
ORDER BY A.city;

-- ANTI LEFT, ANTI RIGHT
SELECT
    c.id, c.first_name,
    c.age, c.country,
    o.total_amount, o.order_date
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.customer_id IS NULL; 
-- ================================================================================================

-- UNION
SELECT customer_id FROM customers1
UNION
SELECT customer_id FROM customers2;

-- UNION ALL (allow duplicates)
SELECT customer_id FROM customers1
UNION ALL
SELECT customer_id FROM customers2;

-- INTERSECT
SELECT customer_id FROM customers1
INTERSECT
SELECT customer_id FROM customers2;

-- EXCEPT (like difference)
SELECT customer_id FROM customers1
EXCEPT
SELECT customer_id FROM customers2;
-- ================================================================================================

-- GROUP BY in SQL
SELECT
    customer_id,
    SUM(total_amount)
FROM orders
GROUP BY cutomer_id;
-- ================================================================================================

-- HAVING & GROUP BY 
SELECT
    customer_id,
    SUM(total_amount)
FROM orders
GROUP BY cutomer_id;
-- ================================================================================================

-- EXISTS (checks whether at least one row is returned by a subquery)
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM customers c
WHERE EXISTS (
    SELECT *
    FROM orders o
    WHERE o.customer_id = c.customer_id
);

-- NOT EXISTS
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM customers c
WHERE NOT EXISTS (
    SELECT *
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
-- ================================================================================================

-- ANY
SELECT product_name
FROM products
WHERE product_id > ANY
  (SELECT product_id
   FROM order_items
   WHERE Quantity = 10);

-- ALL
SELECT product_name
FROM products
WHERE product_id > ALL
  (SELECT product_id
   FROM order_items
   WHERE Quantity = 10);
-- ================================================================================================

-- CASE in SQL
SELECT order_id, total_amount,
CASE
    WHEN total_amount > 80 THEN 'number of orders is big'
    WHEN total_amount = 80 THEN 'number of orders is 80'
    WHEN total_amount < 80 THEN 'number of orders is small'
END AS order_details
FROM orders;
-- ================================================================================================

-- NULL FUNCTION in SQL
SELECT
    customer_id,
    COALESCE("country", "unknown")
FROM customers;
-- ===============================================================================================

-- VIEW (virtual tables that represent the result of a stored SELECT query)
CREATE VIEW view_table AS
SELECT
    c.first_name,
    c.last_name,
    SUM(o.total_amount) AS total_order_amount
FROM customers c
INNER JOIN orders o USING (customer_id)
GROUP BY c.first_name, c.last_name;

SELECT * FROM view_table;
-- ===============================================================================================

-- Modifying a VIEW
CREATE OR REPLACE VIEW AS 
SELECT
    e.fname,
    e.lname,
    d.pname,
    e.hours
FROM employees e
INNER JOIN department d ON e.department_id = d.department_id
WHERE e.department_id = 5;
-- ===============================================================================================

-- CREATING Views with Check Option
CREATE VIEW vw_high_status_suppliers AS
SELECT *
FROM suppliers
WHERE status > 15
WITH CHECK OPTION;
-- ===============================================================================================

-- Create View with check option
CREATE VIEW vw_high_status_suppliers AS
SELECT *
FROM suppliers
WHERE status > 15
WITH CHECK OPTION;
-- ===============================================================================================

-- STORED PROCEDURE (pre-compiled blocks of SQL code that are stored in the database and can be called by name (like a function))
--DELIMITER //
CREATE PROCEDURE GetCustomerOrders(IN cust_id INT)
BEGIN
    SELECT 
        o.order_id,
        o.order_date,
        p.product_name,
        oi.quantity,
        oi.unit_price
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    JOIN products p ON p.product_id = oi.product_id
    WHERE o.customer_id = cust_id
      AND o.status = 'completed';
END //
DELIMITER;

-- Application only needs:
CALL GetCustomerOrders(1453);
-- No direct access to tables needed
-- ===============================================================================================

-- CREATE DATABASE
CREATE DATABASE Sales;

-- DROP DATABASE
DROP DATABASE Sales;

-- CREATE TABLES (Constraints: primary_key, not null, unqiue, check, foreign key, auto_increment, default, UNSIGNED)
--               (data types: INT, VARCHAR, DATE, DECIMAL, BIGHT)
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY SIGNED AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    city VARCHAR(50) DEFAULT "Unknown",
    country VARCHAR(50) DEFAULT "Unknown"
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL CHECK(total_amount > 0 AND total_amount < 100000),
    zip_code VARCHAR(100) UNIQUE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- DROP TABLE
DROP TABLE orders;
-- ===============================================================================================

-- ALTER TABLE
ALTER TABLE cafe
ADD Discount INTEGER;          -- ADD Column

ALTER TABLE cafe
DROP Discount;                 -- DROP Column

ALTER TABLE cafe
RENAME "Price Per Unit" TO "price"; -- RENAME Columns

ALTER TALBE cafe
MODIFY COLUMN 'Quantity' INTEGER; -- Modify data type
-- ===============================================================================================

-- String Functions

LENGTH(str)                     -- Returns the length in bytes (useful for multibyte encodings).

LEFT(str, len)                  --  Extracts the leftmost len characters.
RIGHT(str, len)                 -- Extracts the rightmost len characters.

LOWER(str)                      -- Converts all characters to lowercase.
UPPER(str)                      -- Converts all characters to uppercase.

CONCAT(str1, str2, …)           -- Joins multiple strings into one.
CONCAT_WS(sep, str1, str2, …)   -- Like CONCAT, but adds a separator sep between strings.

SUBSTRING(str, pos, len)        -- Extracts a substring starting at pos for len characters.
TRIM(str)                       -- Removes leading and trailing spaces.

REPLACE(str, from_str, to_str)  -- Replaces all occurrences of from_str with to_str.
REPEAT(str, count)              -- Repeats str count times.
REVERSE(str)                    -- Reverses the string.
-- ===============================================================================================

-- Numeric Functions
ABS(x), ROUND(x, d), TRUNCATE(x, d)

ACOS(x), ASIN(x), ATAN(x)

CEIL(x), FLOOR(x)

SIN(x), COS(x), TAN(x)

DEGREES(x), RADIANS(x)

EXP(x), LN(x)

LOG(x), LOG10(x), LOG2(x)

PI(), POW(x, y)
-- ===============================================================================================

-- Data Functions
NOW()                           --Returns current date and time (YYYY-MM-DD HH:MM:SS)
CURRENT_DATE()	                --Returns current date only (YYYY-MM-DD)
CURRENT_TIME()	                --Returns current time only (HH:MM:SS)

DATE() -- Selects Date from datatime
TIME() -- Select Time from datetime

ADDDATE(date, INTERVAL n unit)	-- Adds interval to a date (e.g., ADDDATE('2025-09-05', INTERVAL 10 DAY))
ADDTIME(datetime, time)	        -- Adds time to a datetime (e.g., ADDTIME('2025-09-05 10:00:00', '02:30:00'))
DATE_SUB(date, INTERVAL n unit)	-- Subtracts interval from a date
DATEDIFF(unit, date1, date2)	-- Returns number of days between two dates

DATE(datetime)	                --Extracts date part only
DAY(date) / DAYOFMONTH(date)    -- Day of the month (1–31)
DAYNAME(date)	                -- Name of the weekday (e.g., 'Friday')
DAYOFWEEK(date)	                -- Weekday index (1 = Sunday, 7 = Saturday)
DAYOFYEAR(date)	                -- Day of the year (1–366)
MONTH(date)	                    -- Month number (1–12)
MONTHNAME(date)	                -- Month name (e.g., 'September')
YEAR(date)	                    -- Year component
QUARTER(date)                   -- Quarter of the year (1–4)
HOUR(time)                      -- Hour component
MINUTE(time)                    -- Minute component
SECOND(time)                    -- Second component
EXTRACT(unit FROM date)	        -- General-purpose extractor (e.g., EXTRACT(YEAR FROM '2025-09-05'))

DATE_FORMAT(date, format)       -- Formats date using custom string (e.g., '%W, %M %d, %Y')
TIME_FORMAT(time, format)       --Formats time (e.g., TIME_FORMAT('14:05:00', '%h:%i %p') → '02:05 PM')
-- ===============================================================================================

-- WINDOW FUNCTIONS in SQL

-- Using aggregate window functions
SELECT
    id,
    Item,
    SUM(Quantity) OVER (PARTITION BY location) AS total_quantity
FROM cafe;

-- Using Ranking window functions
SELECT Student, Scores, RANK() OVER (ORDER BY Scores DESC) AS "rank" FROM Students;       -- rank allows gaps
SELECT Student, Scores, DENSE_RANK() OVER (ORDER BY Scores DESC) AS "rank" FROM Students; -- rank does not allow gaps
SELECT Student, Scores, ROW_NUMBER() OVER (ORDER BY Scores DESC) AS "rank" FROM Students; -- count the rows
SELECT Student, Scores, NTILE(4) OVER (ORDER BY Scores DESC) AS "rank" FROM Students;     -- same as quartiles
-- ===============================================================================================

-- USING VALUE window functions

SELECT item, price, sale_date, LAG(price) OVER (PARTITION BY sale_date ORDER BY id) AS previous_price
FROM cafe_sales; -- gets the value from the previous row

SELECT item, price, sale_date, LEAD(price) OVER (PARTITION BY sale_date ORDER BY id) as next_price
FROM cafe_sales; -- gets the value from the next row

SELECT item, price, sale_date, FIRST_VALUE(price) OVER (PARTITION BY sale_date ORDER BY price DESC) as highest_price
FROM cafe_sales; -- gets the first value in the window


SELECT item, price, sale_date, LAST_VALUE(price) OVER (PARTITION BY sale_date ORDER BY price) as highest_price
FROM cafe_sales; -- gets the last value in the window
-- ===============================================================================================

-- CTE (it the same as subqueries but it easier to read)

WITH sales_summary AS (
    SELECT item , SUM(price) as Total
    FROM cafe_sales
    GROUP BY item
)
SELECT item, Total
FROM sales_summary
WHERE total > 20;

-- another example
WITH avg_sales AS (
    SELECT AVG(price) as avg_price
    FROM cafe_sales
),
high_sales AS (
    SELECT item, price
    FROM cafe_sales
    WHERE price > (SELECT avg_price FROM avg_sales)
)
SELECT item, price
FROM high_sales
ORDER BY price DESC
-- ===============================================================================================

-- ROLLUP AND CUBE in SQL

-- ROLLUP: like a GROUP BY but with grand subtotals
-- NULL means total
SELECT 
    year, 
    month, 
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY ROLLUP(year, month);

-- CUBE: generates all possible combinations of grouped columns
SELECT 
    year, 
    month, 
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY CUBE(year, month);
-- ===============================================================================================

-- CREATE INDEX (useful for performance on searching)
CREATE INDEX idx_customer_country
ON customers(country);
-- ===============================================================================================

-- EXPLAIN AND ANALYZE
-- Use EXPLAIN when you're designing or debugging a query and want a quick look.
-- Use EXPLAIN ANALYZE when you're optimizing performance and need real metrics.

-- EXPLAIN
EXPLAIN SELECT * FROM customers;
EXPLAIN ANALYZE SELECT * FROM customers;
-- ===============================================================================================

-- PARTITIONING 

-- 1. Range partitioning
CREATE TABLE sales (
    id INT AUTO_INCREMENT,
    sale_date DATE NOT NULL,
    amount DECIMAL(10,2),
    PRIMARY KEY (id, sale_date)
)
PARTITION BY RANGE (YEAR(sale_date)) (
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025),
    PARTITION p2025 VALUES LESS THAN (2026),
    PARTITION p_future VALUES LESS THAN MAXVALUE 
);
---------------------------------
-- 2. List partitioning
CREATE TABLE customers (
    id INT AUTO_INCREMENT,
    name VARCHAR(100),
    region ENUM('North', 'South', 'East', 'West', 'Cairo', 'Alex') NOT NULL,
    PRIMARY KEY (id, region)
)
PARTITION BY LIST COLUMNS(region) (
    PARTITION p_north VALUES IN ('North'),
    PARTITION p_south VALUES IN ('South'),
    PARTITION p_east  VALUES IN ('East'),
    PARTITION p_west  VALUES IN ('West'),
    PARTITION p_cairo VALUES IN ('Cairo'),
    PARTITION p_alex  VALUES IN ('Alex')
);