def coor_format(lon:float,lat:float):
    #这个函数的参数必须是整数或浮点数
    if not -180 <= lon <= 180:
        raise ValueError("请输入合适的值")
    if not -90 <= lat <= 90 :
        raise ValueError("请输入合适的值")
    lo_dir = "W" if lon < 0 else "E"
    la_dir = "S" if lat < 0 else "N"
    return f"经度：{abs(lon):.2f}°{lo_dir},纬度：{abs(lat):.2f}°{la_dir}"

while True:
    try:
        o = float(input("请输入经度"))
        a = float(input("请输入纬度"))
        print(coor_format(o,a))
        break
    except Exception as e:
        print(f"输入错误：{e},请重新输入！")
