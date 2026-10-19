def coor_format(lon:float,lat:float):
    if not isinstance(lon,(int,float)) or isinstance(lon,bool):
        raise TypeError("经度需为数字")
    if not isinstance(lat,(int,float)) or isinstance(lat,bool):
        raise TypeError("纬度需为数字")
    if not -180 <= lon <= 180:
        raise ValueError("请输入合适的值")
    lo_dir = "W" if lon < 0 else "E"
    la_dir = "S" if lat < 0 else "N"
    print(f"经度：{abs(lon):.2f}°{lo_dir},纬度：{abs(lat):.2f}°{la_dir}")
coor_format(-166,38)  
