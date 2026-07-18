import random
b = random.randint(1,100)
while True:
    a = int(input("请输入数字:"))
    if a == b:
        print(f"猜对了，数字是{b}")
        break
    elif a > b:
        print(f"猜错了，数字大了，重新输入")
        continue
    else:
        print("猜错了，数字小了，请重新输入")
        continue

account = "123456"
password = "123"
total=0
while total<3:
    a = input("请输入账号：")
    b = input("请输入密码：")
    if a==account and b==password:
        print("成功")
        break
    else:
        total+=1
        print("错误")
        if total < 3:
            print(f"你还有{3-total}次机会")
            continue
        else:
            print("禁止登录")

a = float(input("请输入成绩："))
if a>=90 and a<=100:
    print("优秀")
elif a>=80 and a<90:
    print("良好")
elif a>=70 and a<80:
    print("中等")
elif a>=60 and a<70:
    print("及格")
elif a>=0 and a<60:
    print("不及格")
else:
    print("成绩无效")






