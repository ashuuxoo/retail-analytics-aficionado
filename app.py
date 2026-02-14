import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Aficionado Coffee Roasters — Retail Analytics Dashboard")

# Load dataset
df = pd.read_excel("Afficionado Coffee Roasters.xlsx")
df["revenue"] = df["transaction_qty"] * df["unit_price"]

# Sidebar filters
category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + list(df["product_category"].unique())
)

store = st.sidebar.selectbox(
    "Select Store",
    ["All"] + list(df["store_location"].unique())
)

top_n = st.sidebar.slider("Top N Products", 5, 20, 10)

filtered = df.copy()

if category != "All":
    filtered = filtered[filtered["product_category"] == category]

if store != "All":
    filtered = filtered[filtered["store_location"] == store]

# Product ranking
st.header("Product Ranking")
product_perf = filtered.groupby("product_detail").agg({
    "transaction_qty": "sum",
    "revenue": "sum"
}).sort_values("revenue", ascending=False).head(top_n)

st.dataframe(product_perf)

# Category revenue distribution
st.header("Category Revenue Distribution")
cat_rev = filtered.groupby("product_category")["revenue"].sum()

fig, ax = plt.subplots()
cat_rev.plot(kind="pie", autopct="%1.1f%%", ax=ax)
st.pyplot(fig)

# Popularity vs revenue
st.header("Popularity vs Revenue")
scatter = filtered.groupby("product_detail").agg({
    "transaction_qty": "sum",
    "revenue": "sum"
})

fig2, ax2 = plt.subplots()
ax2.scatter(scatter["transaction_qty"], scatter["revenue"])
ax2.set_xlabel("Units Sold")
ax2.set_ylabel("Revenue")
st.pyplot(fig2)

# Drill-down table
st.header("Product Drill-down Table")
st.dataframe(filtered)
