{% macro positive_values(model, column_name) %}
    SELECT *
    FROM {{ model }}
    WHERE {{ column_name }} < 0
       OR {{ column_name }} IS NULL
{% endmacro %}
-- ==============================================================

{% macro calculate_order_metrics() %}
    -- Reusable logic for order metrics
    SUM(price) AS total_price,
    SUM(shipping_charges) AS total_shipping,
    SUM(price + shipping_charges) AS total_order_value,
    COUNT(*) AS item_count,
    ROUND(AVG(price), 2) AS avg_item_price
{% endmacro %}
-- ==============================================================

{% macro flag_high_value_order(threshold=100) %}
    CASE 
        WHEN SUM(price + shipping_charges) >= {{ threshold }} THEN 'High Value'
        ELSE 'Regular'
    END AS order_value_flag
{% endmacro %}