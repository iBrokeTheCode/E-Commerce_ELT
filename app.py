import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    # /// script
    # [tool.marimo.display]
    # theme = "dark"
    # ///
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# E-Commerce ELT Pipeline""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    💡 Want a step-by-step walkthrough instead?

    You can check the Jupyter notebook version here: 👉 [Jupyter version](https://huggingface.co/spaces/iBrokeTheCode/E-Commerce_ELT/blob/main/tutorial_app.ipynb)
    """
    )
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

    if DB_PATH.exists() and DB_PATH.stat().st_size > 0:
        print("Database found. Skipping ETL process.")
        ENGINE = create_engine(f"sqlite:///{DB_PATH}", echo=False)
    else:
        print("Database not found or empty. Starting ETL process...")
        ENGINE = create_engine(f"sqlite:///{DB_PATH}", echo=False)

        csv_dataframes = extract(
            csv_folder=config.DATASET_ROOT_PATH,
            csv_table_mapping=config.get_csv_to_table_mapping(),
            public_holidays_url=config.PUBLIC_HOLIDAYS_URL,
        )

        load(dataframes=csv_dataframes, database=ENGINE)
        print("ETL process complete.")
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
    mo.md(r"""**A. Revenue by Month and Year**""")
    return


@app.cell
def _(QueryEnum, query_results: "dict[str, DataFrame]"):
    revenue_by_month_year = query_results[QueryEnum.REVENUE_BY_MONTH_YEAR.value]
    revenue_by_month_year
    return (revenue_by_month_year,)


@app.cell
def _(mo):
    mo.md(r"""**B. Top 10 Revenue by categories**""")
    return


@app.cell
def _(QueryEnum, query_results: "dict[str, DataFrame]"):
    top_10_revenue_categories = query_results[
        QueryEnum.TOP_10_REVENUE_CATEGORIES.value
    ]
    top_10_revenue_categories
    return (top_10_revenue_categories,)


@app.cell
def _(mo):
    mo.md(r"""**C. Top 10 Least Revenue by Categories**""")
    return


@app.cell
def _(QueryEnum, query_results: "dict[str, DataFrame]"):
    top_10_least_revenue_categories = query_results[
        QueryEnum.TOP_10_LEAST_REVENUE_CATEGORIES.value
    ]
    top_10_least_revenue_categories
    return (top_10_least_revenue_categories,)


@app.cell
def _(mo):
    mo.md(r"""**D. Revenue per State**""")
    return


@app.cell
def _(QueryEnum, query_results: "dict[str, DataFrame]"):
    revenue_per_state = query_results[QueryEnum.REVENUE_PER_STATE.value]
    revenue_per_state
    return (revenue_per_state,)


@app.cell
def _(mo):
    mo.md(r"""**E. Delivery Date Difference**""")
    return


@app.cell
def _(QueryEnum, query_results: "dict[str, DataFrame]"):
    delivery_date_difference = query_results[
        QueryEnum.DELIVERY_DATE_DIFFERENCE.value
    ]
    delivery_date_difference
    return (delivery_date_difference,)


@app.cell
def _(mo):
    mo.md(r"""**F. Real vs. Predicted Delivered Time**""")
    return


@app.cell
def _(QueryEnum, query_results: "dict[str, DataFrame]"):
    real_vs_estimated_delivery_time = query_results[
        QueryEnum.REAL_VS_ESTIMATED_DELIVERED_TIME.value
    ]
    real_vs_estimated_delivery_time
    return (real_vs_estimated_delivery_time,)


@app.cell
def _(mo):
    mo.md(r"""**G. Global Amount of Order Status**""")
    return


@app.cell
def _(QueryEnum, query_results: "dict[str, DataFrame]"):
    global_amount_order_status = query_results[
        QueryEnum.GLOBAL_AMOUNT_ORDER_STATUS.value
    ]
    global_amount_order_status
    return (global_amount_order_status,)


@app.cell
def _(mo):
    mo.md(r"""**H. Orders per Day and Holidays in 2017**""")
    return


@app.cell
def _(QueryEnum, query_results: "dict[str, DataFrame]"):
    orders_per_day_and_holidays = query_results[
        QueryEnum.ORDERS_PER_DAY_AND_HOLIDAYS_2017.value
    ]
    orders_per_day_and_holidays
    return (orders_per_day_and_holidays,)


@app.cell
def _(mo):
    mo.md(r"""**I. Freight Value Weight Relationship**""")
    return


@app.cell
def _(QueryEnum, query_results: "dict[str, DataFrame]"):
    freight_value_weight_relationship = query_results[
        QueryEnum.GET_FREIGHT_VALUE_WEIGHT_RELATIONSHIP.value
    ]
    freight_value_weight_relationship
    return (freight_value_weight_relationship,)


@app.cell
def _(mo):
    mo.md(r"""## 3. Plots""")
    return


@app.cell
def _():
    from src.plots import (
        plot_revenue_by_month_year,
        plot_real_vs_predicted_delivered_time,
        plot_global_amount_order_status,
        plot_revenue_per_state,
        plot_top_10_least_revenue_categories,
        plot_top_10_revenue_categories_amount,
        plot_top_10_revenue_categories,
        plot_freight_value_weight_relationship,
        plot_delivery_date_difference,
        plot_order_amount_per_day_with_holidays,
    )
    return (
        plot_delivery_date_difference,
        plot_freight_value_weight_relationship,
        plot_global_amount_order_status,
        plot_order_amount_per_day_with_holidays,
        plot_real_vs_predicted_delivered_time,
        plot_revenue_by_month_year,
        plot_revenue_per_state,
        plot_top_10_least_revenue_categories,
        plot_top_10_revenue_categories,
        plot_top_10_revenue_categories_amount,
    )


@app.cell
def _(mo):
    mo.md(r"""**A. Revenue by Month in 2017**""")
    return


@app.cell
def _(plot_revenue_by_month_year, revenue_by_month_year):
    plot_revenue_by_month_year(df=revenue_by_month_year, year=2017)
    return


@app.cell
def _(mo):
    mo.md(r"""**B. Real vs. Predicted Delivered Time**""")
    return


@app.cell
def _(plot_real_vs_predicted_delivered_time, real_vs_estimated_delivery_time):
    plot_real_vs_predicted_delivered_time(
        df=real_vs_estimated_delivery_time, year=2017
    )
    return


@app.cell
def _(mo):
    mo.md(r"""**C. Global Amount of Order Status**""")
    return


@app.cell
def _(global_amount_order_status, plot_global_amount_order_status):
    plot_global_amount_order_status(df=global_amount_order_status)
    return


@app.cell
def _(mo):
    mo.md(r"""**D. Revenue per State**""")
    return


@app.cell
def _(plot_revenue_per_state, revenue_per_state):
    plot_revenue_per_state(df=revenue_per_state)
    return


@app.cell
def _(mo):
    mo.md(r"""**E. Top 10 Least Revenue by Categories**""")
    return


@app.cell
def _(plot_top_10_least_revenue_categories, top_10_least_revenue_categories):
    plot_top_10_least_revenue_categories(df=top_10_least_revenue_categories)
    return


@app.cell
def _(mo):
    mo.md(r"""**F. Top 10 Revenue Categories Amount**""")
    return


@app.cell
def _(plot_top_10_revenue_categories_amount, top_10_revenue_categories):
    plot_top_10_revenue_categories_amount(df=top_10_revenue_categories)
    return


@app.cell
def _(mo):
    mo.md(r"""**G. Top 10 Revenue by Categories**""")
    return


@app.cell
def _(plot_top_10_revenue_categories, top_10_revenue_categories):
    plot_top_10_revenue_categories(df=top_10_revenue_categories)
    return


@app.cell
def _(mo):
    mo.md(r"""**H. Freight Value vs. Product Weight**""")
    return


@app.cell
def _(
    freight_value_weight_relationship,
    plot_freight_value_weight_relationship,
):
    plot_freight_value_weight_relationship(df=freight_value_weight_relationship)
    return


@app.cell
def _(mo):
    mo.md(r"""**I. Diffrence Between Deliver Estimated Date and Delivery Date**""")
    return


@app.cell
def _(delivery_date_difference, plot_delivery_date_difference):
    plot_delivery_date_difference(df=delivery_date_difference)
    return


@app.cell
def _(mo):
    mo.md(r"""**J. Order Amount per Day with Holidays**""")
    return


@app.cell
def _(orders_per_day_and_holidays, plot_order_amount_per_day_with_holidays):
    plot_order_amount_per_day_with_holidays(df=orders_per_day_and_holidays)
    return


if __name__ == "__main__":
    app.run()
