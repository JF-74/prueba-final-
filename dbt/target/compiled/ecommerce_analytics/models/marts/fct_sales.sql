

SELECT
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp,
order_delivered_customer_date
FROM "ecommerce_analytics"."main"."orders" 
WHERE order_status = 'delivered'