import pandas as pd
import numpy as np

month_se = pd.Series(["1월", "2월", "3월", "4월"])
income_se = pd.Series([9_500, 6_200, 6_050, 7_000])
expense_se = pd.Series([5_040, 2_350, 2_300, 4_800])

df = pd.DataFrame({"월":month_se, "수입":income_se, "지출":expense_se})

print(df)

print(month_se[np.argmax(income_se)])
print(df["월"][np.argmax(df["수입"])])
print(df["수입"].max())
print(df["수입"].mean())

print(df.columns)
print(df.index)

print(f"수입 합계: {df['수입'].sum()}")
print(f"지출 합계: {df['지출'].sum()}")