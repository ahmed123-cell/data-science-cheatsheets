{{ config(
    materialized='table',
    tags=['staging']
) }}

SELECT
    order_id,
    product_id,
    seller_id,
    
    CAST(price AS numeric)                    AS price,
    CAST(shipping_charges AS numeric)         AS shipping_charges,
    
    -- Business calculations
    price + shipping_charges                  AS total_item_value,
    1                                         AS item_quantity   -- assuming 1 per row

FROM {{ ref('df_OrderItems') }}