-- Calculates the average difference in days between the estimated delivery date and the actual delivery date for all orders that have been delivered.
--
-- Explanation step by step:
-- 1. Select the customer state and the average difference in days between the estimated delivery date and the actual delivery date for all orders that have been delivered.
-- 2. Join the olist_orders table with the olist_customers table on the customer_id column.
-- 3. Filter the results to only include orders that have been delivered and have an actual delivery date.
-- 4. Group the results by the customer state.
-- 5. Order the results by the average difference in days between the estimated delivery date and the actual delivery date.
SELECT
    oc.customer_state AS State,
    CAST(
        AVG(
            julianday (
                STRFTIME ('%Y-%m-%d', oo.order_estimated_delivery_date)
            ) - julianday (
                STRFTIME ('%Y-%m-%d', oo.order_delivered_customer_date)
            )
        ) AS INTEGER
    ) AS Delivery_Difference
FROM
    olist_orders oo
    JOIN olist_customers oc ON oo.customer_id = oc.customer_id
WHERE
    oo.order_status = 'delivered'
    AND oo.order_delivered_customer_date IS NOT NULL
GROUP BY
    oc.customer_state
ORDER BY
    Delivery_Difference ASC;