name_list = ["Tom","Cai","Kang"]
#print(name_list.index("Cai",0,2))
name = input("请输入用户名")

if name in name_list:
            print("该用户名已存在")
else:
            name_list.append(name)
print(name_list)