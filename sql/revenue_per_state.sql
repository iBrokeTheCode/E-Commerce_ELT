-- Calculate the revenue per state
--
-- It will have different columns: 
-- 1. customer_state, with the state of the customer
-- 2. Revenue, with the revenue per state
--
-- Explanation step by step:
-- 1. Calculate the revenue for each order
-- 2. Group the data by state
-- 3. Calculate the average revenue for each state
-- 4. Order the data by revenue
-- 5. Limit the data to the top 10
SELECT
    oc.customer_state AS customer_state,
    SUM(oop.payment_value) AS Revenue
FROM
    olist_orders oo
    JOIN olist_customers oc ON oo.customer_id = oc.customer_id
    JOIN olist_order_payments oop ON oop.order_id = oo.order_id
WHERE
    oo.order_status = 'delivered'
    AND oo.order_delivered_customer_date IS NOT NULL
GROUP BY
    oc.customer_state
ORDER BY
    Revenue DESC
LIMIT
    10;