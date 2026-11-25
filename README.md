# E-Commerce Sales & Profit Analysis (Python)

## Overview
An exploratory data analysis project examining e-commerce order performance across product categories, monthly trends, and discount tiers using Python (`pandas`, `numpy`, `matplotlib`).

## Key Findings
- **Category Performance:** Revenue distribution varies significantly across categories, with high-ticket and high-demand items driving the bulk of net sales.
- **Monthly Trend:** Tracking monthly net sales highlights seasonal fluctuations and growth consistency across the year.
- **Discount Impact:** Higher discount tiers (25%+) compress profit margins and can turn average order profit negative, showing the need to cap heavy discounts.

## Files Included
- `analysis.py` – Data generation, cleaning check, summary metrics, and chart generation
- `ecommerce_sales.csv` – Order-level dataset
- `sales_by_category.png` – Net sales comparison by category
- `monthly_sales_trend.png` – Monthly revenue trend
- `discount_vs_profit.png` – Impact of discounting on average profit

## How to Run
```bash
pip install pandas matplotlib numpy
python analysis.py