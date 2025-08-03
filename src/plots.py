import matplotlib.pyplot as plt
import plotly.express as px
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


def plot_real_vs_predicted_delivered_time(df: DataFrame, year: int) -> None:
    """
    Plot the real vs predicted delivered time

    Args:
        df (DataFrame): The dataframe
        year (int): The year
    """
    rc_file_defaults()
    sns.set_style(style=None, rc=None)

    _, ax1 = plt.subplots(figsize=(12, 6))

    sns.lineplot(data=df[f"Year{year}_real_time"], marker="o", sort=False, ax=ax1)
    ax1.twinx()
    g = sns.lineplot(
        data=df[f"Year{year}_estimated_time"], marker="o", sort=False, ax=ax1
    )
    g.set_xticks(range(len(df)))
    g.set_xticklabels(df.month.values)
    g.set(xlabel="month", ylabel="Average days delivery time", title="some title")
    ax1.set_title(f"Average days delivery time by month in {year}")
    ax1.legend(["Real time", "Estimated time"])

    plt.show()


def plot_global_amount_order_status(df: DataFrame) -> None:
    """
    Plot global amount of order status

    Args:
        df (DataFrame): The dataframe
    """
    _, ax = plt.subplots(figsize=(8, 3), subplot_kw=dict(aspect="equal"))

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

    my_circle = plt.Circle((0, 0), 0.7, color="white")
    p = plt.gcf()
    p.gca().add_artist(my_circle)

    plt.show()


def plot_revenue_per_state(df: DataFrame) -> None:
    """
    Plot revenue per state

    Args:
        df (DataFrame): The dataframe
    """
    fig = px.treemap(
        df, path=["customer_state"], values="Revenue", width=800, height=300
    )
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    fig.show()


def plot_top_10_least_revenue_categories(df: DataFrame) -> None:
    """
    Plot top 10 least revenue categories

    Args:
        df (DataFrame): The dataframe
    """
    _, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

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
    my_circle = plt.Circle((0, 0), 0.7, color="white")
    p = plt.gcf()
    p.gca().add_artist(my_circle)

    ax.set_title("Top 10 Least Revenue Categories Amount")

    plt.show()


def plot_top_10_revenue_categories_amount(df: DataFrame) -> None:
    """Plot top 10 revenue categories

    Args:
        df (DataFrame): Dataframe with top 10 revenue categories query result
    """
    # Plotting the top 10 revenue categories amount
    _, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

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
    my_circle = plt.Circle((0, 0), 0.7, color="white")
    p = plt.gcf()
    p.gca().add_artist(my_circle)

    ax.set_title("Top 10 Revenue Categories Amount")

    plt.show()


def plot_top_10_revenue_categories(df: DataFrame) -> None:
    """Plot top 10 revenue categories

    Args:
        df (DataFrame): Dataframe with top 10 revenue categories query result
    """
    fig = px.treemap(df, path=["Category"], values="Num_order", width=800, height=400)
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    fig.show()


def plot_freight_value_weight_relationship(df: DataFrame) -> None:
    """Plot freight value weight relationship

    Args:
        df (DataFrame): Dataframe with freight value weight relationship query result
    """
    # Set the figure size
    plt.figure(figsize=(8, 4))

    # Scatter plot: x=product weight, y=freight value
    sns.scatterplot(
        data=df,
        x="product_weight_g",
        y="freight_value",
        edgecolor="white",
    )

    # Customize chart
    plt.title("Freight Value vs Product Weight")
    plt.xlabel("Product Weight (g)")
    plt.ylabel("Freight Value ($)")
    plt.tight_layout()
    plt.show()


def plot_delivery_date_difference(df: DataFrame) -> None:
    """Plot delivery date difference

    Args:
        df (DataFrame): Dataframe with delivery date difference query result
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x="Delivery_Difference", y="State").set(
        title="Difference Between Delivery Estimate Date and Delivery Date"
    )
    plt.show()


def plot_order_amount_per_day_with_holidays(df: DataFrame) -> None:
    """Plot order amount per day with holidays

    Args:
        df (DataFrame): Dataframe with order amount per day with holidays query result
    """

    # Convert timestamp in milliseconds to datetime
    df["date"] = to_datetime(df["date"], unit="ms")

    # Sort by date
    df = df.sort_values("date")

    # Plot the line chart for order count
    plt.figure(figsize=(9, 4))
    plt.plot(df["date"], df["order_count"], color="green")

    # Add vertical lines for holidays
    holidays = df[df["holiday"] == True]
    for holiday_date in holidays["date"]:
        plt.axvline(holiday_date, color="blue", linestyle="dotted", alpha=0.6)

    # Customize chart
    plt.title("Order Amount per Day with Holidays")
    plt.xlabel("Date")
    plt.ylabel("Order Count")
    plt.tight_layout()
    plt.show()
