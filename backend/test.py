re_account = "123456"
re_password = "123456"

account = input("账号：")
password = input("请输入密码：")

if account == re_account and password == re_password:
    print("登录成功")
else:
    print("登录失败")


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="\t")
    print()

for i in range(1,7):
    for j in range(1,i+1):
        print(j,end="\t")
    print()

m = int(input("请输入个数"))
for i in range(m):
    for j in range(m):
        if (i+j)%2==0:
            print(f"□",end="\t")
        else:
            print(f"■",end="\t")
    print()