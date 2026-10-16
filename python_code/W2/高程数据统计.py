dem = []
d = ""
while d != "q":
    d = input("请输入高程")
    if d != "q":
        dem.append(float(d))
print(len(dem),max(dem),min(dem))
dem_vag = sum(dem)/len(dem)
print(dem_vag)

            