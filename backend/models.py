class UserManager:
    def __init__(self):
        self.users = {}

    def user_reg(self):
        while True:
            a = input("请输入账号：")
            p = input("请输入密码：")
            if a in self.users:
                print("已存在")
                continue
            self.users[a] = p
            print("注册成功")
            break

    def login(self):
        for i in range(3):
            a = input("请输入账号：")
            p = input("请输入密码：")
            if a in self.users and self.users[a] == p:
                return "登录成功"
        return "已禁止登录"

    def change_password(self):
        while True:
            a = input("请输入账号：")
            if a not in self.users:
                print("不存在")
                continue
            p = input("请输入旧密码：")
            if p == self.users[a]:
                self.users[a] = input("请输入新密码：")
                print("修改成功")
                break

    def delete(self):
        a = input("请输入账号：")
        if a not in self.users:
            print("不存在")
            return
        c = input("确认删除？(y/n)：")
        if c == "y":
            del self.users[a]
            print("删除成功")

    def list_users(self):
        if not self.users:
            print("暂无用户")
            return
        for u in self.users:
            print(u)

def main():
    um = UserManager()
    while True:
        c = input("1登录 2退出 3注册 4改密 5删除 6查看：")
        if c == "1": print(um.login())
        elif c == "2": break
        elif c == "3": um.user_reg()
        elif c == "4": um.change_password()
        elif c == "5": um.delete()
        elif c == "6": um.list_users()

if __name__ == "__main__":
    main()
