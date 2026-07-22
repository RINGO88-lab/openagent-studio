class UserManager:
    def __init__(self):
        self.users = {}

    def register(self, account, password):
        if account in self.users:
            return "已存在"
        self.users[account] = password
        return "注册成功"

    def login(self, account, password):
        if account in self.users and self.users[account] == password:
            return "登录成功"
        return "账号或密码错误"

    def change_password(self, account, old_pw, new_pw):
        if account not in self.users:
            return "账号不存在"
        if self.users[account] != old_pw:
            return "旧密码错误"
        self.users[account] = new_pw
        return "修改成功"

    def delete(self, account):
        if account not in self.users:
            return "账号不存在"
        del self.users[account]
        return "删除成功"

    def list_users(self):
        if not self.users:
            return "暂无用户"
        return "\n".join(self.users.keys())
