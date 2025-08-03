-- Calculate the real and estimated delivery time for each month
--
-- It will have different columns: 
-- 1. month_no, with the month numbers going from 01 to 12
-- 2. month, with the 3 first letters of each month (e.g. Jan, Feb)
-- 3. Year2016_real_time, with the average delivery time per month of 2016 (NaN if it doesn't exist) 
-- 4. Year2017_real_time, with the average delivery time per month of 2017 (NaN if it doesn't exist)
-- 5. Year2018_real_time, with the average delivery time per month of 2018 (NaN if it doesn't exist)
-- 6. Year2016_estimated_time, with the average estimated delivery time per month of 2016 (NaN if it doesn't exist) 
-- 7. Year2017_estimated_time, with the average estimated delivery time per month of 2017 (NaN if it doesn't exist)
-- 8. Year2018_estimated_time, with the average estimated delivery time per month of 2018 (NaN if it doesn't exist).
--
-- Explanation step by step:
-- 1. Calculate the real and estimated delivery time for each order
-- 2. Group the data by month
-- 3. Calculate the average real and estimated delivery time for each month
WITH
    base AS (
        SELECT
            STRFTIME ('%m', oo.order_purchase_timestamp) AS month_no,
            STRFTIME ('%Y', oo.order_purchase_timestamp) AS year,
            julianday (oo.order_delivered_customer_date) - julianday (oo.order_purchase_timestamp) AS real_time,
            julianday (oo.order_estimated_delivery_date) - julianday (oo.order_purchase_timestamp) AS estimated_time
        FROM
            olist_orders oo
        WHERE
            oo.order_status = 'delivered'
            AND oo.order_delivered_customer_date IS NOT NULL
    ),
    pivot AS (
        SELECT
            b.month_no,
            AVG(
                CASE
                    WHEN year = '2016' THEN b.real_time
                END
            ) AS Year2016_real_time,
            AVG(
                CASE
                    WHEN year = '2017' THEN b.real_time
                END
            ) AS Year2017_real_time,
            AVG(
                CASE
                    WHEN year = '2018' THEN b.real_time
                END
            ) AS Year2018_real_time,
            AVG(
                CASE
                    WHEN year = '2016' THEN b.estimated_time
                END
            ) AS Year2016_estimated_time,
            AVG(
                CASE
                    WHEN year = '2017' THEN b.estimated_time
                END
            ) AS Year2017_estimated_time,
            AVG(
                CASE
                    WHEN year = '2018' THEN b.estimated_time
                END
            ) AS Year2018_estimated_time
        FROM
            base b
        GROUP BY
            month_no
    )
SELECT
    p.month_no,
    CASE p.month_no
        WHEN '01' THEN 'Jan'
        WHEN '02' THEN 'Feb'
        WHEN '03' THEN 'Mar'
        WHEN '04' THEN 'Apr'
        WHEN '05' THEN 'May'
        WHEN '06' THEN 'Jun'
        WHEN '07' THEN 'Jul'
        WHEN '08' THEN 'Aug'
        WHEN '09' THEN 'Sep'
        WHEN '10' THEN 'Oct'
        WHEN '11' THEN 'Nov'
        WHEN '12' THEN 'Dec'
    END AS month,
    p.Year2016_real_time,
    p.Year2017_real_time,
    p.Year2018_real_time,
    p.Year2016_estimated_time,
    p.Year2017_estimated_time,
    p.Year2018_estimated_time
FROM
    pivot p
ORDER BY
    p.month_no;