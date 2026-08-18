{{ config(
    materialized='table',
    tags=['staging']
) }}

SELECT
    order_id,
    customer_id,
    order_status,

    -- Timestamps
    CAST(order_purchase_timestamp AS timestamp)     AS order_purchase_timestamp,
    CAST(order_approved_at AS timestamp)            AS order_approved_at,
    CAST(order_delivered_timestamp AS timestamp)    AS order_delivered_timestamp,
    CAST(order_estimated_delivery_date AS timestamp) AS order_estimated_delivery_date,

    -- Derived columns
    DATE(order_purchase_timestamp)                  AS order_purchase_date,
    EXTRACT(YEAR FROM order_purchase_timestamp)     AS order_year,
    EXTRACT(MONTH FROM order_purchase_timestamp)    AS order_month

FROM {{ ref('df_Orders') }}