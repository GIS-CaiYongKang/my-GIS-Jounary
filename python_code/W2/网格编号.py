while True:
    try:
        lon = float(input("请输入经度"))
        lat = float(input("请输入纬度"))
        break
    except ValueError:
        print("请输入正确的值")
longitude = lon*100
latitude = lat*100
print(f'转换后的网格ID为GRID-{latitude:.0f}-{longitude:.0f}')