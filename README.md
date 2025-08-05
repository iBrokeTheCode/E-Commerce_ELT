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
3. [Entity Relationship Diagram](#3-entity-relationship-diagram)

## 1. 🛍️ Description

This dashboard presents insights from the real-world [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), which includes data on over **100,000 orders** placed between **2016 and 2018** across various online marketplaces in Brazil. It also integrates data from the [Public Holiday API](https://date.nager.at/Api) to analyze sales performance during national holidays.

The dataset offers a detailed view of the e-commerce experience, including:

- Order status, prices, and payment types
- Freight and delivery performance
- Customer locations and product categories
- Customer reviews and satisfaction

> [!IMPORTANT]  
> Check the Dashboard deployed on Hugging Face Spaces: [E-Commerce ELT](https://huggingface.co/spaces/iBrokeTheCode/E-Commerce_ELT)

## 2. 🧑‍💻 Stack

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

## 3. Entity Relationship Diagram

![ERD](./public/erd-schema.png)
