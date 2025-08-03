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
def _(mo):
    mo.md(r"""### 2.1 Extract and Load""")
    return


@app.cell
def _(Path, config, create_engine, extract, load):
    DB_PATH = Path(config.SQLITE_DB_ABSOLUTE_PATH)

    if not DB_PATH.is_file():
        print("Database not found. Starting ETL process...")
        DB_PATH.touch()

        ENGINE = create_engine(f"sqlite:///{DB_PATH}", echo=False)

        csv_dataframes = extract(
            csv_folder=config.DATASET_ROOT_PATH,
            csv_table_mapping=config.get_csv_to_table_mapping(),
            public_holidays_url=config.PUBLIC_HOLIDAYS_URL,
        )

        load(dataframes=csv_dataframes, database=ENGINE)
        print("ETL process complete.")
    else:
        print("Database found. Skipping ETL process.")
        ENGINE = create_engine(f"sqlite:///{DB_PATH}", echo=False)
    return (ENGINE,)


@app.cell
def _(mo):
    mo.md(r"""### 2.2 Transform""")
    return


@app.cell
def _(DataFrame, ENGINE, run_queries):
    query_results: dict[str, DataFrame] = run_queries(database=ENGINE)
    return (query_results,)


@app.cell
def _(mo):
    mo.md(r"""#### 2.2.1 Revenue by Month and Year""")
    return


@app.cell
def _(QueryEnum, query_results: "dict[str, DataFrame]"):
    revenue_by_month_year = query_results[QueryEnum.REVENUE_BY_MONTH_YEAR.value]
    revenue_by_month_year
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
