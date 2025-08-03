from collections import namedtuple
from enum import Enum
from typing import Callable

from pandas import DataFrame, merge, read_sql, to_datetime
from sqlalchemy import Engine, TextClause, text

from src.config import QUERIES_ROOT_PATH

QueryResult = namedtuple("QueryResult", ["query", "result"])


class QueryEnum(Enum):
    """Enumerates all the queries"""

    DELIVERY_DATE_DIFFERENCE = "delivery_date_difference"
    GLOBAL_AMOUNT_ORDER_STATUS = "global_amount_order_status"
    REVENUE_BY_MONTH_YEAR = "revenue_by_month_year"
    REVENUE_PER_STATE = "revenue_per_state"
    TOP_10_LEAST_REVENUE_CATEGORIES = "top_10_least_revenue_categories"
    TOP_10_REVENUE_CATEGORIES = "top_10_revenue_categories"
    REAL_VS_ESTIMATED_DELIVERED_TIME = "real_vs_estimated_delivered_time"
    ORDERS_PER_DAY_AND_HOLIDAYS_2017 = "orders_per_day_and_holidays_2017"
    GET_FREIGHT_VALUE_WEIGHT_RELATIONSHIP = "get_freight_value_weight_relationship"


def read_query(query_name: str) -> TextClause:
    """
    Reads the query from the file and returns it as a string

    Args:
        query_name (str): The name of the query

    Returns:
        TextClause: The query
    """
    with open("{}/{}.sql".format(QUERIES_ROOT_PATH, query_name), "r") as file:
        sql_file = file.read()
        sql = text(sql_file)
    return sql


def query_delivery_date_difference(database: Engine) -> QueryResult:
    """
    Get the query for the delivery date difference

    Args:
        database (Engine): The database to get the data from

    Returns:
        QueryResult: The query and the result
    """
    query_name = QueryEnum.DELIVERY_DATE_DIFFERENCE.value
    query = read_query(QueryEnum.DELIVERY_DATE_DIFFERENCE.value)

    return QueryResult(query=query_name, result=read_sql(query, database))


def query_global_amount_order_status(database: Engine) -> QueryResult:
    """
    Get the query for the global amount of order status

    Args:
        database (Engine): The database to get the data from

    Returns:
        QueryResult: The query and the result
    """
    query_name = QueryEnum.GLOBAL_AMOUNT_ORDER_STATUS.value
    query = read_query(QueryEnum.GLOBAL_AMOUNT_ORDER_STATUS.value)

    return QueryResult(query=query_name, result=read_sql(query, database))


def query_revenue_by_month_year(database: Engine) -> QueryResult:
    """
    Get the query for the revenue by month and year

    Args:
        database (Engine): The database to get the data from

    Returns:
        QueryResult: The query and the result
    """
    query_name = QueryEnum.REVENUE_BY_MONTH_YEAR.value
    query = read_query(QueryEnum.REVENUE_BY_MONTH_YEAR.value)

    return QueryResult(query=query_name, result=read_sql(query, database))


def query_revenue_per_state(database: Engine) -> QueryResult:
    """
    Get the query for the revenue per state

    Args:
        database (Engine): The database to get the data from

    Returns:
        QueryResult: The query and the result
    """
    query_name = QueryEnum.REVENUE_PER_STATE.value
    query = read_query(QueryEnum.REVENUE_PER_STATE.value)

    return QueryResult(query=query_name, result=read_sql(query, database))


def query_top_10_least_revenue_categories(database: Engine) -> QueryResult:
    """
    Get the query for the top 10 least revenue categories

    Args:
        database (Engine): The database to get the data from

    Returns:
        QueryResult: The query and the result
    """
    query_name = QueryEnum.TOP_10_LEAST_REVENUE_CATEGORIES.value
    query = read_query(QueryEnum.TOP_10_LEAST_REVENUE_CATEGORIES.value)

    return QueryResult(query=query_name, result=read_sql(query, database))


def query_top_10_revenue_categories(database: Engine) -> QueryResult:
    """
    Get the query for the top 10 revenue categories

    Args:
        database (Engine): The database to get the data from

    Returns:
        QueryResult: The query and the result
    """
    query_name = QueryEnum.TOP_10_REVENUE_CATEGORIES.value
    query = read_query(QueryEnum.TOP_10_REVENUE_CATEGORIES.value)

    return QueryResult(query=query_name, result=read_sql(query, database))


def query_real_vs_estimated_delivered_time(database: Engine) -> QueryResult:
    """
    Get the query for the real vs estimated delivered time

    Args:
        database (Engine): The database to get the data from

    Returns:
        QueryResult: The query and the result
    """
    query_name = QueryEnum.REAL_VS_ESTIMATED_DELIVERED_TIME.value
    query = read_query(QueryEnum.REAL_VS_ESTIMATED_DELIVERED_TIME.value)

    return QueryResult(query=query_name, result=read_sql(query, database))


def query_freight_value_weight_relationship(database: Engine) -> QueryResult:
    """
    Get the query for the freight value weight relationship

    Args:
        database (Engine): The database to get the data from

    Returns:
        QueryResult: The query and the result
    """

    query_name = QueryEnum.GET_FREIGHT_VALUE_WEIGHT_RELATIONSHIP.value

    # Get data from database
    orders = read_sql("SELECT * FROM olist_orders", database)
    items = read_sql("SELECT * FROM olist_order_items", database)
    products = read_sql("SELECT * FROM olist_products", database)

    # Merge data
    items_products = merge(items, products, on="product_id")
    data = merge(items_products, orders, on="order_id")

    # Filter delivered orders
    delivered = data[data["order_status"] == "delivered"]

    # Get the sum of freight_value and product_weight_g for each order_id
    aggregations = delivered.groupby("order_id", as_index=False)[
        ["freight_value", "product_weight_g"]
    ].sum()

    return QueryResult(query=query_name, result=aggregations)


def query_orders_per_day_and_holidays_2017(database: Engine) -> QueryResult:
    query_name = QueryEnum.ORDERS_PER_DAY_AND_HOLIDAYS_2017.value

    # Get data from database
    holidays = read_sql("SELECT * FROM public_holidays", database)
    orders = read_sql("SELECT * FROM olist_orders", database)

    # Convert the date column to datetime
    orders["order_purchase_timestamp"] = to_datetime(orders["order_purchase_timestamp"])

    # Filter orders for 2017
    filtered_dates = orders[orders["order_purchase_timestamp"].dt.year == 2017]

    # Count orders per day
    order_purchase_amount_per_date = (
        filtered_dates.groupby(filtered_dates["order_purchase_timestamp"].dt.date)
        .size()
        .reset_index(name="order_count")
    )

    # Convert date column to datetime for comparison
    holidays["date"] = to_datetime(holidays["date"]).dt.date

    # Add milliseconds timestamp
    order_purchase_amount_per_date["date"] = to_datetime(
        order_purchase_amount_per_date["order_purchase_timestamp"]
    )
    order_purchase_amount_per_date["date"] = (
        order_purchase_amount_per_date["date"].astype("int64") // 10**6
    )

    # Check if each date is a holiday
    order_purchase_amount_per_date["holiday"] = order_purchase_amount_per_date[
        "order_purchase_timestamp"
    ].isin(holidays["date"])

    # Create a dataframe with the result
    result_df = order_purchase_amount_per_date[["order_count", "date", "holiday"]]

    return QueryResult(query=query_name, result=result_df)


def get_all_queries() -> list[Callable[[Engine], QueryResult]]:
    """
    Get all the queries

    Returns:
        list[Callable[[Engine], QueryResult]]: The queries
    """
    return [
        query_delivery_date_difference,
        query_global_amount_order_status,
        query_revenue_by_month_year,
        query_revenue_per_state,
        query_top_10_least_revenue_categories,
        query_top_10_revenue_categories,
        query_real_vs_estimated_delivered_time,
        query_orders_per_day_and_holidays_2017,
        query_freight_value_weight_relationship,
    ]


def run_queries(database: Engine) -> dict[str, DataFrame]:
    """
    Transform data based on queries. For each query, the query is executed and the results is stored in the dataframe

    Args:
        database (Engine): The database to get the data from

    Returns:
        dict[str, DataFrame]: A dictionary with keys as the query filenames and values the result of the query as a dataframe
    """

    query_results = {}

    for query in get_all_queries():
        query_result = query(database)
        query_results[query_result.query] = query_result.result

    return query_results
