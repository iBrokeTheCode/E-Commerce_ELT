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

    _Built with [Marimo](https://marimo.io)._

    > 💡 **Want a step-by-step walkthrough instead?**   
    > Check the Jupyter notebook version here: 👉 [Jupyter notebook](https://huggingface.co/spaces/iBrokeTheCode/E-Commerce_ELT/blob/main/tutorial_app.ipynb)
    """
    )
    return


@app.cell
def _():
    # 📌 IMPORT LIBRARIES AND PACKAGES

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
    # 📌 LOAD SQLITE DATABASE

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
    # 📌 RETRIEVE RELEVANT DATA FROM DATABASE

    revenue_by_month_year = query_results[QueryEnum.REVENUE_BY_MONTH_YEAR.value]

    top_10_revenue_categories = query_results[
        QueryEnum.TOP_10_REVENUE_CATEGORIES.value
    ]

    top_10_least_revenue_categories = query_results[
        QueryEnum.TOP_10_LEAST_REVENUE_CATEGORIES.value
    ]

    revenue_per_state = query_results[QueryEnum.REVENUE_PER_STATE.value]

    delivery_date_difference = query_results[
        QueryEnum.DELIVERY_DATE_DIFFERENCE.value
    ]

    real_vs_estimated_delivery_time = query_results[
        QueryEnum.REAL_VS_ESTIMATED_DELIVERED_TIME.value
    ]

    global_amount_order_status = query_results[
        QueryEnum.GLOBAL_AMOUNT_ORDER_STATUS.value
    ]

    orders_per_day_and_holidays = query_results[
        QueryEnum.ORDERS_PER_DAY_AND_HOLIDAYS_2017.value
    ]

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
    mo.Html("<br><hr><br>")
    return


@app.cell
def _(mo):
    mo.md(r"""# 📈 Insights""")
    return


@app.cell
def _(mo):
    # 📌 TODO: Retrieve real data

    st1 = mo.stat(
        label="Total Revenue 2017",
        bordered=True,
        value=f"${2_000_000:,}",
        caption=f"Previous year: ${1_500_000:,}",
        direction="increase",
    )
    st2 = mo.stat(
        label="Successful Deliveries",
        bordered=True,
        value=f"{1_280_700:,}",
        caption="Review chart for more details",
        direction="increase",
    )
    st3 = mo.stat(
        label="Uncompleted Orders",
        bordered=True,
        value=f"{80_700:,}",
        caption="Review chart for more details",
        direction="decrease",
    )
    st4 = mo.stat(
        label="Category with greater revenue",
        bordered=True,
        value=f"{'bed_bath_table'.replace('_', ' ').title()}",
        caption=f"${884_220:,}",
        direction="increase",
    )

    mo.hstack([st1, st2, st3, st4], widths="equal", gap=1)
    return


@app.cell
def _(mo):
    mo.Html("<br><hr><br>")
    return


@app.cell
def _(mo):
    mo.md(r"""# 📋 Tables""")
    return


@app.cell
def _(
    freight_value_weight_relationship,
    global_amount_order_status,
    mo,
    orders_per_day_and_holidays,
    real_vs_estimated_delivery_time,
    revenue_by_month_year,
    revenue_per_state,
    top_10_least_revenue_categories,
    top_10_revenue_categories,
):
    overview_table_tab = mo.vstack(
        align="center",
        justify="center",
        gap=2,
        items=[
            mo.center(mo.md("## Global Order Status Overview")),
            global_amount_order_status,
        ],
    )
    revenue_table_tab = mo.vstack(
        align="center",
        justify="center",
        gap=2,
        items=[
            mo.center(mo.md("## Revenue by Month and Year")),
            revenue_by_month_year,
            mo.center(mo.md("## Revenue by State")),
            revenue_per_state,
        ],
    )
    categories_table_tab = mo.vstack(
        align="center",
        justify="center",
        gap=2,
        items=[
            mo.center(mo.md("## Top 10 Revenue Categories")),
            top_10_revenue_categories,
            mo.center(mo.md("## Bottom 10 Revenue Categories")),
            top_10_least_revenue_categories,
        ],
    )
    delivery_table_tab = mo.vstack(
        align="center",
        justify="center",
        gap=2,
        items=[
            mo.center(mo.md("## Freight Value vs Product Weight")),
            freight_value_weight_relationship,
            mo.center(mo.md("## Real vs Estimated Delivery Time")),
            real_vs_estimated_delivery_time,
            mo.center(mo.md("## Orders and Holidays")),
            orders_per_day_and_holidays,
        ],
    )

    mo.ui.tabs(
        {
            "📊 Overview": overview_table_tab,
            "💰 Revenue": revenue_table_tab,
            "📦 Categories": categories_table_tab,
            "🚚 Freight & Delivery": delivery_table_tab,
        }
    )
    return


@app.cell
def _(mo):
    mo.Html("<br><hr><br>")
    return


@app.cell
def _(mo):
    mo.md(r"""# 📊 Charts""")
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
        align="center",
        justify="center",
        gap=2,
        items=[
            mo.center(mo.md("## Global Order Status Overview")),
            plot_global_amount_order_status(df=global_amount_order_status),
        ],
    )

    revenue_tab = mo.vstack(
        align="center",
        justify="center",
        gap=2,
        items=[
            mo.center(mo.md("## Revenue by Month and Year")),
            plot_revenue_by_month_year(df=revenue_by_month_year, year=2017),
            mo.center(mo.md("## Revenue by State")),
            plot_revenue_per_state(revenue_per_state),
        ],
    )

    categories_tab = mo.vstack(
        align="center",
        justify="center",
        gap=2,
        items=[
            mo.center(mo.md("## Top 10 Revenue Categories")),
            plot_top_10_revenue_categories(top_10_revenue_categories),
            mo.center(mo.md("## Top 10 Revenue Categories by Amount")),
            plot_top_10_revenue_categories_amount(top_10_revenue_categories),
            mo.center(mo.md("## Bottom 10 Revenue Categories")),
            plot_top_10_least_revenue_categories(top_10_least_revenue_categories),
        ],
    )

    delivery_tab = mo.vstack(
        gap=2,
        justify="center",
        align="center",
        heights="equal",
        items=[
            mo.center(mo.md("## Freight Value vs Product Weight")),
            plot_freight_value_weight_relationship(
                freight_value_weight_relationship
            ),
            mo.center(mo.md("## Real vs Estimated Delivery Time")),
            plot_real_vs_predicted_delivered_time(
                df=real_vs_estimated_delivery_time, year=2017
            ),
            mo.center(mo.md("## Orders and Holidays")),
            plot_order_amount_per_day_with_holidays(orders_per_day_and_holidays),
        ],
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


if __name__ == "__main__":
    app.run()
