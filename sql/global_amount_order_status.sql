-- Calculates the amount of orders for each order status.
--
-- Explanation step by step:
-- 1. Select the order status and the amount of orders for each order status.
-- 2. Join the olist_orders table with the olist_order_items table on the order_id column.
-- 3. Group the results by the order status.
SELECT
    oo.order_status,
    COUNT(oo.order_status) AS Amount
FROM
    olist_orders oo
GROUP BY
    oo.order_status;