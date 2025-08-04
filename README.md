---
title: E-Commerce ELT
emoji: 🍃
colorFrom: indigo
colorTo: purple
sdk: docker
pinned: true
license: mit
short_description: Extract, Load, Transform Pipeline applied to an E-Commerce
---

# E-Commerce ELT Pipeline

## Table of Contents

1. [Description](#1-description)
2. [Stack](#2-stack)

## 1. Description

This project analyzes e-commerce data from a Brazilian marketplace to explore key business metrics related to **revenue** and **delivery performance**. Using an interactive Marimo application, the analysis provides insights into:

- **Revenue:** Annual revenue, popular product categories, and sales by state.
- **Delivery:** Delivery performance, including time-to-delivery and its correlation with public holidays.

The data pipeline processes information from [multiple CSV files](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) and a [public API](https://date.nager.at/Api), storing and analyzing the results using Python. The final interactive report is presented as a Hugging Face Space built with Marimo.

## 2. Stack

- [Marimo](https://github.com/marimo-team/marimo): A Python library for building interactive dashboards.
- [Hugging Face Spaces](https://huggingface.co/docs/hub/spaces-config-reference): A platform for hosting and sharing interactive machine learning demos and applications
- [Pandas](https://pandas.pydata.org/): A Python library for data manipulation and analysis.
- [Plotly](https://plotly.com/python/): A Python library for interactive data visualization.
- [Matplotlib](https://matplotlib.org/): A Python library for creating static, animated, and interactive visualizations.
- [Seaborn](https://seaborn.pydata.org/): A Python library for creating statistical graphics.
- [SQLAlchemy](https://www.sqlalchemy.org/): A Python library for interacting with databases.
- [Requests](https://requests.readthedocs.io/en/latest/): A Python library for making HTTP requests.
- [Ruff](https://github.com/charliermarsh/ruff): An extremely fast Python linter and code formatter, written in Rust.
- [uv](https://github.com/astral-sh/uv): An extremely fast Python package and project manager, written in Rust.
