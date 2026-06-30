{{ config(materialized='table') }}

SELECT
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp,
order_delivered_customer_date
FROM {{ source('raw_data', 'orders') }} 
WHERE order_status = 'delivered'
