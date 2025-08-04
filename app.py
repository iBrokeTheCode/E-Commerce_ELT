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
    mo.md(r"""# 📦 Brazilian E-Commerce Dashboard""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    This interactive dashboard explores insights from the [Brazilian e-commerce dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) and the [Public Holiday API](https://date.nager.at/Api) :
    - Sales performance by category and state
    - Delivery efficiency
    - Seasonal trends and holidays impact

    Use the tabs above to explore different insights!

    _Built with Marimo._

    ---

    💡 **Want a step-by-step walkthrough instead?**

    You can check the Jupyter notebook version here: 👉 [Jupyter notebook](https://huggingface.co/spaces/iBrokeTheCode/E-Commerce_ELT/blob/main/tutorial_app.ipynb)
    """
    )
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
        DataFrame,
        Path,
        QueryEnum,
        config,
        create_engine,
        extract,
        load,
        plot_freight_value_weight_relationship,
        plot_global_amount_order_status,
        plot_order_amount_per_day_with_holidays,
        plot_real_vs_predicted_delivered_time,
        plot_revenue_by_month_year,
        plot_revenue_per_state,
        plot_top_10_least_revenue_categories,
        plot_top_10_revenue_categories,
        plot_top_10_revenue_categories_amount,
        run_queries,
    )


@app.cell
def _(DataFrame, Path, config, create_engine, extract, load, run_queries):
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

    query_results: dict[str, DataFrame] = run_queries(database=ENGINE)
    return (query_results,)


@app.cell
def _(QueryEnum, query_results: "dict[str, DataFrame]"):
    # **A. Revenue by Month and Year**
    revenue_by_month_year = query_results[QueryEnum.REVENUE_BY_MONTH_YEAR.value]

    # **B. Top 10 Revenue by categories**
    top_10_revenue_categories = query_results[
        QueryEnum.TOP_10_REVENUE_CATEGORIES.value
    ]

    # **C. Top 10 Least Revenue by Categories**
    top_10_least_revenue_categories = query_results[
        QueryEnum.TOP_10_LEAST_REVENUE_CATEGORIES.value
    ]

    # **D. Revenue per State**
    revenue_per_state = query_results[QueryEnum.REVENUE_PER_STATE.value]

    # **E. Delivery Date Difference**
    delivery_date_difference = query_results[
        QueryEnum.DELIVERY_DATE_DIFFERENCE.value
    ]

    # **F. Real vs. Predicted Delivered Time**
    real_vs_estimated_delivery_time = query_results[
        QueryEnum.REAL_VS_ESTIMATED_DELIVERED_TIME.value
    ]

    # **G. Global Amount of Order Status**
    global_amount_order_status = query_results[
        QueryEnum.GLOBAL_AMOUNT_ORDER_STATUS.value
    ]

    # **H. Orders per Day and Holidays in 2017**
    orders_per_day_and_holidays = query_results[
        QueryEnum.ORDERS_PER_DAY_AND_HOLIDAYS_2017.value
    ]

    # **I. Freight Value Weight Relationship**
    freight_value_weight_relationship = query_results[
        QueryEnum.GET_FREIGHT_VALUE_WEIGHT_RELATIONSHIP.value
    ]
    return (
        freight_value_weight_relationship,
        global_amount_order_status,
        orders_per_day_and_holidays,
        real_vs_estimated_delivery_time,
        revenue_by_month_year,
        revenue_per_state,
        top_10_least_revenue_categories,
        top_10_revenue_categories,
    )


@app.cell
def _(mo):
    mo.md(r"""## Insights""")
    return


@app.cell
def _(
    freight_value_weight_relationship,
    global_amount_order_status,
    mo,
    orders_per_day_and_holidays,
    plot_freight_value_weight_relationship,
    plot_global_amount_order_status,
    plot_order_amount_per_day_with_holidays,
    plot_real_vs_predicted_delivered_time,
    plot_revenue_by_month_year,
    plot_revenue_per_state,
    plot_top_10_least_revenue_categories,
    plot_top_10_revenue_categories,
    plot_top_10_revenue_categories_amount,
    real_vs_estimated_delivery_time,
    revenue_by_month_year,
    revenue_per_state,
    top_10_least_revenue_categories,
    top_10_revenue_categories,
):
    overview_tab = mo.vstack(
        [
            mo.md("### Global Order Status Overview"),
            mo.hstack(
                [
                    global_amount_order_status,
                    plot_global_amount_order_status(df=global_amount_order_status),
                ]
            ),
        ]
    )

    revenue_tab = mo.vstack(
        [
            mo.md("### Revenue by Month and Year"),
            mo.ui.table(revenue_by_month_year),
            plot_revenue_by_month_year(df=revenue_by_month_year, year=2017),
            mo.md("### Revenue by State"),
            mo.ui.table(revenue_per_state),
            plot_revenue_per_state(revenue_per_state),
        ]
    )

    categories_tab = mo.vstack(
        [
            mo.md("### Top 10 Revenue Categories"),
            mo.ui.table(top_10_revenue_categories),
            plot_top_10_revenue_categories(top_10_revenue_categories),
            plot_top_10_revenue_categories_amount(top_10_revenue_categories),
            mo.md("### Bottom 10 Revenue Categories"),
            mo.ui.table(top_10_least_revenue_categories),
            plot_top_10_least_revenue_categories(top_10_least_revenue_categories),
        ]
    )

    delivery_tab = mo.vstack(
        [
            mo.md("### Freight Value vs Product Weight"),
            mo.ui.table(freight_value_weight_relationship),
            plot_freight_value_weight_relationship(
                freight_value_weight_relationship
            ),
            mo.md("### Real vs Estimated Delivery Time"),
            mo.ui.table(real_vs_estimated_delivery_time),
            plot_real_vs_predicted_delivered_time(
                df=real_vs_estimated_delivery_time, year=2017
            ),
            mo.md("### Orders and Holidays"),
            mo.ui.table(orders_per_day_and_holidays),
            plot_order_amount_per_day_with_holidays(orders_per_day_and_holidays),
        ]
    )
    return categories_tab, delivery_tab, overview_tab, revenue_tab


@app.cell
def _(categories_tab, delivery_tab, mo, overview_tab, revenue_tab):
    mo.ui.tabs(
        {
            "📊 Overview": overview_tab,
            "💰 Revenue": revenue_tab,
            "📦 Categories": categories_tab,
            "🚚 Freight & Delivery": delivery_tab,
        }
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
