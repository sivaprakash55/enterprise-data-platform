{{ config(materialized='incremental') }}
SELECT order_id, customer_id, amount, order_date
FROM {{ ref('core_orders') }}
{% if is_incremental() %}
WHERE order_date > (SELECT MAX(order_date) FROM {{ this }})
{% endif %}