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

1. [Project Description](#1-project-description)
2. [Methodology & Key Features](#2-methodology--key-features)
3. [Technology Stack](#3-technology-stack)
4. [Dataset](#4-dataset)

## 1. Project Description

This project showcases an Extract, Load, and Transform (ELT) pipeline applied to a real-world e-commerce dataset. The primary goal is to extract valuable business insights from transactional data and present them through an interactive dashboard. The pipeline integrates data from the **Brazilian E-Commerce Public Dataset by Olist**, which contains over **100,000 orders** from 2016 to 2018, and also incorporates data from the Public Holiday API to analyze sales performance during national holidays.

The dashboard provides a detailed view of the e-commerce experience, including:

- Order status, prices, and payment types
- Freight and delivery performance
- Customer locations and product categories
- Customer reviews and satisfaction

> [!IMPORTANT]  
> You can check out the deployed dashboard here: [E-Commerce ELT](https://huggingface.co/spaces/iBrokeTheCode/E-Commerce_ELT)

![Dashboard](./public/dashboard-demo.png)

## 2. Methodology & Key Features

The ELT pipeline extracts raw data, loads it into a structured format, and then transforms it to generate key metrics and visualizations. The analysis is presented using an interactive dashboard built with Marimo, a Python library.

### Key Features:

- **Data Integration**: Combines e-commerce order data with public holiday information to analyze temporal sales patterns.
- **Data Transformation**: Cleans and prepares raw data for analysis, enabling the calculation of key performance indicators (KPIs).
- **Interactive Dashboard**: Provides a dynamic and user-friendly interface for exploring business insights.

## 3. Technology Stack

This project was built using the following technologies and libraries:

**Dashboard & Hosting:**

- [Marimo](https://github.com/marimo-team/marimo): A Python library for building interactive dashboards.
- [Hugging Face Spaces](https://huggingface.co/docs/hub/spaces-config-reference): Used for hosting and sharing the interactive dashboard.

**Data Analysis & Visualization:**

- [Pandas](https://pandas.pydata.org/): For data manipulation and analysis.
- [Plotly](https://plotly.com/python/): For creating interactive data visualizations.
- [Matplotlib](https://matplotlib.org/): For creating static visualizations.
- [Seaborn](https://seaborn.pydata.org/): For creating statistical graphics.

**Data Handling & Utilities:**

- [SQLAlchemy](https://www.sqlalchemy.org/): For interacting with databases.
- [Requests](https://requests.readthedocs.io/en/latest/): For making HTTP requests to external APIs.

**Development Tools:**

- [Ruff](https://github.com/charliermarsh/ruff): A fast Python linter and code formatter.
- [uv](https://github.com/astral-sh/uv): A fast Python package installer and resolver.

## 4. Dataset

This project utilizes the **Brazilian E-Commerce Public Dataset by Olist** from Kaggle, a public dataset containing details on over 100,000 orders. The data spans from 2016 to 2018 and includes a wide range of transactional information.

- **Source**: [Kaggle Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- **Additional Data**: The project also integrates data from the [Public Holiday API](https://date.nager.at/Api).

Here is the ERD diagram for the database schema:

![ERD](./public/erd-schema.png)
