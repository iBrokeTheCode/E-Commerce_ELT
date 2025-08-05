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
    mo.center(mo.md("# 📦 Brazilian E-Commerce Dashboard"))
    return


@app.cell
def _(mo):
    mo.Html("<br><hr><br>")
    return


@app.cell
def _(mo):
    description = mo.md(r"""### 🛍️ About the Dataset   

    This dashboard presents insights from the real-world [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), which includes data on over **100,000 orders** placed between **2016 and 2018** across various online marketplaces in Brazil. It also integrates data from the [Public Holiday API](https://date.nager.at/Api) to analyze sales performance during national holidays.

    The dataset offers a detailed view of the e-commerce experience, including:

    * Order status, prices, and payment types
    * Freight and delivery performance
    * Customer locations and product categories
    * Customer reviews and satisfaction
    """)

    erd_diagram = mo.md("""### Entity Relationship Diagram
    <img src="public/erd-schema.png" />
    """)

    stack = mo.md(r"""### 🧑‍💻 Stack
    - [Marimo](https://github.com/marimo-team/marimo): A Python library for building interactive dashboards.
    - [Hugging Face Spaces](https://huggingface.co/docs/hub/spaces-config-reference): A platform for hosting and sharing interactive machine learning demos and applications.
    - [Pandas](https://pandas.pydata.org/): A Python library for data manipulation and analysis.
    - [Plotly](https://plotly.com/python/): A Python library for interactive data visualization.
    - [Matplotlib](https://matplotlib.org/): A Python library for creating static, animated, and interactive visualizations.
    - [Seaborn](https://seaborn.pydata.org/): A Python library for creating statistical graphics.
    - [SQLAlchemy](https://www.sqlalchemy.org/): A Python library for interacting with databases.
    - [Requests](https://requests.readthedocs.io/en/latest/): A Python library for making HTTP requests.
    - [Ruff](https://github.com/charliermarsh/ruff): An extremely fast Python linter and code formatter, written in Rust.
    - [uv](https://github.com/astral-sh/uv): An extremely fast Python package and project manager, written in Rust.

    """)

    mo.carousel(items=[description, erd_diagram, stack])
    return


@app.cell
def _():
    # 📌 IMPORT LIBRARIES AND PACKAGES

    from pathlib import Path

    from pandas import DataFrame
    from sqlalchemy import create_engine

    from src import config
    from src.extract import extract
    from src.load import load
    from src.plots import (
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
    from src.transform import QueryEnum, run_queries
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
def _(
    global_amount_order_status,
    revenue_by_month_year,
    top_10_revenue_categories,
):
    # 📌 RETRIEVE INSIGHTS VALUES

    # [1]
    total_2018 = revenue_by_month_year["Year2018"].sum()
    total_2017 = revenue_by_month_year["Year2017"].sum()

    # [2]
    delivered = global_amount_order_status.loc[
        global_amount_order_status["order_status"] == "delivered", "Amount"
    ].values[0]

    # Get total number of orders and delivery rate as a percentage string
    total_orders = global_amount_order_status["Amount"].sum()
    delivery_rate = delivered / total_orders
    percentage = f"{delivery_rate:.1%}"  # e.g., '85.2%'

    # [3]
    # Uncompleted orders = total - delivered
    uncompleted = total_orders - delivered
    uncompleted_pct = f"{(uncompleted / total_orders) * 100:.1f}%"

    # [4]
    top_cat = top_10_revenue_categories.iloc[0]

    cat_name = top_cat["Category"].replace("_", " ").title()
    cat_num_orders = int(top_cat["Num_order"])
    cat_revenue = top_cat["Revenue"]
    return (
        cat_name,
        cat_num_orders,
        cat_revenue,
        delivered,
        percentage,
        total_2017,
        total_2018,
        uncompleted,
        uncompleted_pct,
    )


@app.cell
def _(
    cat_name,
    cat_num_orders,
    cat_revenue,
    delivered,
    mo,
    percentage,
    total_2017,
    total_2018,
    uncompleted,
    uncompleted_pct,
):
    # 📌 DISPLAY INSIGHTS

    stat1 = mo.stat(
        label="Total Revenue 2018",
        bordered=True,
        value=f"${total_2018:,.0f}",
        caption=f"Previous year: ${total_2017:,.0f}",
        direction="increase" if total_2018 > total_2017 else "decrease",
    )

    stat2 = mo.stat(
        label="Successful Deliveries",
        bordered=True,
        value=f"{delivered:,}",
        caption=f"{percentage} of total orders",
        direction="increase",
    )

    stat3 = mo.stat(
        label="Uncompleted Orders",
        bordered=True,
        value=f"{uncompleted:,}",
        caption=f"{uncompleted_pct} of total orders",
        direction="decrease",
    )

    stat4 = mo.stat(
        label="Category with greater revenue",
        bordered=True,
        value=cat_name,
        caption=f"{cat_num_orders:,} orders • Revenue: ${cat_revenue:,.0f}",
        direction="increase",
    )

    mo.hstack([stat1, stat2, stat3, stat4], widths="equal", gap=1)
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
            mo.center(mo.md("## Real vs Estimated Delivery Time")),
            plot_real_vs_predicted_delivered_time(
                df=real_vs_estimated_delivery_time, year=2017
            ),
            mo.center(mo.md("## Freight Value vs Product Weight")),
            plot_freight_value_weight_relationship(
                freight_value_weight_relationship
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
            mo.center(mo.md("## Real vs Estimated Delivery Time")),
            real_vs_estimated_delivery_time,
            mo.center(mo.md("## Freight Value vs Product Weight")),
            freight_value_weight_relationship,
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
    mo.callout(
        kind="info",
        value=mo.md(
            """💡 **Want a step-by-step walkthrough instead?**   
    Check the Jupyter notebook version here: 👉 [Jupyter notebook](https://huggingface.co/spaces/iBrokeTheCode/E-Commerce_ELT/blob/main/tutorial_app.ipynb)""",
        ),
    )
    return


@app.cell
def _(mo):
    mo.Html("<br><hr><br>")

    return


@app.cell
def _(mo):
    mo.center(
        mo.md(
            "**Connect with me:** 💼 [Linkedin](https://www.linkedin.com/in/alex-turpo/) • 🐱 [GitHub](https://github.com/iBrokeTheCode) • 🤗 [Hugging Face](https://huggingface.co/iBrokeTheCode)"
        )
    )
    return


if __name__ == "__main__":
    app.run()
