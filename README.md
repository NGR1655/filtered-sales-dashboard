# Filtered Sales Dashboard

An interactive sales analytics dashboard built with Streamlit and Plotly, enabling real-time filtering and AI-powered insights from Excel sales data.

## Features

- Loads sales data from an Excel file automatically
- Filter sales data by Region using a sidebar dropdown
- Interactive Bar Chart showing Total Sales by Product and Status
- AI-generated insights for the filtered data
- Clean and responsive wide-layout UI

## How it works

1. The app reads `data/augmented_dashboard.xlsx`
2. Calculates `total_sales = quantity × unit_price`
3. User selects a **Region** from the sidebar
4. Dashboard displays filtered table, bar chart, and AI insight


## How to run it

Make sure you have Python installed, then:

```bash
pip install streamlit pandas plotly openpyxl
python -m streamlit run app.py
```


## Project Structure

```
├── app.py
├── data/
│   └── augmented_dashboard.xlsx
└── utils/
    └── insights.py

----
## Built with

- Python
- Streamlit
- Plotly
- Pandas
