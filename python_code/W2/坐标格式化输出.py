while True:
    try:
        longitude = float(input("请输入经度"))
        latitude = float(input("请输入纬度"))
        if not(-180 <= longitude <= 180):
            raise ValueError("请输入适当的经度")
        if not(-90 <= latitude <= 90):
            raise ValueError("请输入适当的纬度")           
    except ValueError as e:
        error_msg = str(e) or "请输入数字格式的经纬度"
        print(f"输入有误：{error_msg}，请重新输入")
    else:
        name_lo = "E" if longitude > 0 else "W"
        name_la = "N" if latitude > 0 else "S"
        print(f"经度：{abs(longitude):.2f}°{name_lo},纬度：{abs(latitude):.2f}°{name_la}")
        break
    
        
