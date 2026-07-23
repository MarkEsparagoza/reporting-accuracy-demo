"""
Generates synthetic sample data for a two-system sales reconciliation demo.
This is fabricated data for portfolio/demonstration purposes only.
"""
import itertools
import pandas as pd
import numpy as np

np.random.seed(42)

regions = ["West", "Midwest", "Northeast", "South"]
distributors = ["Distributor A", "Distributor B", "Distributor C", "Distributor D"]
skus = [f"SKU-{i:03d}" for i in range(1, 21)]
months = ["2026-01", "2026-02", "2026-03", "2026-04", "2026-05"]

distributor_bias = {"Distributor A": 0.06, "Distributor B": 0.01, "Distributor C": 0.045, "Distributor D": -0.01}

combos = list(itertools.product(months, skus, regions, distributors))
keep = [c for c in combos if np.random.rand() < 0.7]

rows = []
for month, sku, region, dist in keep:
      base_qty = np.random.randint(50, 500)
      unit_price = round(np.random.uniform(8, 45), 2)
      system_a_sales = round(base_qty * unit_price, 2)
      bias = distributor_bias[dist]
      random_noise = np.random.uniform(-0.01, 0.01)
      system_b_sales = round(system_a_sales * (1 + bias + random_noise), 2)
      row = {"month": month, "sku": sku, "region": region, "distributor": dist, "system_a_sales": system_a_sales, "system_b_sales": system_b_sales}
      rows.append(row)

df = pd.DataFrame(rows)
df.to_csv("data/sample_reconciliation_data.csv", index=False)
print(f"Generated {len(df)} rows")
print(df.head())
