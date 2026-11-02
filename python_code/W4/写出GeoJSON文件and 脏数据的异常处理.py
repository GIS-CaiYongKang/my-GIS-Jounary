from pathlib import Path
import csv
import json
from coord_utils import point

input_path = Path('poi.csv')
out_path = Path('poi_test.json')
features = []

with input_path.open('r',encoding='utf-8') as f: 
    reader = csv.reader(f)
    head_line = next(reader)

    for row in reader:
        try:
            name = row[0]
            lon = float(row[1])
            lat = float(row[2])
            point(lon,lat)

            point_dict = {
                "type":"Feature",
                "geometry":{
                    "type":"Point",
                    "coordinates":[lon,lat]
                },
                "properties":{
                    "name":name
                }
            }

            features.append(point_dict)
        except (TypeError,ValueError):
            continue
geojson_data = {
    "type":"FeatureCollection",
    "features":features
}

with out_path.open('w',encoding='utf-8') as file:
    json.dump(geojson_data,file,ensure_ascii=False,indent=4)
print(f"运行成功！共写入了{len(features)}个有效的poi点。")