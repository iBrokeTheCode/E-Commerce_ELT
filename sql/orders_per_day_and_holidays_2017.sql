-- Calculates the number of orders per day and whether each day is a holiday.
--
-- Explanation step by step:
-- 1. Select the number of orders per day and whether each day is a holiday.
-- 2. Join the olist_orders table with the public_holidays table on the date column.
-- 3. Filter the results to only include orders from 2017.
-- 4. Group the results by the date.
-- 5. Order the results by the date.
SELECT
    COUNT(o.order_id) AS order_count,
    CAST(
        STRFTIME ('%s', DATE(o.order_purchase_timestamp)) AS INTEGER
    ) * 1000 AS date,
    CASE
        WHEN DATE(h.date) IS NOT NULL THEN 'true'
        ELSE 'false'
    END AS holiday
FROM
    olist_orders o
    LEFT JOIN public_holidays h ON DATE(o.order_purchase_timestamp) = DATE(h.date)
WHERE
    STRFTIME ('%Y', o.order_purchase_timestamp) = '2017'
GROUP BY
    DATE(o.order_purchase_timestamp)
ORDER BY
    DATE(o.order_purchase_timestamp);