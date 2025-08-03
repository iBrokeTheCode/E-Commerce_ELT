from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent

DATASET_ROOT_PATH = str(ROOT_PATH / "dataset")
QUERIES_ROOT_PATH = str(ROOT_PATH / "sql")
QUERY_RESULTS_ROOT_PATH = str(ROOT_PATH / "tests/query_results")
PUBLIC_HOLIDAYS_URL = "https://date.nager.at/api/v3/publicholidays"
SQLITE_DB_ABSOLUTE_PATH = str(ROOT_PATH / "olist.db")


def get_csv_to_table_mapping() -> dict[str, str]:
    """
    Get the mapping between the csv files and the table names

    Returns:
        Dict[str, str]: The dictionary with keys as the csv file names and values as the table names
    """
    return dict(
        [
            ("olist_customers_dataset.csv", "olist_customers"),
            ("olist_geolocation_dataset.csv", "olist_geolocation"),
            ("olist_order_items_dataset.csv", "olist_order_items"),
            ("olist_order_payments_dataset.csv", "olist_order_payments"),
            ("olist_order_reviews_dataset.csv", "olist_order_reviews"),
            ("olist_orders_dataset.csv", "olist_orders"),
            ("olist_products_dataset.csv", "olist_products"),
            ("olist_sellers_dataset.csv", "olist_sellers"),
            (
                "product_category_name_translation.csv",
                "product_category_name_translation",
            ),
        ]
    )
