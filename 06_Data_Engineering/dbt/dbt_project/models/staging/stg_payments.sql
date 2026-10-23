{{ config(
    materialized='table',
    tags=['staging']
) }}

SELECT
    order_id,
    payment_sequential,
    payment_type,
    
    CAST(payment_installments AS integer)     AS payment_installments,
    CAST(payment_value AS numeric)            AS payment_value

FROM {{ ref('df_Payments') }}