from pandas import DataFrame
from sqlalchemy.engine.base import Engine


def load(dataframes: dict[str, DataFrame], database: Engine) -> None:
    """
    Load the dataframes into the database

    Args:
        dataframes (dict[str, DataFrame]): The dataframes to load
        database (Engine): The database to load the dataframes into

    Returns:
        None
    """
    for table_name, dataframe in dataframes.items():
        dataframe.to_sql(table_name, database, if_exists="replace")
