/* ================================================================================================
   PART 1 - QUERYING BASICS
   ================================================================================================ */

-- ------------------------------------------------------------------------------------------------
-- 1.1  SELECT / DISTINCT
-- ------------------------------------------------------------------------------------------------
SELECT first_name, last_name FROM customers;    -- specific columns
SELECT * FROM customers;                        -- entire table
SELECT DISTINCT country FROM customers;         -- unique values only


-- ------------------------------------------------------------------------------------------------
-- 1.2  WHERE  (filters ROWS before grouping)
-- ------------------------------------------------------------------------------------------------
SELECT * FROM orders   WHERE total_amount > 100;
SELECT * FROM products WHERE category != 'Cars';                    -- also: <>
SELECT * FROM orders   WHERE total_amount BETWEEN 200 AND 300;      -- inclusive on both ends
SELECT * FROM customers WHERE country IN ('Canada', 'Egypt');       -- match any in list


-- ------------------------------------------------------------------------------------------------
-- 1.3  AND / OR / NOT
--      Precedence: NOT > AND > OR   (use parentheses to be explicit)
-- ------------------------------------------------------------------------------------------------
-- AND: both conditions must be true
SELECT * FROM insurance WHERE age <= 25 AND smoker = 'no';
SELECT * FROM insurance WHERE age >= 30 AND (bmi > 25 OR region LIKE 'S%');

-- OR: at least one condition must be true
SELECT * FROM insurance WHERE bmi > 30 OR age > 30;
SELECT * FROM insurance WHERE (sex = 'male' AND smoker = 'no') OR charges > 3000;   -- AND is evaluated first

-- NOT: negates a condition
SELECT * FROM insurance WHERE NOT smoker = 'no';
SELECT * FROM insurance WHERE age NOT BETWEEN 25 AND 40;
SELECT * FROM insurance WHERE region NOT IN ('southeast', 'northeast');


-- ------------------------------------------------------------------------------------------------
-- 1.4  LIKE & WILDCARDS
--      %  = any number of characters (including none)
--      _  = exactly one character
-- ------------------------------------------------------------------------------------------------
SELECT * FROM customers WHERE first_name LIKE 'y%';     -- starts with 'y'
SELECT * FROM customers WHERE first_name LIKE '%o';     -- ends with 'o'
SELECT * FROM customers WHERE first_name LIKE '%e%';    -- contains 'e'
SELECT * FROM customers WHERE first_name LIKE 'f%e';    -- starts with 'f' and ends with 'e'
SELECT * FROM customers WHERE first_name LIKE 'm_l_';   -- m, any char, l, any char (4 letters)

-- Combining wildcards
SELECT * FROM customers WHERE first_name LIKE 's__%';   -- starts with 's', at least 3 characters long
SELECT * FROM customers WHERE first_name LIKE '__r%';   -- 'r' is the 3rd character


-- ------------------------------------------------------------------------------------------------
-- 1.5  NULL VALUES  (NULL is "unknown": use IS NULL, never = NULL)
-- ------------------------------------------------------------------------------------------------
SELECT customer_id FROM customers WHERE age IS NULL;
SELECT customer_id FROM customers WHERE age IS NOT NULL;


-- ------------------------------------------------------------------------------------------------
-- 1.6  ORDER BY  (numbers and text; default is ASC)
-- ------------------------------------------------------------------------------------------------
SELECT * FROM customers ORDER BY first_name, age;               -- first_name, then age as tie-breaker
SELECT * FROM customers ORDER BY first_name DESC;               -- descending
SELECT * FROM customers ORDER BY age ASC, first_name DESC;      -- mixed directions


-- ------------------------------------------------------------------------------------------------
-- 1.7  LIMIT / OFFSET   [NOTE] SQL Server uses SELECT TOP n instead
-- ------------------------------------------------------------------------------------------------
SELECT * FROM orders LIMIT 5;               -- first 5 rows
SELECT * FROM orders LIMIT 10 OFFSET 5;     -- skip 5 rows, then return 10


-- ------------------------------------------------------------------------------------------------
-- 1.8  ALIASES  (AS)  - rename columns or tables temporarily
-- ------------------------------------------------------------------------------------------------
SELECT COUNT(order_id) AS num_orders FROM orders;                           -- column alias

SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customers;      -- concat + alias

SELECT * FROM customers AS c;                                               -- table alias
-- Tip: table aliases are essential for joins, self-joins and correlated subqueries.



/* ================================================================================================
   PART 2 - AGGREGATION & GROUPING
   ================================================================================================ */

-- ------------------------------------------------------------------------------------------------
-- 2.1  AGGREGATE FUNCTIONS  (collapse many rows into one value; NULLs are ignored except COUNT(*))
-- ------------------------------------------------------------------------------------------------
SELECT MIN(total_amount)        FROM orders;
SELECT MAX(total_amount)        FROM orders;
SELECT COUNT(*)                 FROM orders;    -- number of rows (NULLs included)
SELECT COUNT(total_amount)      FROM orders;    -- number of non-NULL values in the column
SELECT SUM(total_amount)        FROM orders;
SELECT SUM(total_amount / 10)   FROM orders;    -- aggregate over an expression
SELECT AVG(total_amount)        FROM orders;

-- Related scalar function (row-by-row, not an aggregate)
SELECT LENGTH(country) FROM customers;          -- bytes; use CHAR_LENGTH() for characters


-- ------------------------------------------------------------------------------------------------
-- 2.2  GROUP BY / HAVING
--      WHERE  filters rows  BEFORE grouping
--      HAVING filters groups AFTER  grouping (can use aggregates)
-- ------------------------------------------------------------------------------------------------
SELECT
    customer_id,
    SUM(total_amount) AS total_spent
FROM orders
GROUP BY customer_id;

-- With HAVING
SELECT
    customer_id,
    SUM(total_amount) AS total_spent
FROM orders
GROUP BY customer_id
HAVING SUM(total_amount) > 500;


-- ------------------------------------------------------------------------------------------------
-- 2.3  ROLLUP & CUBE
--      ROLLUP: GROUP BY plus hierarchical subtotals and a grand total (NULL = "total")
--      CUBE  : every possible combination of the grouped columns
-- ------------------------------------------------------------------------------------------------
-- [NOTE] Standard / PostgreSQL / SQL Server syntax:
SELECT year, month, SUM(sales) AS total_sales
FROM sales_data
GROUP BY ROLLUP (year, month);

SELECT year, month, SUM(sales) AS total_sales
FROM sales_data
GROUP BY CUBE (year, month);

-- [NOTE] MySQL syntax (MySQL has no CUBE):
SELECT year, month, SUM(sales) AS total_sales
FROM sales_data
GROUP BY year, month WITH ROLLUP;



/* ================================================================================================
   PART 3 - COMBINING DATA
   ================================================================================================ */

-- ------------------------------------------------------------------------------------------------
-- 3.1  JOINS
--      INNER      : only matching rows in both tables
--      LEFT       : all left rows + matches from right (NULL if none)
--      RIGHT      : all right rows + matches from left (NULL if none)
--      FULL OUTER : all rows from both sides   [NOTE] not supported in MySQL
-- ------------------------------------------------------------------------------------------------
-- INNER JOIN
SELECT
    c.customer_id, c.first_name,
    c.country,
    o.total_amount, o.order_date
FROM customers c
INNER JOIN orders o ON o.customer_id = c.customer_id;

-- LEFT JOIN (keeps customers with no orders)
SELECT
    c.customer_id, c.first_name,
    o.total_amount, o.order_date
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id;

-- ANTI JOIN (LEFT): rows in the left table with NO match on the right
SELECT
    c.customer_id, c.first_name
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.customer_id IS NULL;
-- ANTI RIGHT is the same idea with RIGHT JOIN and `WHERE c.customer_id IS NULL`.

-- SELF JOIN: join a table to itself (here: pairs of customers living in the same city)
SELECT
    a.first_name AS customer1,
    b.first_name AS customer2,
    a.city
FROM customers a, customers b
WHERE a.customer_id < b.customer_id     -- avoids self-pairs and duplicate mirrored pairs
  AND a.city = b.city
ORDER BY a.city;


-- ------------------------------------------------------------------------------------------------
-- 3.2  SET OPERATORS  (same number of columns & compatible types in both queries)
-- ------------------------------------------------------------------------------------------------
SELECT customer_id FROM customers1
UNION                                   -- combine, remove duplicates
SELECT customer_id FROM customers2;

SELECT customer_id FROM customers1
UNION ALL                               -- combine, keep duplicates (faster)
SELECT customer_id FROM customers2;

SELECT customer_id FROM customers1
INTERSECT                               -- only rows present in both
SELECT customer_id FROM customers2;

SELECT customer_id FROM customers1
EXCEPT                                  -- rows in the first but not in the second (difference)
SELECT customer_id FROM customers2;     -- [NOTE] Oracle calls this MINUS



/* ================================================================================================
   PART 4 - ADVANCED QUERYING
   ================================================================================================ */

-- ------------------------------------------------------------------------------------------------
-- 4.1  SUBQUERIES: EXISTS / ANY / ALL
-- ------------------------------------------------------------------------------------------------
-- EXISTS: true if the subquery returns at least one row
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM customers c
WHERE EXISTS (
    SELECT *
    FROM orders o
    WHERE o.customer_id = c.customer_id
);

-- NOT EXISTS: customers with no orders
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM customers c
WHERE NOT EXISTS (
    SELECT *
    FROM orders o
    WHERE o.customer_id = c.customer_id
);

-- ANY: condition true for AT LEAST ONE value returned by the subquery
SELECT product_name
FROM products
WHERE product_id > ANY (
    SELECT product_id
    FROM order_items
    WHERE quantity = 10
);

-- ALL: condition true for EVERY value returned by the subquery
SELECT product_name
FROM products
WHERE product_id > ALL (
    SELECT product_id
    FROM order_items
    WHERE quantity = 10
);


-- ------------------------------------------------------------------------------------------------
-- 4.2  CASE  (if / else logic inside a query)
-- ------------------------------------------------------------------------------------------------
SELECT
    order_id,
    total_amount,
    CASE
        WHEN total_amount > 80 THEN 'big order'
        WHEN total_amount = 80 THEN 'order is exactly 80'
        ELSE 'small order'
    END AS order_details
FROM orders;


-- ------------------------------------------------------------------------------------------------
-- 4.3  COALESCE  (returns the first non-NULL argument)
-- ------------------------------------------------------------------------------------------------
SELECT
    customer_id,
    COALESCE(country, 'Unknown') AS country      -- single quotes = string, double quotes = identifier
FROM customers;


-- ------------------------------------------------------------------------------------------------
-- 4.4  CTE  (Common Table Expression) - a named subquery, easier to read than nesting
-- ------------------------------------------------------------------------------------------------
WITH sales_summary AS (
    SELECT item, SUM(price) AS total
    FROM cafe_sales
    GROUP BY item
)
SELECT item, total
FROM sales_summary
WHERE total > 20;

-- Multiple CTEs (later ones can reference earlier ones)
WITH avg_sales AS (
    SELECT AVG(price) AS avg_price
    FROM cafe_sales
),
high_sales AS (
    SELECT item, price
    FROM cafe_sales
    WHERE price > (SELECT avg_price FROM avg_sales)
)
SELECT item, price
FROM high_sales
ORDER BY price DESC;



/* ================================================================================================
   PART 5 - WINDOW FUNCTIONS
   Like aggregates, but rows are NOT collapsed. Syntax: func() OVER (PARTITION BY ... ORDER BY ...)
   ================================================================================================ */

-- ------------------------------------------------------------------------------------------------
-- 5.1  AGGREGATE WINDOWS
-- ------------------------------------------------------------------------------------------------
SELECT
    id,
    item,
    SUM(quantity) OVER (PARTITION BY location) AS total_quantity
FROM cafe;


-- ------------------------------------------------------------------------------------------------
-- 5.2  RANKING FUNCTIONS
-- ------------------------------------------------------------------------------------------------
SELECT student, scores, RANK()       OVER (ORDER BY scores DESC) AS rnk FROM students;  -- ties share rank, gaps follow (1,2,2,4)
SELECT student, scores, DENSE_RANK() OVER (ORDER BY scores DESC) AS rnk FROM students;  -- ties share rank, no gaps    (1,2,2,3)
SELECT student, scores, ROW_NUMBER() OVER (ORDER BY scores DESC) AS rn  FROM students;  -- unique sequential number    (1,2,3,4)
SELECT student, scores, NTILE(4)     OVER (ORDER BY scores DESC) AS quartile FROM students; -- splits rows into 4 equal buckets


-- ------------------------------------------------------------------------------------------------
-- 5.3  VALUE FUNCTIONS
-- ------------------------------------------------------------------------------------------------
-- LAG: value from the previous row
SELECT item, price, sale_date,
       LAG(price) OVER (PARTITION BY sale_date ORDER BY id) AS previous_price
FROM cafe_sales;

-- LEAD: value from the next row
SELECT item, price, sale_date,
       LEAD(price) OVER (PARTITION BY sale_date ORDER BY id) AS next_price
FROM cafe_sales;

-- FIRST_VALUE: first value in the window
SELECT item, price, sale_date,
       FIRST_VALUE(price) OVER (PARTITION BY sale_date ORDER BY price DESC) AS highest_price
FROM cafe_sales;

-- LAST_VALUE: last value in the window
-- Gotcha: the default frame ends at the CURRENT row, so you must widen the frame explicitly.
SELECT item, price, sale_date,
       LAST_VALUE(price) OVER (
           PARTITION BY sale_date
           ORDER BY price
           ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
       ) AS highest_price
FROM cafe_sales;



/* ================================================================================================
   PART 6 - MODIFYING DATA (DML)
   ================================================================================================ */

-- ------------------------------------------------------------------------------------------------
-- 6.1  INSERT INTO
-- ------------------------------------------------------------------------------------------------
-- Specified columns (safest: order doesn't matter, omitted columns get defaults)
INSERT INTO customers (customer_id, first_name, last_name, country, age)
VALUES (35, 'Ahmed', 'Hazem', 'Egypt', 18);

-- All columns (values must follow the table's exact column order)
INSERT INTO customers
VALUES (36, 'Ahmed', 'Hazem', 'Egypt', 18);

-- Multiple rows in one statement
INSERT INTO customers (customer_id, first_name, last_name, country, age)
VALUES (37, 'Ahmed',   'Hazem', 'Egypt', 18),
       (38, 'Mohamed', 'Hamza', 'Canada', 20),
       (39, 'Yousef',  'Hady',  'USA',    30);


-- ------------------------------------------------------------------------------------------------
-- 6.2  UPDATE  (ALWAYS include WHERE, otherwise every row changes)
-- ------------------------------------------------------------------------------------------------
UPDATE customers
SET age = 18
WHERE customer_id = 3;


-- ------------------------------------------------------------------------------------------------
-- 6.3  DELETE  (ALWAYS include WHERE, otherwise every row is removed)
-- ------------------------------------------------------------------------------------------------
DELETE FROM customers WHERE age < 18;

-- DELETE FROM customers;     -- removes ALL rows, keeps the table structure
-- TRUNCATE TABLE customers;  -- removes ALL rows faster, resets AUTO_INCREMENT



/* ================================================================================================
   PART 7 - DEFINING STRUCTURE (DDL)
   ================================================================================================ */

-- ------------------------------------------------------------------------------------------------
-- 7.1  CREATE / DROP DATABASE
-- ------------------------------------------------------------------------------------------------
CREATE DATABASE Sales;
-- DROP DATABASE Sales;       -- permanent!


-- ------------------------------------------------------------------------------------------------
-- 7.2  CREATE TABLE
--      Constraints : PRIMARY KEY, NOT NULL, UNIQUE, CHECK, FOREIGN KEY, AUTO_INCREMENT, DEFAULT
--      Data types  : INT, BIGINT, VARCHAR(n), DATE, DECIMAL(p, s)    (UNSIGNED = no negatives)
-- ------------------------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT SIGNED PRIMARY KEY AUTO_INCREMENT,
    first_name  VARCHAR(50) NOT NULL,
    last_name   VARCHAR(50) NOT NULL,
    city        VARCHAR(50) DEFAULT 'Unknown',
    country     VARCHAR(50) DEFAULT 'Unknown'
);

CREATE TABLE IF NOT EXISTS orders (
    order_id     INT PRIMARY KEY AUTO_INCREMENT,
    customer_id  INT NOT NULL,
    order_date   DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount > 0 AND total_amount < 100000),
    zip_code     VARCHAR(100) UNIQUE,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
        ON DELETE CASCADE       -- deleting a customer deletes their orders
        ON UPDATE CASCADE       -- changing customer_id updates it here too
);


-- ------------------------------------------------------------------------------------------------
-- 7.3  ALTER TABLE
-- ------------------------------------------------------------------------------------------------
ALTER TABLE cafe ADD COLUMN discount INTEGER;                           -- add column
ALTER TABLE cafe DROP COLUMN discount;                                  -- drop column
ALTER TABLE cafe RENAME COLUMN `Price Per Unit` TO price;               -- rename column (backticks for names with spaces)
ALTER TABLE cafe MODIFY COLUMN quantity INTEGER;                        -- change data type


-- ------------------------------------------------------------------------------------------------
-- 7.4  DROP TABLE
-- ------------------------------------------------------------------------------------------------
-- DROP TABLE orders;         -- deletes the table AND its data permanently



/* ================================================================================================
   PART 8 - DATABASE OBJECTS & PERFORMANCE
   ================================================================================================ */

-- ------------------------------------------------------------------------------------------------
-- 8.1  VIEWS  (virtual table based on a stored SELECT query)
-- ------------------------------------------------------------------------------------------------
-- Create a view
CREATE VIEW view_table AS
SELECT
    c.first_name,
    c.last_name,
    SUM(o.total_amount) AS total_order_amount
FROM customers c
INNER JOIN orders o USING (customer_id)
GROUP BY c.first_name, c.last_name;

SELECT * FROM view_table;       -- query it like a normal table

-- Modify a view (a name is required)
CREATE OR REPLACE VIEW employee_department_hours AS
SELECT
    e.fname,
    e.lname,
    d.pname,
    e.hours
FROM employees e
INNER JOIN department d ON e.department_id = d.department_id
WHERE e.department_id = 5;

-- WITH CHECK OPTION: INSERT/UPDATE through the view must satisfy the view's WHERE clause
CREATE VIEW vw_high_status_suppliers AS
SELECT *
FROM suppliers
WHERE status > 15
WITH CHECK OPTION;

-- DROP VIEW view_table;


-- ------------------------------------------------------------------------------------------------
-- 8.2  STORED PROCEDURES  (named, reusable blocks of SQL stored in the database)
--      DELIMITER changes the statement terminator so the ; inside the body doesn't end the CREATE.
-- ------------------------------------------------------------------------------------------------
DELIMITER //

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
    JOIN products p     ON p.product_id = oi.product_id
    WHERE o.customer_id = cust_id
      AND o.status = 'completed';
END //

DELIMITER ;

-- The application only needs:
CALL GetCustomerOrders(1453);
-- No direct access to the underlying tables is required (good for security).


-- ------------------------------------------------------------------------------------------------
-- 8.3  INDEXES  (speed up searching/filtering at the cost of slower writes and extra storage)
-- ------------------------------------------------------------------------------------------------
CREATE INDEX idx_customer_country
ON customers (country);


-- ------------------------------------------------------------------------------------------------
-- 8.4  EXPLAIN / EXPLAIN ANALYZE
--      EXPLAIN         : shows the planned execution (use while designing/debugging a query)
--      EXPLAIN ANALYZE : actually runs the query and shows real timings (use when optimizing)
-- ------------------------------------------------------------------------------------------------
EXPLAIN SELECT * FROM customers;
EXPLAIN ANALYZE SELECT * FROM customers;


/* ================================================================================================
   PART 9 - FUNCTION CHEAT SHEETS
   ================================================================================================ */

/* ------------------------------------------------------------------------------------------------
   9.1  STRING FUNCTIONS
   ------------------------------------------------------------------------------------------------
   LENGTH(str)                      Length in bytes (CHAR_LENGTH(str) = length in characters)
   LEFT(str, len)                   Leftmost len characters
   RIGHT(str, len)                  Rightmost len characters
   LOWER(str) / UPPER(str)          Convert case
   CONCAT(str1, str2, ...)          Join strings
   CONCAT_WS(sep, str1, str2, ...)  Join strings with a separator
   SUBSTRING(str, pos, len)         Extract len characters starting at pos
   TRIM(str)                        Remove leading and trailing spaces
   REPLACE(str, from_str, to_str)   Replace all occurrences of from_str with to_str
   REPEAT(str, count)               Repeat str count times
   REVERSE(str)                     Reverse the string
*/

/* ------------------------------------------------------------------------------------------------
   9.2  NUMERIC FUNCTIONS
   ------------------------------------------------------------------------------------------------
   Basic        ABS(x), ROUND(x, d), TRUNCATE(x, d), CEIL(x), FLOOR(x)
   Powers/logs  POW(x, y), EXP(x), LN(x), LOG(x), LOG10(x), LOG2(x)
   Trig         SIN(x), COS(x), TAN(x), ASIN(x), ACOS(x), ATAN(x)
   Angles       DEGREES(x), RADIANS(x)
   Constants    PI()
*/

/* ------------------------------------------------------------------------------------------------
   9.3  DATE & TIME FUNCTIONS
   ------------------------------------------------------------------------------------------------
   Current values
     NOW()                            Current date and time   (YYYY-MM-DD HH:MM:SS)
     CURRENT_DATE()                   Current date only       (YYYY-MM-DD)
     CURRENT_TIME()                   Current time only       (HH:MM:SS)

   Arithmetic
     ADDDATE(date, INTERVAL n unit)   Add interval, e.g. ADDDATE('2025-09-05', INTERVAL 10 DAY)
     ADDTIME(datetime, time)          Add time,     e.g. ADDTIME('2025-09-05 10:00:00', '02:30:00')
     DATE_SUB(date, INTERVAL n unit)  Subtract interval from a date
     DATEDIFF(date1, date2)           Days between two dates (MySQL: 2 arguments, no unit)

   Extracting parts
     DATE(datetime)                   Date part only
     TIME(datetime)                   Time part only
     DAY(date) / DAYOFMONTH(date)     Day of month (1-31)
     DAYNAME(date)                    Weekday name, e.g. 'Friday'
     DAYOFWEEK(date)                  Weekday index (1 = Sunday ... 7 = Saturday)
     DAYOFYEAR(date)                  Day of year (1-366)
     MONTH(date) / MONTHNAME(date)    Month number (1-12) / name, e.g. 'September'
     YEAR(date)                       Year
     QUARTER(date)                    Quarter (1-4)
     HOUR(time), MINUTE(time), SECOND(time)
     EXTRACT(unit FROM date)          General extractor, e.g. EXTRACT(YEAR FROM '2025-09-05')

   Formatting
     DATE_FORMAT(date, format)        e.g. '%W, %M %d, %Y'
     TIME_FORMAT(time, format)        e.g. TIME_FORMAT('14:05:00', '%h:%i %p') -> '02:05 PM'
*/