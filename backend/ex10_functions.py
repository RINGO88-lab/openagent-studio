import random

def guess_number():
    target = random.randint(1, 100)
    while True:
        try:
            guess = int(input('请输入数字：'))
        except ValueError:
            print('请输入有效数字')
            continue
        if guess > target:
            print('猜大了')
        elif guess < target:
            print('猜小了')
        else:
            print(f'猜对了，答案是{target}')
            break

def login_check():
    correct_account = '123456'
    correct_password = '123'
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        account = input('请输入账号：')
        password = input('请输入密码：')
        if account == correct_account and password == correct_password:
            return '登录成功'
        else:
            attempts += 1
            print(f'账号或密码错误，还剩{max_attempts - attempts}次机会')
    return '已禁止登录'

def grade_score():
    try:
        score = float(input('请输入成绩：'))
    except ValueError:
        print('请输入有效数字')
        return
    if 90 <= score <= 100:
        print('优秀')
    elif 80 <= score < 90:
        print('良好')
    elif 70 <= score < 80:
        print('中等')
    elif 60 <= score < 70:
        print('及格')
    elif 0 <= score < 60:
        print('不及格')
    else:
        print('成绩无效')

if __name__ == '__main__':
    choice = input('选择功能（1-猜数字 2-登录 3-成绩）：')
    if choice == '1':
        guess_number()
    elif choice == '2':
        result = login_check()
        print(result)
    elif choice == '3':
        grade_score()
    else:
        print('无效选择')
