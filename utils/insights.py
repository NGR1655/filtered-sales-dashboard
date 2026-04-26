import random

def generate_insight(df):
    # Check if dataframe is empty
    if df.empty:
        return "No data available for this region."

    # Top selling product
    top_product = df.groupby("product")["total_sales"].sum().idxmax()

    # Total sales
    total = df["total_sales"].sum()

    # Average order value
    avg_order = df["total_sales"].mean()

    # Insight options
    options = [
        f"💰 Total sales in this region: ₹{total:.2f}",
        f"🏆 Best seller: {top_product}",
        f"📊 Average order value: ₹{avg_order:.2f}"
    ]

    return random.choice(options)
