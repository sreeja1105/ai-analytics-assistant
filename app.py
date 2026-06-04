import os

import pandas as pd
import plotly.express as px
import streamlit as st

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


def load_sample_data():
    data = pd.DataFrame([
        {"OrderID": 1001, "Region": "West", "SalesAmount": 12500, "Quantity": 25, "Product": "Smart Display", "OrderDate": "2024-01-08"},
        {"OrderID": 1002, "Region": "East", "SalesAmount": 9800, "Quantity": 18, "Product": "AI Speaker", "OrderDate": "2024-02-14"},
        {"OrderID": 1003, "Region": "North", "SalesAmount": 14200, "Quantity": 28, "Product": "Business Laptop", "OrderDate": "2024-03-05"},
        {"OrderID": 1004, "Region": "South", "SalesAmount": 7600, "Quantity": 14, "Product": "Wireless Headset", "OrderDate": "2024-03-21"},
        {"OrderID": 1005, "Region": "West", "SalesAmount": 18300, "Quantity": 35, "Product": "AI Dashboard", "OrderDate": "2024-04-12"},
    ])
    data["OrderDate"] = pd.to_datetime(data["OrderDate"])
    return data


def summarize_data(df: pd.DataFrame):
    total_sales = df["SalesAmount"].sum()
    total_units = df["Quantity"].sum()
    avg_order = df["SalesAmount"].mean()
    top_region = df.groupby("Region")["SalesAmount"].sum().idxmax()
    return {
        "total_sales": total_sales,
        "total_units": total_units,
        "avg_order": avg_order,
        "top_region": top_region,
    }


def build_prompt(summary: dict, question: str):
    prompt = [
        "You are an analytics assistant.",
        "Use the summary statistics and sample data to answer the question.",
        "Summary:",
        f"Total Sales: {summary['total_sales']}",
        f"Total Units: {summary['total_units']}",
        f"Average Order Value: {summary['avg_order']:.2f}",
        f"Top Region: {summary['top_region']}",
        "Answer the question concisely and include a recommended next step.",
        "Question:",
        question,
    ]
    return "\n".join(prompt)


def ask_model(question: str, summary: dict):
    api_key = os.getenv("OPENAI_API_KEY")
    if OpenAI is None or not api_key:
        return (
            "OpenAI is not configured.\n"
            "Set OPENAI_API_KEY and install the openai package to enable AI answers."
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
    "Use this app to explore sales data and ask business questions in natural language."
)

sales_data = load_sample_data()
summary = summarize_data(sales_data)

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${summary['total_sales']:,}")
col2.metric("Total Units", f"{summary['total_units']}")
col3.metric("Top Region", summary["top_region"])

st.subheader("Sales by Region")
fig = px.bar(
    sales_data.groupby("Region", as_index=False)["SalesAmount"].sum(),
    x="Region",
    y="SalesAmount",
    title="Revenue by Region",
)
st.plotly_chart(fig, use_container_width=True)

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
