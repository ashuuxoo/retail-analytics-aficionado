# Product Optimization & Revenue Contribution Analysis

## Aficionado Coffee Roasters — Retail Analytics Project

### Project Overview

This project analyzes transaction-level retail data from Aficionado Coffee Roasters to understand product performance, revenue contribution, and category-level sales trends. The goal is to support data-driven decision-making for menu optimization and revenue growth.

The analysis focuses on identifying top-selling products, underperforming menu items, and revenue concentration across product categories and store locations.

---

### Dataset

The dataset contains transaction-level sales information including:

* transaction_id
* transaction_time
* transaction_qty
* unit_price
* store_location
* product_category
* product_type
* product_detail

A **revenue column** was created using:

Revenue = transaction_qty × unit_price

---

### Analytical Methodology

The project includes:

* Data ingestion and validation
* Revenue computation
* Product popularity analysis
* Revenue contribution analysis
* Category and product-type performance analysis
* Pareto (80/20) revenue concentration analysis

---

### Streamlit Dashboard Features

The dashboard includes:

* Product ranking by revenue and quantity
* Category revenue distribution
* Popularity vs revenue scatter plot
* Product drill-down table
* Category filter
* Store location selector
* Top-N product slider

---

### Tools & Technologies

* Python
* Pandas
* Matplotlib
* Streamlit
* Google Colab
* GitHub

---

### Project Structure

```
app.py
Afficionado Coffee Roasters.xlsx
Retail_Analytics_Aficionado.ipynb
Research_Paper_Retail_Analytics.pdf
Executive_Summary.pdf
```

---

### Key Insights

* A small number of products contribute a large share of total revenue.
* Core beverage categories generate most of the sales.
* Some products are popular but contribute less revenue.
* Several long-tail products have minimal financial impact.
* Store performance varies across locations.

---

### Conclusion

This project demonstrates how retail transaction data can be transformed into actionable business insights using exploratory data analysis and dashboard visualization. The results support product optimization, pricing strategy improvements, and better inventory planning.
