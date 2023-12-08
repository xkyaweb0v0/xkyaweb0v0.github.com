def verify_code(user_code, email_code):
    if user_code == email_code:
        print("验证码正确！")
    else:
        print("验证码错误！")
