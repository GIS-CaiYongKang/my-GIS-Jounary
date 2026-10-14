"""
以下是两种写法（以后有机会还会改进）
只适用于两距离较小的点
import math
point1_longitude = float(input("请输入第一个点的经度"))
point1_latitude = float(input("请输入第一个点的纬度"))
point2_longitude = float(input("请输入第二个点的经度"))
point2_latitude = float(input("请输入第二个点的纬度"))
longitude = point1_longitude - point2_longitude
latitude = point1_latitude - point2_latitude
latitude_avg = math.radians((point1_latitude + point2_latitude)/2)
y = latitude * 111
x = longitude * 111 * math.cos(latitude_avg)
s_square = y**2 + x**2
s = math.sqrt(s_square)
print(s,end=" ") 
if s < 1:
    print("数量级：1")
elif 1 < s < 5:
    print("数量级：2")
else:
    print("数量级：3")
"""
import math
longitude_1 = []
latitude_1 = []
print("请分别输入要求的两点的经纬度")
for i in range(2):
    while True:
        try:
            longitude_1.append(float(input(f"第{i+1}个点的经度")))
            latitude_1.append(float(input(f"第{i+1}个点的纬度")))
            break
        except ValueError:
            print("请输入正确的值")
latitude = (latitude_1[0] - latitude_1[1]) * 111
latitude_vag = (latitude_1[0] + latitude_1[1])/2 * math.radians(latitude)
longitude = (longitude_1[0] - longitude_1[1]) * 111 *latitude_vag
s = math .sqrt(latitude**2 + longitude**2)
print(f"两点间距离为{s:.2f}km") 
if s < 1:
    print("数量级：1")
elif 1 < s < 5:
    print("数量级：2")
else:
    print("数量级：3")
    