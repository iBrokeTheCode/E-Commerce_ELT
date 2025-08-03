-- Calculates the top 10 least revenue categories
--
-- It will have different columns: 
-- 1. Category, with the category name
-- 2. Num_order, with the number of orders
-- 3. Revenue, with the revenue
--
-- Explanation step by step:
-- 1. Calculate the revenue for each order
-- 2. Group the data by category
-- 3. Calculate the average revenue for each category
-- 4. Order the data by revenue
-- 5. Limit the data to the top 10
SELECT
    pcnt.product_category_name_english AS Category,
    COUNT(DISTINCT oo.order_id) AS Num_order,
    SUM(p.payment_value) AS Revenue
FROM
    olist_orders oo
    JOIN olist_order_items ooi ON oo.order_id = ooi.order_id
    JOIN olist_products op ON ooi.product_id = op.product_id
    JOIN product_category_name_translation pcnt ON op.product_category_name = pcnt.product_category_name
    JOIN olist_order_payments p ON oo.order_id = p.order_id
WHERE
    oo.order_status = 'delivered'
    AND oo.order_delivered_customer_date IS NOT NULL
    AND op.product_category_name IS NOT NULL
GROUP BY
    Category
ORDER BY
    Revenue ASC
LIMIT
    10;