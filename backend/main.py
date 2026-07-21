from models import user, user_reg, login, change_password, delete, list_users

def main():
    while True:
        print("1 登录")
        print("2 退出")
        print("3 注册新用户")
        print("4 修改密码")
        print("5 删除用户")
        print("6 查看用户")
        choice = input("请输入选择：")
        if choice == "1":
            print(login())
        elif choice == "2":
            print("再见")
            break
        elif choice == "3":
            user_reg()
        elif choice == "4":
            change_password()
        elif choice == "5":
            delete()
        elif choice == "6":
            list_users()

main()