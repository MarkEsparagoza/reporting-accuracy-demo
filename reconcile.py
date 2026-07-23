"""
Sales Data Reconciliation Analysis
Compares sales figures between two independent reporting systems
(System A vs System B), quantifies the gap, and breaks it down
by month, SKU, region, and distributor to surface where and why
discrepancies occur.
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sample_reconciliation_data.csv")

total_a = df["system_a_sales"].sum()
total_b = df["system_b_sales"].sum()
gap_pct = (total_b - total_a) / total_a * 100

print("OVERALL RECONCILIATION SUMMARY")
print(f"System A total: {total_a:,.2f}")
print(f"System B total: {total_b:,.2f}")
print(f"Gap: {gap_pct:+.2f} percent")

monthly = df.groupby("month").agg(system_a=("system_a_sales", "sum"), system_b=("system_b_sales", "sum"))
monthly["gap_pct"] = (monthly["system_b"] - monthly["system_a"]) / monthly["system_a"] * 100
print("GAP BY MONTH")
print(monthly.round(2))

by_dist = df.groupby("distributor").agg(system_a=("system_a_sales", "sum"), system_b=("system_b_sales", "sum"))
by_dist["gap_pct"] = (by_dist["system_b"] - by_dist["system_a"]) / by_dist["system_a"] * 100
by_dist = by_dist.sort_values("gap_pct", ascending=False)
print("GAP BY DISTRIBUTOR")
print(by_dist.round(2))

by_region = df.groupby("region").agg(system_a=("system_a_sales", "sum"), system_b=("system_b_sales", "sum"))
by_region["gap_pct"] = (by_region["system_b"] - by_region["system_a"]) / by_region["system_a"] * 100
print("GAP BY REGION")
print(by_region.round(2))

monthly.to_csv("output/gap_by_month.csv")
by_dist.to_csv("output/gap_by_distributor.csv")
by_region.to_csv("output/gap_by_region.csv")

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
axes[0].plot(monthly.index, monthly["gap_pct"], marker="o", color="#1F3864", linewidth=2)
axes[0].axhline(0, color="grey", linewidth=0.8, linestyle="--")
axes[0].set_title("Reporting Gap pct by Month")
axes[0].set_ylabel("Gap (%)")
axes[0].tick_params(axis="x", rotation=45)
axes[1].barh(by_dist.index, by_dist["gap_pct"], color="#2E5090")
axes[1].axvline(0, color="grey", linewidth=0.8)
axes[1].set_title("Reporting Gap pct by Distributor")
axes[1].set_xlabel("Gap (%)")
plt.tight_layout()
plt.savefig("output/reconciliation_summary_chart.png", dpi=150)
print("Saved chart to output/reconciliation_summary_chart.png")
