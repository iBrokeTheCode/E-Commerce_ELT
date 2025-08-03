import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# E-Commerce ELT Pipeline""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Table of Contents""")
    return


@app.cell
def _(mo):
    mo.md(r"""1. [Description](#1-description)""")
    return


@app.cell
def _(mo):
    mo.md(r"""## 1. Description""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    This project analyzes e-commerce data from a Brazilian marketplace to explore key business metrics related to **revenue** and **delivery performance**. Using an interactive Marimo application, the analysis provides insights into:

    * **Revenue:** Annual revenue, popular product categories, and sales by state.
    * **Delivery:** Delivery performance, including time-to-delivery and its correlation with public holidays.

    The data pipeline processes information from multiple CSV files and a public API, storing and analyzing the results using Python. The final interactive report is presented as a Hugging Face Space built with Marimo.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## 2. ETL""")
    return


@app.cell
def _():
    from pandas import DataFrame
    from pathlib import Path
    from sqlalchemy import create_engine


    from src import config
    from src.extract import extract
    from src.load import load
    from src.transform import QueryEnum, run_queries
    return (
        DataFrame,
        Path,
        QueryEnum,
        config,
        create_engine,
        extract,
        load,
        run_queries,
    )


@app.cell
def _(Path, config, create_engine):
    # Create the sqlite database
    Path(config.SQLITE_DB_ABSOLUTE_PATH).touch()

    # Create the database connection
    ENGINE = create_engine(
        r"sqlite:///{}".format(config.SQLITE_DB_ABSOLUTE_PATH), echo=False
    )
    return (ENGINE,)


@app.cell
def _(mo):
    mo.md(r"""### 2.1 Extract""")
    return


@app.cell
def _(config, extract):
    csv_folder = config.DATASET_ROOT_PATH
    public_holidays_url = config.PUBLIC_HOLIDAYS_URL

    # Get the mapping of the csv files to the table names
    csv_table_mapping = config.get_csv_to_table_mapping()

    # Extract the data from the csv files, holidays and load them into the dataframes
    csv_dataframes = extract(
        csv_folder=csv_folder,
        csv_table_mapping=csv_table_mapping,
        public_holidays_url=public_holidays_url,
    )
    return (csv_dataframes,)


@app.cell
def _(mo):
    mo.md(r"""### 2.2 Load""")
    return


@app.cell
def _(ENGINE, csv_dataframes, load):
    # Store dataframes in SQLite database (our Data Warehouse in this case)
    load(dataframes=csv_dataframes, database=ENGINE)
    return


@app.cell
def _(mo):
    mo.md(r"""### 2.3 Transform""")
    return


@app.cell
def _(DataFrame, ENGINE, run_queries):
    query_results: dict[str, DataFrame] = run_queries(database=ENGINE)
    return (query_results,)


@app.cell
def _(QueryEnum, query_results: "dict[str, DataFrame]"):
    # Transforming the revenue_by_month_year query to a table
    revenue_by_month_year = query_results[QueryEnum.REVENUE_BY_MONTH_YEAR.value]
    revenue_by_month_year
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
