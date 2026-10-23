{{ config(
    materialized='table',
    tags=['staging']
) }}

SELECT
    product_id,
    product_category_name,
    
    CAST(product_weight_g AS numeric)         AS product_weight_g,
    CAST(product_length_cm AS numeric)        AS product_length_cm,
    CAST(product_height_cm AS numeric)        AS product_height_cm,
    CAST(product_width_cm AS numeric)         AS product_width_cm,
    
    -- Derived: Volume & Density
    (product_length_cm * product_height_cm * product_width_cm) AS product_volume_cm3,
    CASE 
        WHEN product_weight_g > 0 
        THEN ROUND((product_length_cm * product_height_cm * product_width_cm) / product_weight_g, 2) 
        ELSE NULL 
    END AS volume_per_gram

FROM {{ ref('df_Products') }}