-- List all films with their titles, release years, and rental rates.
SELECT
    title,
    release_year,
    rental_rate
FROM film;
--================================================================

-- Count the total number of customers.
SELECT COUNT(*) FROM customer;
--================================================================

-- Find the top 5 most expensive films (by replacement cost).
SELECT
    film_id,
    title,
    replacement_cost
FROM film
ORDER BY replacement_cost DESC
LIMIT 5;
--================================================================

-- Show the number of films per rating category.
SELECT
    rating,
    COUNT(film_id) AS num_of_films
FROM film
GROUP BY rating;
--================================================================

-- List all actors with their first and last names, sorted alphabetically by last name.
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name
FROM actor
ORDER BY last_name;
--================================================================

-- Count how many rentals were made in total.
SELECT COUNT(*) FROM rental;
--================================================================

-- Find the total number of films in each category.
SELECT
    name,
    COUNT(film_id) AS num_of_films
FROM category  
INNER JOIN film_category USING (category_id)
GROUP BY name;
--================================================================

-- Show the first and last names of all customers who live in the United States
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name
FROM customer
INNER JOIN address USING (address_id)
INNER JOIN city USING (city_id)
INNER JOIN country USING (country_id)
WHERE country = 'United States';
--================================================================

-- List all stores with their addresses.
SELECT
    store_id,
    address
FROM store
INNER JOIN address USING(address_id);
--================================================================

-- Find the average rental rate across all films.
SELECT
ROUND(AVG(rental_rate), 2) AS avg_rental_rate
FROM film;
--================================================================

-- Find the top 10 customers by total amount spent (rental payments).
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name,
    SUM(amount) AS total_spent
FROM customer
INNER JOIN payment USING (customer_id)
GROUP BY full_name
ORDER BY total_spent DESC
LIMIT 10;
--================================================================

-- Show the number of rentals per customer, sorted by most active customers.
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name,
    COUNT(rental_id) AS num_of_rentals
FROM customer
INNER JOIN rental USING (customer_id)
GROUP BY full_name
ORDER BY num_of_rentals DESC;
--================================================================

-- List films that have never been rented.
SELECT
    title AS film_name
FROM film
LEFT JOIN inventory USING (film_id)
LEFT JOIN rental USING (inventory_id)
WHERE rental_id IS NULL;
--================================================================

-- Find the average rental duration (in days) per film category.
SELECT
    name AS category_name,
    AVG(return_date - rental_date) AS avg_rental_duration -- it gives me in days 
FROM rental
INNER JOIN inventory USING (inventory_id)
INNER JOIN film USING (film_id)
INNER JOIN film_category USING (film_id)
INNER JOIN category USING (category_id)
GROUP BY category_name;
--================================================================

-- Identify staff members and the total payments they processed.
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name,
    SUM(amount) AS total_amount
FROM staff
INNER JOIN payment USING (staff_id)
GROUP BY full_name;
--================================================================

-- Find the most popular film categories based on rental count.
SELECT
    name,
    COUNT(rental_id) AS count_of_rentals
FROM rental
INNER JOIN inventory USING (inventory_id)
INNER JOIN film_category USING (film_id)
INNER JOIN category USING (category_id)
GROUP BY name
ORDER BY count_of_rentals DESC;
--================================================================

-- Show customer names along with their city and country.
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name,
    city,
    country
FROM customer
INNER JOIN address USING (address_id)
INNER JOIN city USING (city_id)
INNER JOIN country USING (country_id);
--================================================================

-- Calculate monthly rental revenue trends (by month and year).
SELECT
    EXTRACT(YEAR FROM payment_date) AS year,
    EXTRACT(MONTH FROM payment_date) AS month,
    SUM(amount) AS total_amount
FROM payment
GROUP BY year, month
ORDER BY year, month;
--================================================================

-- Find films where the rental rate is higher than the average rental rate.
SELECT
    title
FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film);
--================================================================

-- Determine which actors have appeared in the most films.
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name,
    COUNT(film_id) AS count_apperance
FROM actor
INNER JOIN film_actor USING (actor_id)
INNER JOIN film USING (film_id)
GROUP BY full_name
ORDER BY count_apperance DESC;
--================================================================

-- Find the top 5 customers by total spending in each store (with window functions).
WITH table1 AS (
    SELECT
        CONCAT(first_name, ' ', last_name) AS full_name,
        store_id,
        SUM(amount) AS total_amount
    FROM customer
    INNER JOIN payment USING (customer_id) 
    GROUP BY full_name, store_id
),
table2 AS (
    SELECT *,
    ROW_NUMBER() OVER (PARTITION BY store_id ORDER BY total_amount DESC) AS ranking
    FROM table1
)
SELECT * FROM table2 WHERE ranking IN (1, 2, 3, 4, 5);
--================================================================

-- Calculate the cumulative revenue over time (running total by date).
SELECT
SUM(amount) OVER (ORDER BY payment_date) AS cumm_payment
FROM payment
ORDER BY payment_date;
--================================================================

-- Identify films that were rented in every month of the year (full-year coverage).
WITH table1 AS (
SELECT 
    DISTINCT title,
    EXTRACT(MONTH FROM rental_date) AS months
FROM film
INNER JOIN inventory USING (film_id)
INNER JOIN rental USING (inventory_id)
),
table2 AS (
SELECT
    title,
    ROW_NUMBER() OVER (PARTITION BY title ORDER BY months) AS ranking
FROM table1
)
SELECT title from table2 where ranking = 12;
--================================================================

-- Find the percentage of total revenue contributed by each customer segment (e.g., by city or country)
WITH table1 AS (
SELECT
    country,
    SUM(amount) AS total_amount
FROM payment
INNER JOIN customer USING (customer_id)
INNER JOIN address USING (address_id)
INNER JOIN city USING (city_id)
INNER JOIN country USING (country_id)
GROUP BY country
),
total_revenue AS (
SELECT SUM(total_amount) AS total_revenue_ FROM table1
)
SELECT
    country,
    (total_amount / (SELECT total_revenue_ From total_revenue) * 100) AS percent_sum_revenue
FROM table1;
--================================================================

-- Rank films by rental count within each category using window functions.
WITH table1 AS (
    SELECT
        title,
        name AS categroy_name,
        COUNT(rental_id) AS count_rental
    FROM rental
    INNER JOIN inventory USING (inventory_id)
    INNER JOIN film USING (film_id)
    INNER JOIN film_category USING (film_id)
    INNER JOIN category USING (category_id)
    GROUP BY name, title
)
SELECT
    *,
    RANK() OVER (PARTITION BY categroy_name ORDER BY count_rental DESC) AS rank_
FROM table1;
--================================================================

-- Find customers who have rented more than the average number of films and spent above average.
WITH table1 AS (
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name,
    COUNT(rental_id) AS count_rental,
    SUM(amount) AS total_spent
FROM customer
INNER JOIN rental USING (customer_id)
INNER JOIN payment USING (rental_id)
GROUP BY full_name
)
SELECT
    *
FROM table1
WHERE count_rental > (SELECT AVG(count_rental) FROM table1)
AND total_spent > (SELECT AVG(total_spent) FROM table1);
--================================================================

-- Analyze inventory turnover: number of rentals per inventory item and average days between rentals.
SELECT
    inventory_id,
    COUNT(rental_id) AS count_rental,
    ROUND(AVG(EXTRACT(DAY FROM (return_date - rental_date))), 2) AS avg_bet_rentals
FROM inventory
INNER JOIN rental USING (inventory_id)
GROUP BY inventory_id;
--================================================================

-- Find the correlation between film length and rental count.
WITH table1 AS (
SELECT
    length AS film_length,
    COUNT(rental_id) AS count_rental
FROM film
INNER JOIN inventory USING (film_id)
INNER JOIN rental USING (inventory_id)
GROUP BY film_id
)
SELECT corr(film_length, count_rental) FROM table1;
--================================================================

-- Identify "loyal" customers: those who have rented in at least 6 different months.
WITH table1 AS (
SELECT
     DISTINCT CONCAT(first_name, ' ', last_name) AS full_name,
    EXTRACT(MONTH FROM rental_date) AS months
FROM customer
INNER JOIN rental USING (customer_id)
),
table2 AS (
SELECT
    *,
    ROW_NUMBER() OVER (PARTITION BY full_name) AS ranking
FROM table1
)
SELECT
    DISTINCT full_name
FROM table2
WHERE ranking >= 6;
--================================================================