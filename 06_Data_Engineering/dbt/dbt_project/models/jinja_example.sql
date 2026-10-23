{{ config(
    materialized='table',
    tags=['example', 'jinja']
) }}

-- ========================================
-- JINJA EXAMPLE: Variables, Loops & If Conditions
-- ========================================

{% set numeric_columns = ['price', 'shipping_charges', 'payment_value', 'total_item_value'] %}
{% set order_status_list = ['delivered', 'shipped', 'canceled', 'invoiced'] %}
{% set high_value_threshold = 300 %}

WITH base_data AS (
    SELECT 
        oi.order_id,
        oi.product_id,
        o.customer_id,
        o.order_status,
        o.order_purchase_timestamp,
        oi.price,
        oi.shipping_charges,
        oi.total_item_value,
        p.payment_value,
        p.payment_type
    FROM {{ ref('stg_order_items') }} oi
    JOIN {{ ref('stg_orders') }} o 
        ON oi.order_id = o.order_id
    LEFT JOIN {{ ref('stg_payments') }} p 
        ON oi.order_id = p.order_id
),

transformed AS (
    SELECT
        *,
        
        -- 1. Variable Example
        {% set current_year = 2018 %}   -- You can change this or make it dynamic
        CASE 
            WHEN EXTRACT(YEAR FROM order_purchase_timestamp) = {{ current_year }} 
            THEN 'Current Year'
            ELSE 'Previous Years' 
        END AS year_category,

        -- 2. For Loop Example: Dynamically cast multiple numeric columns
        {% for col in numeric_columns %}
            CAST({{ col }} AS numeric) as {{ col }}_cleaned{% if not loop.last %},{% endif %}
        {% endfor %},

        -- 3. If Condition + For Loop: Flag high value orders
        {% if high_value_threshold > 0 %}
            CASE 
                WHEN total_item_value >= {{ high_value_threshold }} THEN 'High Value Order'
                WHEN total_item_value >= 100 THEN 'Medium Value Order'
                ELSE 'Low Value Order'
            END AS value_segment,
        {% else %}
            'All Orders' AS value_segment,
        {% endif %}

        -- 4. For Loop with If inside: Dynamic status grouping
        CASE 
            {% for status in order_status_list %}
                WHEN LOWER(order_status) = '{{ status }}' 
                    THEN '{{ status | title }} Order'
            {% endfor %}
            ELSE 'Other Status'
        END AS order_status_grouped

    FROM base_data
)

SELECT 
    *,
    
    -- Final calculated column using variables
    {% set delivery_target = 7 %}
    CASE 
        WHEN DATE_DIFF('day', order_purchase_timestamp, order_delivered_timestamp) <= {{ delivery_target }}
            THEN 'On Time'
        ELSE 'Delayed'
    END AS delivery_performance

FROM transformed