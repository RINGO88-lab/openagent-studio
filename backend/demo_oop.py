user = {}
def user_reg():
    while True:
        user_account = input("请输入账号：")
        user_password = input("请输入密码")
        if user_account in user:
            print("该用户已被注册！重新注册")
            continue
        user[user_account] = user_password
        print("注册成功！")
        break

def login():
        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            user_account = input("请输入账号")
            user_password = input("请输入密码")
            if user_account in user and user_password == user[user_account]:
                return '登录成功'
            else:
                attempts += 1
                print(f'账号或密码错误，还剩{max_attempts - attempts}次机会')
        return '已禁止登录'


def change_password():
    while True:
        account = input("请输入账号：")
        if account not in user:
            print("账号不存在")
            continue
        else:
            password = input("请输入旧密码")
        if password == user[account]:
            new_password = input("请输入修改后的密码")
            user[account] = new_password
            print("修改成功")
            break


def delete():
    account = input("请输入账号：")
    if account not in user:
        print("账号不存在")
        return
    confirm = input(f"确认删除 {account}？(输入yes确认)：")
    if confirm == "yes":
        del user[account]
        print("删除成功")
    else:
        print("已取消")


def list_users():
    if not user:
        print("暂无用户")
        return
    print("用户列表：")
    for u in user:
        print(f"  {u}")