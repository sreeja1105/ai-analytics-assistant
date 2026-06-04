# AI Analytics Assistant

[![Streamlit](https://img.shields.io/badge/Streamlit-Ready-orange?logo=streamlit)](https://streamlit.io/) [![OpenAI](https://img.shields.io/badge/OpenAI-GPT-blue?logo=openai)](https://openai.com/) [![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/) [![Status](https://img.shields.io/badge/status-in_development-yellow)](https://github.com/sreeja1105/ai-analytics-assistant)

A modern analytics project that combines AI and data insights for business decision-making.

This repository demonstrates a practical AI-assisted analytics assistant with a user-facing interface, real business data patterns, and natural language insight generation.

## Why this project

This project is ideal for recruiters and hiring managers because it shows:
- AI / LLM integration
- data analysis and visualization
- business storytelling
- practical product experience

## Features

- Load a sample sales dataset
- Show key business metrics
- Create charts and trend summaries
- Ask questions in natural language
- Generate insights using a large language model

## Tech stack

- Python
- Streamlit
- pandas
- OpenAI (or another LLM provider)
- Plotly / Matplotlib

## How it works

1. Load a sales dataset from the included demo CSV.
2. Calculate metrics such as total revenue, units sold, average order value, and best region.
3. Display interactive charts for region revenue, product revenue, and sales trend.
4. Accept a natural language question from the user.
5. Send the question, summary statistics, and sales insights to an LLM.
6. Display the AI-generated recommendation and next steps.

## Demo dataset

This repo includes a sample dataset at `data/sales_sample.csv`.
It is ready to use for the app and contains sales orders across regions, products, and customer segments.

## How to run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your_api_key"
```

3. Run the app:
```bash
streamlit run app.py
```

4. Optionally upload your own CSV file in the app sidebar.

## Demo and deployment

This project is ready for deployment on Streamlit Cloud or any Python hosting platform. After deployment, add a live demo link here to make the project more visible to hiring managers.

## Example use cases

- Ask: "What were the top selling products last quarter?"
- Ask: "Which region had the highest revenue growth?"
- Ask: "What action should the sales team take next month?"

## Project value

This project is a strong addition to a portfolio because it blends modern AI with business analytics, making it relevant to roles such as:
- Data Analyst
- Business Intelligence Analyst
- AI/ML Analyst
- Analytics Engineer
- Product Analytics

## Next improvements

- Add real dataset uploads
- Build a DAX / Power BI recommendation engine
- Enable multi-modal insights with charts and tables
- Add a deployment demo with Streamlit Cloud or GitHub Pages
