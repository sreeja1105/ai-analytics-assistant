import os
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

DATA_PATH = Path(__file__).resolve().parent / "data" / "sales_sample.csv"


def load_sample_data() -> pd.DataFrame:
    if DATA_PATH.exists():
        df = pd.read_csv(DATA_PATH, parse_dates=["OrderDate"])
    else:
        df = pd.DataFrame([
            {"OrderID": 1001, "Region": "West", "SalesAmount": 12500, "Quantity": 25, "Product": "Smart Display", "OrderDate": "2024-01-08"},
            {"OrderID": 1002, "Region": "East", "SalesAmount": 9800, "Quantity": 18, "Product": "AI Speaker", "OrderDate": "2024-02-14"},
            {"OrderID": 1003, "Region": "North", "SalesAmount": 14200, "Quantity": 28, "Product": "Business Laptop", "OrderDate": "2024-03-05"},
            {"OrderID": 1004, "Region": "South", "SalesAmount": 7600, "Quantity": 14, "Product": "Wireless Headset", "OrderDate": "2024-03-21"},
            {"OrderID": 1005, "Region": "West", "SalesAmount": 18300, "Quantity": 35, "Product": "AI Dashboard", "OrderDate": "2024-04-12"},
        ])
        df["OrderDate"] = pd.to_datetime(df["OrderDate"])
    return df


def summarize_data(df: pd.DataFrame) -> dict:
    total_sales = df["SalesAmount"].sum()
    total_units = df["Quantity"].sum()
    avg_order = df["SalesAmount"].mean()
    top_region = df.groupby("Region")["SalesAmount"].sum().idxmax()
    top_product = df.groupby("Product")["SalesAmount"].sum().idxmax()
    return {
        "total_sales": total_sales,
        "total_units": total_units,
        "avg_order": avg_order,
        "top_region": top_region,
        "top_product": top_product,
    }


def build_prompt(summary: dict, question: str) -> str:
    prompt = [
        "You are an analytics assistant.",
        "Use the summary statistics and sample data to answer the question.",
        "Summary:",
        f"Total Sales: {summary['total_sales']}",
        f"Total Units: {summary['total_units']}",
        f"Average Order Value: {summary['avg_order']:.2f}",
        f"Top Region: {summary['top_region']}",
        f"Top Product: {summary['top_product']}",
        "Answer the question concisely and include a recommended next step.",
        "Question:",
        question,
    ]
    return "\n".join(prompt)


def ask_model(question: str, summary: dict) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if OpenAI is None or not api_key:
        return (
            "OpenAI is not configured.\n"
            "Install the openai package and set OPENAI_API_KEY to enable AI answers."
        )

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=build_prompt(summary, question),
        max_tokens=250,
    )
    return response.output_text


st.set_page_config(page_title="AI Analytics Assistant", layout="wide")
st.title("AI Analytics Assistant")
st.markdown(
    "Explore sample sales data and ask business questions in natural language."
)

sales_data = load_sample_data()
uploaded_file = st.sidebar.file_uploader("Upload a CSV file to replace the sample dataset", type=["csv"])
if uploaded_file is not None:
    sales_data = pd.read_csv(uploaded_file, parse_dates=["OrderDate"])

summary = summarize_data(sales_data)

st.sidebar.markdown("## Dataset details")
st.sidebar.write(f"Rows: {sales_data.shape[0]}")
st.sidebar.write(f"Columns: {sales_data.shape[1]}")
st.sidebar.write("Use the sample data or upload your own CSV with OrderDate, Region, Product, Quantity, and SalesAmount.")

st.subheader("Key business metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${summary['total_sales']:,}")
col2.metric("Total Units", f"{summary['total_units']}")
col3.metric("Avg Order Value", f"${summary['avg_order']:.2f}")
col4.metric("Top Region", summary["top_region"])

st.subheader("Revenue by Region")
region_fig = px.bar(
    sales_data.groupby("Region", as_index=False)["SalesAmount"].sum(),
    x="Region",
    y="SalesAmount",
    title="Revenue by Region",
    labels={"SalesAmount": "Sales Amount", "Region": "Region"},
)
st.plotly_chart(region_fig, use_container_width=True)

st.subheader("Sales trend")
trend_fig = px.line(
    sales_data.groupby("OrderDate", as_index=False)["SalesAmount"].sum(),
    x="OrderDate",
    y="SalesAmount",
    title="Sales Trend Over Time",
    labels={"SalesAmount": "Sales Amount", "OrderDate": "Order Date"},
)
st.plotly_chart(trend_fig, use_container_width=True)

st.subheader("Top products")
product_fig = px.bar(
    sales_data.groupby("Product", as_index=False)["SalesAmount"].sum().sort_values("SalesAmount", ascending=False),
    x="SalesAmount",
    y="Product",
    orientation="h",
    title="Top Products by Revenue",
    labels={"SalesAmount": "Sales Amount", "Product": "Product"},
)
st.plotly_chart(product_fig, use_container_width=True)

st.subheader("Question for the AI assistant")
user_question = st.text_input("Ask a business question about the sales data:")

if st.button("Ask AI") and user_question:
    with st.spinner("Generating answer..."):
        answer = ask_model(user_question, summary)
        st.markdown("### AI Answer")
        st.write(answer)

st.markdown("---")
st.subheader("Sample data")
st.dataframe(sales_data)
