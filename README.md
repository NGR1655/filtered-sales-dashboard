# 📊 Filtered Sales Dashboard

An interactive sales analytics dashboard built with **Streamlit** and **Plotly**, enabling real-time filtering and AI-powered insights from Excel sales data.

---

## 🚀 Features

- 📁 Loads sales data from an Excel file automatically
- 🌍 Filter sales data by **Region** using a sidebar dropdown
- 📊 Interactive **Bar Chart** showing Total Sales by Product and Status
- 🧠 **AI-generated insights** for the filtered data
- ✅ Clean and responsive wide-layout UI

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| Streamlit | Web dashboard framework |
| Pandas | Data manipulation |
| Plotly Express | Interactive charts |
| OpenPyXL | Excel file reading |

---

## 📂 Project Structure

```
filtered-sales-dashboard/
│
├── app.py                        # Main Streamlit app
├── data/
│   └── augmented_dashboard.xlsx  # Sales data (Excel)
├── utils/
│   └── insights.py               # AI insight generator
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/NGR1655/filtered-sales-dashboard.git
cd filtered-sales-dashboard
```

### 2. Install dependencies
```bash
python -m pip install streamlit pandas numpy openpyxl plotly
```

### 3. Run the app
```bash
python -m streamlit run app.py
```

### 4. Open in browser
The app will automatically open at:
```
http://localhost:8501
```

---

## 📸 Screenshot

> Dashboard showing Sales Data filtered by Region with AI Insights

---

## 📊 How It Works

1. The app reads `data/augmented_dashboard.xlsx`
2. Calculates `total_sales = quantity × unit_price`
3. User selects a **Region** from the sidebar
4. Dashboard displays filtered table, bar chart, and AI insight

---

## 🙋‍♀️ Author

**Greeshma Reddy N**  
GitHub: [@NGR1655](https://github.com/NGR1655)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
