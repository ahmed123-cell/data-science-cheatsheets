{{ config(
    materialized='table',
    tags=['mart', 'fact']
) }}

WITH order_items_joined AS (
    SELECT
        oi.order_id,
        oi.product_id,
        oi.seller_id,
        oi.price,
        oi.shipping_charges,
        oi.total_item_value,
        
        o.customer_id,
        o.order_status,
        o.order_purchase_timestamp,
        o.order_delivered_timestamp,
        o.order_estimated_delivery_date,
        o.order_purchase_date,
        o.order_year,
        o.order_month,
        
        p.payment_type,
        p.payment_installments,
        p.payment_value,
        
        pr.product_category_name,
        pr.product_weight_g

    FROM {{ ref('stg_order_items') }} oi
    JOIN {{ ref('stg_orders') }} o 
        ON oi.order_id = o.order_id
    LEFT JOIN {{ ref('stg_payments') }} p 
        ON oi.order_id = p.order_id
    LEFT JOIN {{ ref('stg_products') }} pr 
        ON oi.product_id = pr.product_id
),

aggregated_orders AS (
    SELECT
        order_id,
        customer_id,
        order_status,
        order_purchase_timestamp,
        order_delivered_timestamp,
        order_estimated_delivery_date,
        order_purchase_date,
        order_year,
        order_month,
        payment_type,
        MAX(payment_installments) AS payment_installments,   -- one payment method per order usually
        SUM(payment_value) AS total_payment_value,
        
        -- Using macro for metrics
        {{ calculate_order_metrics() }},
        
        -- Using macro for business flag
        {{ flag_high_value_order(150) }},
        
        -- Delivery performance
        CASE 
            WHEN order_delivered_timestamp IS NOT NULL 
            THEN DATE_DIFF('day', order_purchase_timestamp, order_delivered_timestamp)
            ELSE NULL 
        END AS delivery_days_actual,
        
        DATE_DIFF('day', order_purchase_timestamp, order_estimated_delivery_date) AS delivery_days_estimated

    FROM order_items_joined
    GROUP BY 
        order_id, customer_id, order_status, order_purchase_timestamp,
        order_delivered_timestamp, order_estimated_delivery_date, 
        order_purchase_date, order_year, order_month, payment_type
)

SELECT * 
FROM aggregated_orders