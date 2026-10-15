try:
    longitude = float(input("请输入经度"))
    latitude = float(input("请输入纬度"))
except ValueError:
     print("请输入正确的经纬度（不带E/W/N/S的）")
else:
    name_lo = ["E","W"]
    name_la = ["N","S"]

    if longitude < 0:
        if latitude <0 :
            print(f"经度：{longitude:.2f}°{name_lo[1]}，纬度：{latitude:.2f}°{name_la[1]}")
        else:
             print(f"经度：{longitude:.2f}°{name_lo[1]}，纬度：{latitude:.2f}°{name_la[0]}")
    else:
        if latitude <0 :
            print(f"经度：{longitude:.2f}°{name_lo[0]}，纬度：{latitude:.2f}°{name_la[1]}")
        else:
            print(f"经度：{longitude:.2f}°{name_lo[0]}，纬度：{latitude:.2f}°{name_la[0]}")
        
