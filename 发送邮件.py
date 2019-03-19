"""发邮件"""
#发邮件的库
import smtplib

#邮件文本
from email.mime.text import MIMEText

#SMTP服务器
SMTPServer = "smtp.163.com"

#发邮件的地址
Sender = "15171453782@163.com"

#发送者邮箱的密码
passwd = "zhang123"

#设置发送的内容
message = "you are a good man "
#转换成邮件文本
msg = MIMEText(message)

#标题
msg["Subject"] = "来自帅哥的问候"

#发送者
msg["From"] = Sender

#创建SMTP服务器
mailServer = smtplib.SMTP(SMTPServer,25) #25是端口号
#登录邮箱
mailServer.login(Sender,passwd)
#发送邮件
mailServer.sendmail(Sender,['15171453782@163.com'],msg.as_string())
#退出邮箱
mailServer.quit()


