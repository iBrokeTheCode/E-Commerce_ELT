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


if __name__ == "__main__":
    app.run()
