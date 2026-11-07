import pandas as pd
import numpy as np
from pathlib import Path

path = Path(".\poi.csv")
df = pd.read_csv(path)
df_test = df[(df["lon"] > 110) & (df["lon"] < 111) & (df["lat"] < 22) & (df["lat"] > 21)]
print(df_test)