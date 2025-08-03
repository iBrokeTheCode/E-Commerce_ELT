-- Calculates the total freight value and the total weight of the products in each order where the order status is 'delivered'.
--
-- Explanation step by step:
-- 1. Select the order ID, the total freight value, and the total weight of the products in each order where the order status is 'delivered'.
-- 2. Join the olist_orders table with the olist_order_items table on the order_id column.
-- 3. Join the olist_order_items table with the olist_products table on the product_id column.
-- 4. Filter the results to only include orders where the order status is 'delivered'.
-- 5. Group the results by the order ID.
-- 6. Order the results by the order ID.
SELECT
    ooi.order_id,
    SUM(ooi.freight_value) AS freight_value,
    SUM(op.product_weight_g) AS product_weight_g
FROM
    olist_orders o
    JOIN olist_order_items ooi ON o.order_id = ooi.order_id
    JOIN olist_products op ON ooi.product_id = op.product_id
WHERE
    o.order_status = 'delivered'
GROUP BY
    ooi.order_id
ORDER BY
    ooi.order_id