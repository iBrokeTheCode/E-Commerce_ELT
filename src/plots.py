import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
from matplotlib import rc_file_defaults
from matplotlib.figure import Figure
from pandas import DataFrame, to_datetime


def plot_revenue_by_month_year(df: DataFrame, year: int) -> Figure:
    """
    Generate and return a matplotlib figure showing monthly revenue for a given year.

    Designed to be used in interactive environments like Marimo, where the figure
    will be rendered automatically when returned from a code cell.

    Args:
        df (DataFrame): DataFrame containing revenue data, with a column 'month'
                        and a column named 'Year{year}' for the selected year.
        year (int): The year to visualize (e.g., 2018).

    Returns:
        Figure: A matplotlib figure object with a line and bar chart overlay.
    """
    rc_file_defaults()
    sns.set_style(style="darkgrid", rc=None)

    fig, ax1 = plt.subplots(figsize=(12, 6))

    sns.lineplot(data=df[f"Year{year}"], marker="o", sort=False, ax=ax1)
    ax2 = ax1.twinx()
    sns.barplot(data=df, x="month", y=f"Year{year}", alpha=0.5, ax=ax2)

    ax1.set_title(f"Revenue by month in {year}")

    return fig


def plot_real_vs_predicted_delivered_time(df: DataFrame, year: int) -> Figure:
    """
    Generate and return a matplotlib figure comparing real vs. estimated delivery time
    by month for a specific year.

    Intended for interactive environments like Marimo where returning the figure
    automatically renders the plot.

    Args:
        df (DataFrame): DataFrame with columns:
            - 'month': Month names or numbers.
            - f'Year{year}_real_time': Real average delivery time.
            - f'Year{year}_estimated_time': Estimated average delivery time.
        year (int): The year to visualize (e.g., 2018).

    Returns:
        Figure: A matplotlib figure with two overlaid line plots.
    """
    rc_file_defaults()
    sns.set_style(style=None, rc=None)

    fig, ax1 = plt.subplots(figsize=(12, 6))

    sns.lineplot(data=df[f"Year{year}_real_time"], marker="o", sort=False, ax=ax1)
    sns.lineplot(data=df[f"Year{year}_estimated_time"], marker="o", sort=False, ax=ax1)

    ax1.set_xticks(range(len(df)))
    ax1.set_xticklabels(df["month"].values)
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Average Days to Deliver")
    ax1.set_title(f"Average Delivery Time (Real vs Estimated) in {year}")
    ax1.legend(["Real Time", "Estimated Time"])

    return fig


from matplotlib.figure import Figure
from pandas import DataFrame


def plot_global_amount_order_status(df: DataFrame) -> Figure:
    """
    Create and return a donut pie chart showing the global amount per order status.

    Args:
        df (DataFrame): DataFrame containing:
            - 'order_status': Status labels (e.g., 'order delivered').
            - 'Amount': Corresponding counts or totals per status.

    Returns:
        Figure: A matplotlib figure containing a pie (donut) chart with legend.
    """
    fig, ax = plt.subplots(figsize=(8, 3), subplot_kw=dict(aspect="equal"))

    # Extract last word of each status for cleaner labels
    elements = [x.split()[-1] for x in df["order_status"]]

    wedges, autotexts = ax.pie(df["Amount"], textprops=dict(color="w"))

    ax.legend(
        wedges,
        elements,
        title="Order Status",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
    )

    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title("Order Status Total")

    # Add donut center
    center_circle = plt.Circle((0, 0), 0.7, color="white")
    ax.add_artist(center_circle)

    return fig


def plot_revenue_per_state(df: DataFrame) -> go.Figure:
    """
    Create a Plotly treemap to visualize revenue per customer state.

    Args:
        df (DataFrame): DataFrame with columns:
            - 'customer_state': State or region
            - 'Revenue': Revenue value per state

    Returns:
        go.Figure: A Plotly treemap figure object.
    """
    fig = px.treemap(
        df, path=["customer_state"], values="Revenue", width=800, height=300
    )
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    return fig


def plot_top_10_least_revenue_categories(df: DataFrame) -> Figure:
    """
    Create a donut pie chart showing the top 10 least revenue categories.

    Args:
        df (DataFrame): DataFrame with columns:
            - 'Category': Category name
            - 'Revenue': Corresponding revenue values

    Returns:
        Figure: A matplotlib figure with a donut chart and legend.
    """
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    elements = [x.split()[-1] for x in df["Category"]]
    revenue = df["Revenue"]

    wedges, autotexts = ax.pie(revenue, textprops=dict(color="w"))

    ax.legend(
        wedges,
        elements,
        title="Top 10 Revenue Categories",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
    )

    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title("Top 10 Least Revenue Categories Amount")

    center_circle = plt.Circle((0, 0), 0.7, color="white")
    ax.add_artist(center_circle)

    return fig


def plot_top_10_revenue_categories_amount(df: DataFrame) -> Figure:
    """
    Create a donut pie chart showing the revenue distribution of the top 10 categories.

    Args:
        df (DataFrame): DataFrame with columns:
            - 'Category': Category name
            - 'Revenue': Revenue amount

    Returns:
        Figure: A matplotlib figure object.
    """
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    elements = [x.split()[-1] for x in df["Category"]]
    revenue = df["Revenue"]

    wedges, autotexts = ax.pie(revenue, textprops=dict(color="w"))

    ax.legend(
        wedges,
        elements,
        title="Top 10 Revenue Categories",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
    )

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title("Top 10 Revenue Categories Amount")

    center_circle = plt.Circle((0, 0), 0.7, color="white")
    ax.add_artist(center_circle)

    return fig


def plot_top_10_revenue_categories(df: DataFrame) -> go.Figure:
    """
    Create a Plotly treemap showing the number of orders for the top 10 revenue categories.

    Args:
        df (DataFrame): DataFrame with columns:
            - 'Category': Category name
            - 'Num_order': Number of orders per category

    Returns:
        go.Figure: A Plotly treemap figure object.
    """
    fig = px.treemap(df, path=["Category"], values="Num_order", width=800, height=400)
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    return fig


def plot_freight_value_weight_relationship(df: DataFrame) -> Figure:
    """
    Plot the relationship between product weight and freight value using a scatter plot.

    Args:
        df (DataFrame): DataFrame with columns:
            - 'product_weight_g': Weight of the product in grams
            - 'freight_value': Freight value in dollars

    Returns:
        Figure: A matplotlib figure object.
    """
    fig, ax = plt.subplots(figsize=(8, 4))

    sns.scatterplot(
        data=df, x="product_weight_g", y="freight_value", edgecolor="white", ax=ax
    )

    ax.set_title("Freight Value vs Product Weight")
    ax.set_xlabel("Product Weight (g)")
    ax.set_ylabel("Freight Value ($)")
    fig.tight_layout()

    return fig


def plot_delivery_date_difference(df: DataFrame) -> Figure:
    """
    Plot the difference between estimated and actual delivery dates, grouped by state.

    Args:
        df (DataFrame): DataFrame with columns:
            - 'Delivery_Difference': Difference in days
            - 'State': Destination state

    Returns:
        Figure: A matplotlib figure object.
    """
    fig, ax = plt.subplots(figsize=(12, 6))

    sns.barplot(data=df, x="Delivery_Difference", y="State", ax=ax)
    ax.set_title("Difference Between Delivery Estimate Date and Delivery Date")
    ax.set_xlabel("Delivery Difference (days)")
    ax.set_ylabel("State")

    fig.tight_layout()
    return fig


def plot_order_amount_per_day_with_holidays(df: DataFrame) -> Figure:
    """
    Plot the number of orders per day, highlighting holidays with vertical lines.

    Args:
        df (DataFrame): DataFrame with columns:
            - 'date': Timestamp in milliseconds
            - 'order_count': Number of orders on that date
            - 'holiday': Boolean indicating if the date is a holiday

    Returns:
        Figure: A matplotlib figure object.
    """
    df = df.copy()
    df["date"] = to_datetime(df["date"], unit="ms")
    df = df.sort_values("date")

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(df["date"], df["order_count"], color="green")

    for holiday_date in df[df["holiday"]]["date"]:
        ax.axvline(holiday_date, color="blue", linestyle="dotted", alpha=0.6)

    ax.set_title("Order Amount per Day with Holidays")
    ax.set_xlabel("Date")
    ax.set_ylabel("Order Count")
    fig.tight_layout()

    return fig
