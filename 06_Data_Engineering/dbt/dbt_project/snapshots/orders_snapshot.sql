{% snapshot orders_snapshot %}

{{ config(
    target_schema='snapshots',
    unique_key='order_id',
    strategy='timestamp',
    updated_at='order_approved_at'
) }}

SELECT 
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_timestamp,
    order_estimated_delivery_date,
    order_purchase_date,
    order_year,
    order_month
FROM {{ ref('stg_orders') }}

{% endsnapshot %}