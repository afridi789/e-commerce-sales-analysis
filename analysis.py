import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Realistic dataset generate karo (300 rows)
np.random.seed(42)
rows = 300

categories = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Fitness"]
regions = ["North", "South", "East", "West"]
dates = pd.date_range("2026-01-01", "2026-10-31", periods=rows)

df = pd.DataFrame({
    "Order_ID": [f"ORD-{1000 + i}" for i in range(rows)],
    "Order_Date": dates,
    "Category": np.random.choice(categories, size=rows, p=[0.28, 0.24, 0.20, 0.14, 0.14]),
    "Region": np.random.choice(regions, size=rows),
    "Units_Sold": np.random.randint(1, 8, size=rows),
    "Unit_Price": np.random.randint(400, 8000, size=rows),
    "Discount_Pct": np.random.choice([0, 5, 10, 15, 20, 25, 30], size=rows, p=[0.2, 0.2, 0.2, 0.15, 0.1, 0.1, 0.05])
})

df["Gross_Sales"] = df["Units_Sold"] * df["Unit_Price"]
df["Net_Sales"] = (df["Gross_Sales"] * (1 - df["Discount_Pct"] / 100)).round(2)
# Higher discount reduces profit margin
margin_rate = np.where(df["Discount_Pct"] >= 25, -0.05,
              np.where(df["Discount_Pct"] >= 15, 0.10, 0.22))
df["Profit"] = (df["Net_Sales"] * margin_rate).round(2)

# Save dataset
df.to_csv("ecommerce_sales.csv", index=False)

# 2. Data cleaning check
print("Missing values:\n", df.isnull().sum())
print("\nTotal Net Sales:", round(df["Net_Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("\nCategory Summary:\n", df.groupby("Category")[["Net_Sales", "Profit"]].sum().sort_values("Net_Sales", ascending=False))
print("\nDiscount vs Avg Profit:\n", df.groupby("Discount_Pct")["Profit"].mean().round(2))

# 3. Chart 1: Net Sales by Category
plt.figure(figsize=(8, 5))
cat_sales = df.groupby("Category")["Net_Sales"].sum().sort_values()
cat_sales.plot(kind="barh")
plt.title("Net Sales by Category (Jan - Oct 2026)")
plt.xlabel("Net Sales (INR)")
plt.tight_layout()
plt.savefig("sales_by_category.png", dpi=150)
plt.close()

# 4. Chart 2: Monthly Net Sales Trend
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
monthly_sales = df.groupby("Month")["Net_Sales"].sum()

plt.figure(figsize=(8, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Net Sales Trend")
plt.ylabel("Net Sales (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=150)
plt.close()

# 5. Chart 3: Discount % vs Average Profit
plt.figure(figsize=(8, 5))
disc_profit = df.groupby("Discount_Pct")["Profit"].mean()
disc_profit.plot(kind="bar")
plt.title("Average Profit by Discount Level")
plt.xlabel("Discount (%)")
plt.ylabel("Average Profit (INR)")
plt.tight_layout()
plt.savefig("discount_vs_profit.png", dpi=150)
plt.close()

print("\nCharts and CSV generated successfully.")