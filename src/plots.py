import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
from matplotlib import rc_file_defaults
from matplotlib.figure import Figure
from pandas import DataFrame, to_datetime

from src.utils.theme import apply_custom_palette, custom_palette


def plot_revenue_by_month_year(df: DataFrame, year: int) -> Figure:
    """
    Generate a matplotlib figure showing monthly revenue for a given year,
    using consistent color styling.
    """

    # Set the theme
    apply_custom_palette()

    # Clear any previous settings and set seaborn style
    sns.set_style("whitegrid")

    fig, ax1 = plt.subplots(figsize=(12, 4))

    # Line plot for revenue trend
    sns.lineplot(
        data=df[f"Year{year}"],
        marker="o",
        sort=False,
        linewidth=2,
        ax=ax1,
        label=f"Line: Revenue {year}",
    )

    # Bar plot with light transparency
    ax2 = ax1.twinx()
    sns.barplot(
        data=df,
        x="month",
        y=f"Year{year}",
        alpha=0.4,
        ax=ax2,
        label=f"Bar: Revenue {year}",
    )

    # Beautify axes
    ax1.set_ylabel("Revenue")
    ax1.set_xlabel("Month")
    ax1.grid(True, linestyle="--", alpha=0.5)

    # Optional: display value annotations on bars
    for i, value in enumerate(df[f"Year{year}"]):
        ax2.text(
            i,
            value + value * 0.02,  # small offset above bar
            f"{int(value):,}",
            ha="center",
            va="bottom",
            fontsize=8,
            color="black",
        )

    # Remove default plot title (you handle titles in Marimo)
    ax1.set_title("")
    fig.tight_layout()

    return fig


def plot_real_vs_predicted_delivered_time(df: DataFrame, year: int) -> Figure:
    """
    Create a line plot comparing real vs. estimated delivery time
    by month for a given year.
    """
    rc_file_defaults()
    sns.set_style("whitegrid")  # Use light grid for clarity

    fig, ax = plt.subplots(figsize=(12, 4))

    # Plot each line with explicit color and label
    sns.lineplot(
        x=df["month"],
        y=df[f"Year{year}_real_time"],
        marker="o",
        label="Real Time",
        color=custom_palette[0],
        ax=ax,
    )
    sns.lineplot(
        x=df["month"],
        y=df[f"Year{year}_estimated_time"],
        marker="s",
        label="Estimated Time",
        color=custom_palette[1],
        ax=ax,
    )

    # Axis labeling and ticks
    ax.set_xlabel("Month")
    ax.set_ylabel("Average Days to Deliver")
    ax.set_xticks(range(len(df)))
    ax.set_xticklabels(df["month"].values, rotation=45)

    # Legend configuration
    ax.legend(title="", loc="upper right")

    # Improve spacing
    fig.tight_layout()

    return fig


def plot_global_amount_order_status(df: DataFrame) -> Figure:
    """
    Create a horizontal bar chart showing the global amount per order status.

    Args:
        df (DataFrame): DataFrame with:
            - 'order_status': Status labels (e.g., 'order delivered')
            - 'Amount': Count or value per status

    Returns:
        Figure: A matplotlib bar chart figure.
    """
    rc_file_defaults()
    fig, ax = plt.subplots(figsize=(10, 5))

    df = df.copy()
    df["short_status"] = df["order_status"].apply(lambda x: x.split()[-1].capitalize())
    sorted_df = df.sort_values("Amount", ascending=True)

    colors = custom_palette[: len(sorted_df)]

    bars = ax.barh(
        sorted_df["short_status"], sorted_df["Amount"], color=colors, edgecolor="black"
    )

    # Add value labels
    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + 50,
            bar.get_y() + bar.get_height() / 2,
            f"{int(width):,}",
            va="center",
            fontsize=9,
            color="black",
        )

    ax.set_xlabel("Amount")
    ax.set_ylabel("Order Status")
    ax.grid(axis="x", linestyle="--", alpha=0.4)
    fig.tight_layout()
    return fig


def plot_revenue_per_state(df: DataFrame) -> go.Figure:
    """
    Create a Plotly treemap to visualize revenue per customer state,
    using a consistent custom color palette.
    """
    fig = px.treemap(
        df,
        path=["customer_state"],
        values="Revenue",
        color="customer_state",  # Important to trigger color mapping
        color_discrete_sequence=custom_palette,
        width=800,
        height=300,
    )

    # Add label customization
    fig.update_traces(
        textinfo="label+percent entry+value",  # show label, percentage, and raw value
        textfont_size=14,
        marker=dict(
            line=dict(color="#FFFFFF", width=1)
        ),  # white borders between blocks
    )

    fig.update_layout(
        margin=dict(t=20, l=20, r=20, b=20),
        uniformtext=dict(minsize=12, mode="hide"),
    )

    return fig


def plot_top_10_least_revenue_categories(df: DataFrame) -> Figure:
    """
    Create a horizontal bar chart showing the top 10 least revenue categories.

    Args:
        df (DataFrame): DataFrame with columns:
            - 'Category': Category name
            - 'Revenue': Corresponding revenue values

    Returns:
        Figure: A matplotlib figure with a horizontal bar chart.
    """
    rc_file_defaults()
    fig, ax = plt.subplots(figsize=(10, 6))

    # Sort and plot
    sorted_df = df.sort_values("Revenue", ascending=True)
    colors = custom_palette[: len(sorted_df)]

    bars = ax.barh(
        sorted_df["Category"], sorted_df["Revenue"], color=colors, edgecolor="black"
    )

    # Add value labels
    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + 100,  # shift label to the right of the bar
            bar.get_y() + bar.get_height() / 2,
            f"${int(width):,}",
            va="center",
            fontsize=9,
            color="black",
        )

    ax.set_xlabel("Revenue")
    ax.set_ylabel("Category")
    ax.grid(axis="x", linestyle="--", alpha=0.4)
    fig.tight_layout()
    return fig


def plot_top_10_revenue_categories_amount(df: DataFrame) -> Figure:
    """
    Create a horizontal bar chart showing the revenue of the top 10 categories.

    Args:
        df (DataFrame): DataFrame with columns:
            - 'Category': Category name
            - 'Revenue': Revenue amount

    Returns:
        Figure: A matplotlib figure object.
    """
    rc_file_defaults()
    fig, ax = plt.subplots(figsize=(10, 6))

    sorted_df = df.sort_values("Revenue", ascending=True)
    colors = custom_palette[: len(sorted_df)]

    bars = ax.barh(
        sorted_df["Category"], sorted_df["Revenue"], color=colors, edgecolor="black"
    )

    # Add value labels on the right
    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + 100,
            bar.get_y() + bar.get_height() / 2,
            f"${int(width):,}",
            va="center",
            fontsize=9,
            color="black",
        )

    ax.set_xlabel("Revenue")
    ax.set_ylabel("Category")
    ax.grid(axis="x", linestyle="--", alpha=0.4)
    fig.tight_layout()
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
    fig = px.treemap(
        df,
        path=["Category"],
        values="Num_order",
        color="Num_order",
        color_continuous_scale=custom_palette,  # Optional for consistency
        hover_data={"Num_order": ":,"},  # Adds commas to values
        width=800,
        height=400,
    )
    fig.update_layout(
        margin=dict(t=40, l=30, r=30, b=30),
        coloraxis_showscale=False,  # Optional: hides legend bar
    )
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
    rc_file_defaults()
    fig, ax = plt.subplots(figsize=(10, 5))

    sns.scatterplot(
        data=df,
        x="product_weight_g",
        y="freight_value",
        color=custom_palette[2],
        edgecolor="white",
        alpha=0.7,
        s=50,
        ax=ax,
    )

    ax.set_xlabel("Product Weight (grams)")
    ax.set_ylabel("Freight Value ($)")
    ax.grid(True, linestyle="--", alpha=0.5)

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
    rc_file_defaults()
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.barplot(
        data=df, x="Delivery_Difference", y="State", color=custom_palette[0], ax=ax
    )

    ax.set_title(
        "Difference Between Estimated and Actual Delivery Dates by State",
        fontsize=12,
        weight="bold",
    )
    ax.set_xlabel("Delivery Difference (Days)")
    ax.set_ylabel("State")
    ax.grid(True, linestyle="--", alpha=0.4, axis="x")

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
    rc_file_defaults()
    df = df.copy()
    df["date"] = to_datetime(df["date"], unit="ms")
    df = df.sort_values("date")

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df["date"], df["order_count"], color=custom_palette[2], label="Order Count")

    for holiday_date in df[df["holiday"]]["date"]:
        ax.axvline(
            holiday_date,
            color=custom_palette[3],
            linestyle="--",
            alpha=0.4,
            label="Holiday",
        )

    ax.set_xlabel("Date")
    ax.set_ylabel("Order Count")

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.tick_params(axis="x", rotation=45)

    ax.grid(True, linestyle="--", alpha=0.5)
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))  # avoid duplicate "Holiday" entries
    ax.legend(by_label.values(), by_label.keys(), loc="upper left")

    fig.tight_layout()
    return fig
