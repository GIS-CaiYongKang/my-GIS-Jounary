from pathlib import Path
import csv

path = Path('poi.csv')

with  path.open('r',encoding="utf-8") as file:
    lines = csv.reader(file)
    head_low = next(lines)
    print(f"表头是:{head_low}")
    for i,row in enumerate(lines):
        print(f"第{i+1}行的数据为：{row}")