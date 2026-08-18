{{ config(
    materialized='table',
    tags=['staging']
) }}

SELECT
    customer_id,
    customer_zip_code_prefix,
    customer_city,
    customer_state
FROM {{ ref('df_Customers') }}  