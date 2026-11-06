import pandas as pd
import numpy as np
from pathlib import Path

path = Path(".\poi.csv")
df = pd.read_csv(path)
print(df.head(5))
df.info()
print(df.describe())