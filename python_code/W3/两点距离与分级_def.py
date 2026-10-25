import math
def point(lon:float,lat:float) -> tuple:
    if not isinstance(lon,(float,int)) or isinstance(lon,bool):
        raise TypeError("请输入正确格式的值")
    if not isinstance(lat,(float,int)) or isinstance(lat,bool):
        raise TypeError("请输入正确格式的值")
    if not -180 <= lon <= 180:
        raise ValueError("请输入-180~180的经度")
    if not -90 <= lat <= 90:
        raise ValueError("请输入-90~90的纬度")
    return lon,lat

def distance(p1:tuple,p2:tuple) -> float:
    delta_lon = p1[0] - p2[0]
    delta_lat = p1[1] - p2[1]
    avg_lat = (p1[1] + p2[1])/2
    lat_rad = math.radians(avg_lat)
    S_lo = delta_lon * 111 * math.cos(lat_rad)
    S_la = delta_lat * 111
    S = math.sqrt(S_lo**2 + S_la**2)
    return S

def distance_level(d) -> int:
    if  not isinstance (d,(float,int)) or isinstance(d,bool):
        raise TypeError("请输入浮点数或整数")
    if d < 1 :
        return 1
    elif d < 5:
        return 2
    elif d >= 5:
        return 3 

point_list = []
i = 1
while i <= 2: 
    try:
        lon = float(input("经度："))
        lat = float(input("纬度："))
        point_list.append(point(lon,lat))
        i += 1
    except (TypeError,ValueError) as e:
        print(f"输入错误：{e}，请重新输入！")

print(f"两个点的经纬度为：{point_list}")
print(f"两点之间的距离是：{distance(point_list[0],point_list[1]):.2f}km")
print(f"距离等级为：{distance_level(distance(point_list[0],point_list[1]))}")


