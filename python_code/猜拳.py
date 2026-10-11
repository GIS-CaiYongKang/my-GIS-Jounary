import random
options = ['石头','剪刀','布']
while True:
    user = input("你想出什么？剪刀/石头/布/n如果想退出请输入q")
    if user == "q":
        print("游戏结束")
        break
    if user not in options:
        print("error")
        continue
    bot = random.choice(options)
    print(f"chu{bot}")
    if user == bot:
        print('ping')
    elif(user == '石头' and bot == '剪刀') or (user == '剪刀' and bot == '布') or (user == '布' and bot == '石头'):
        print('win')
    else:
        print('no')
