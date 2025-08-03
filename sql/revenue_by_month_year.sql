-- Calculates revenue by month and year
--
-- It will have different columns: 
-- 1. month_no, with the month numbers going from 01 to 12
-- 2. month, with the 3 first letters of each month (e.g. Jan, Feb)
-- 3. Year2016, with the revenue per month of 2016 (0.00 if it doesn't exist)
-- 4. Year2017, with the revenue per month of 2017 (0.00 if it doesn't exist)
-- 5. Year2018, with the revenue per month of 2018 (0.00 if it doesn't exist)
--
-- Explanation step by step:
-- 1. Calculate the revenue for each order
-- 2. Group the data by month
-- 3. Calculate the average revenue for each month
WITH
    month_names AS (
        SELECT
            '01' AS month_no,
            'Jan' AS month
        UNION ALL
        SELECT
            '02',
            'Feb'
        UNION ALL
        SELECT
            '03',
            'Mar'
        UNION ALL
        SELECT
            '04',
            'Apr'
        UNION ALL
        SELECT
            '05',
            'May'
        UNION ALL
        SELECT
            '06',
            'Jun'
        UNION ALL
        SELECT
            '07',
            'Jul'
        UNION ALL
        SELECT
            '08',
            'Aug'
        UNION ALL
        SELECT
            '09',
            'Sep'
        UNION ALL
        SELECT
            '10',
            'Oct'
        UNION ALL
        SELECT
            '11',
            'Nov'
        UNION ALL
        SELECT
            '12',
            'Dec'
    ),
    -- Get the minimum payment per order
    min_payments AS (
        SELECT
            oop.order_id,
            MIN(oop.payment_value) AS min_payment
        FROM
            olist_order_payments oop
        GROUP BY
            oop.order_id
    ),
    -- Calculate revenue grouped by year and month
    revenue AS (
        SELECT
            strftime ('%m', oo.order_delivered_customer_date) AS month_no,
            strftime ('%Y', oo.order_delivered_customer_date) AS year,
            SUM(mp.min_payment) AS total_revenue
        FROM
            olist_orders oo
            JOIN min_payments mp ON oo.order_id = mp.order_id
        WHERE
            oo.order_status = 'delivered'
            AND oo.order_delivered_customer_date IS NOT NULL
            AND strftime ('%Y', oo.order_delivered_customer_date) IN ('2016', '2017', '2018')
        GROUP BY
            month_no,
            year
    )
    -- Final Select
SELECT
    mn.month_no,
    mn.month,
    COALESCE(
        MAX(
            CASE
                WHEN r.year = '2016' THEN r.total_revenue
            END
        ),
        0.0
    ) AS Year2016,
    COALESCE(
        MAX(
            CASE
                WHEN r.year = '2017' THEN r.total_revenue
            END
        ),
        0.0
    ) AS Year2017,
    COALESCE(
        MAX(
            CASE
                WHEN r.year = '2018' THEN r.total_revenue
            END
        ),
        0.0
    ) AS Year2018
FROM
    month_names mn
    LEFT JOIN revenue r ON mn.month_no = r.month_no
GROUP BY
    mn.month_no,
    mn.month
ORDER BY
    mn.month_no;