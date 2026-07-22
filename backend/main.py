from models import UserManager

def main():
    um = UserManager()
    while True:
        c = input("1登录 2退出 3注册 4改密 5删除 6查看：")
        if c == "1":
            a = input("账号：")
            p = input("密码：")
            print(um.login(a, p))
        elif c == "2":
            break
        elif c == "3":
            a = input("账号：")
            p = input("密码：")
            print(um.register(a, p))
        elif c == "4":
            a = input("账号：")
            o = input("旧密码：")
            n = input("新密码：")
            print(um.change_password(a, o, n))
        elif c == "5":
            a = input("账号：")
            c2 = input("确认？(y): ")
            if c2 == "y":
                print(um.delete(a))
        elif c == "6":
            print(um.list_users())

if __name__ == "__main__":
    main()
