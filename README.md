# AI Analytics Assistant

[![Streamlit](https://img.shields.io/badge/Streamlit-Ready-orange?logo=streamlit)](https://streamlit.io/) [![OpenAI](https://img.shields.io/badge/OpenAI-GPT-blue?logo=openai)](https://openai.com/) [![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/) [![Status](https://img.shields.io/badge/status-in_development-yellow)](https://github.com/sreeja1105/ai-analytics-assistant)

AI Analytics Assistant is a practical data product that combines AI-powered insights with interactive analytics.

This Streamlit application loads a sample sales dataset, calculates business KPIs, visualizes revenue trends, and answers natural language questions using an LLM.

## Overview

- Load structured sales data and calculate revenue, volume, and product metrics.
- Display clear charts for region performance, product revenue, and sales trend.
- Answer business questions in plain language using OpenAI.
- Support CSV upload so users can analyze their own dataset.

## Features

- Interactive dashboard with business metrics and charts
- Natural language question-answering over sales data
- Demo dataset included for quick evaluation
- CSV upload support for custom files
- Clean, modern Streamlit UI

## Tech stack

- Python
- Streamlit
- pandas
- Plotly
- OpenAI API

## Project files

- `app.py` - main Streamlit application
- `data/sales_sample.csv` - sample sales dataset
- `requirements.txt` - Python dependencies
- `.gitignore` - exclude temp files and environment files

## Demo dataset

The included sample dataset is stored in `data/sales_sample.csv` and contains sales orders across regions, products, and customer segments. It is ready to use for a fast project demonstration.

## How to run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key:
```powershell
setx OPENAI_API_KEY "your_api_key"
```

3. Run the app:
```bash
streamlit run app.py
```

4. Optionally upload your own CSV file in the app sidebar.

## Example use cases

- Ask: "What were the top selling products last quarter?"
- Ask: "Which region had the highest revenue growth?"
- Ask: "What action should the sales team take next month?"

## Why this project is valuable

This project demonstrates AI and analytics skills that employers seek in modern data roles:
- AI / LLM integration for business insights
- data visualization and dashboarding
- practical product design and storytelling
- hands-on Python and Streamlit development

## Demo and deployment

This repository is ready for deployment on Streamlit Cloud or any Python hosting platform. Deploying a live demo will make the project easier for hiring managers to review.

## Next improvements

- Add more advanced data cleaning and feature engineering
- Deploy a live demo with Streamlit Cloud
- Extend the AI prompt to include trend insights and forecasts
- Add unit tests and deployment automation
