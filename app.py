import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Retail Analytics Dashboard", layout="wide")

st.title("Executive Retail Intelligence")
st.markdown("Product Optimization & Revenue Contribution Analysis")

# Load data
df = pd.read_excel("Afficionado Coffee Roasters.xlsx")
df["revenue"] = df["transaction_qty"] * df["unit_price"]

# Sidebar
st.sidebar.header("Filters")

category = st.sidebar.selectbox(
    "Category",
    ["All"] + list(df["product_category"].unique())
)

store = st.sidebar.selectbox(
    "Store",
    ["All"] + list(df["store_location"].unique())
)

top_n = st.sidebar.slider("Top Products", 5, 20, 10)

filtered = df.copy()

if category != "All":
    filtered = filtered[filtered["product_category"] == category]

if store != "All":
    filtered = filtered[filtered["store_location"] == store]

# KPI SECTION
total_revenue = filtered["revenue"].sum()
total_qty = filtered["transaction_qty"].sum()
transactions = filtered["transaction_id"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Units Sold", f"{total_qty:,}")
col3.metric("Transactions", f"{transactions:,}")

st.divider()

# Product ranking
st.subheader("Top Products by Revenue")

product_perf = filtered.groupby("product_detail").agg({
    "transaction_qty": "sum",
    "revenue": "sum"
}).sort_values("revenue", ascending=False).head(top_n)

st.dataframe(product_perf, use_container_width=True)

st.divider()

# Charts side by side
colA, colB = st.columns(2)

with colA:
    st.subheader("Category Revenue Distribution")
    cat_rev = filtered.groupby("product_category")["revenue"].sum()
    fig, ax = plt.subplots()
    cat_rev.plot(kind="pie", autopct="%1.1f%%", ax=ax)
    st.pyplot(fig)

with colB:
    st.subheader("Popularity vs Revenue")
    scatter = filtered.groupby("product_detail").agg({
        "transaction_qty": "sum",
        "revenue": "sum"
    })
    fig2, ax2 = plt.subplots()
    ax2.scatter(scatter["transaction_qty"], scatter["revenue"])
    ax2.set_xlabel("Units Sold")
    ax2.set_ylabel("Revenue")
    st.pyplot(fig2)

st.divider()

st.subheader("Transaction Data")
st.dataframe(filtered, use_container_width=True)
