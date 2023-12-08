import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header

def send_email():
    # 发件人邮箱
    sender = 'hoshino_enroll@163.com'
    # 收件人邮箱（从用户填写的表单获取）
    recipient = 'recipient@example.com'  # 这里示例为收件人邮箱

    # 生成四位数的随机验证码
    verification_code = str(random.randint(1000, 9999))

    # 邮件内容
    subject = '欢迎注册聊天室'
    content = f'您好，欢迎注册目前还在测试中的，开发代号为hoshino的聊天室，以下是您的验证码: {verification_code}'

    # 邮件对象
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(sender)
    message['To'] = Header(recipient)
    message['Subject'] = Header(subject)

    try:
        # 连接SMTP服务器
        smtp_obj = smtplib.SMTP('smtp.163.com', 25)
        # 登录邮箱
        smtp_obj.login(sender, 'your_password')  # 请替换为发件人邮箱的密码

        # 发送邮件
        smtp_obj.sendmail(sender, recipient, message.as_string())
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送失败:', str(e))
    finally:
        # 断开连接
        smtp_obj.quit()

# 调用发送邮件函数
send_email()
