"""邮件类"""
import smtplib
from email.mime.text import MIMEText

class SendMail(object):
    def __init__(self):
        #邮件服务器
        self.smtpserver="smtp.163.com"
        #发送邮件的地址
        self.sender="15171453782@163.com"
        #发送者的密码
        self.passwd="zhang123"

    def send(self,message,towho):
        #转成邮件文本
        msg=MIMEText(message)
        #标题
        msg['Subject']="来自帅哥的问候"
        #发送者
        msg['Sender']=self.sender
        # 创建SMTP服务器
        mailServer = smtplib.SMTP(self.smtpserver, 25)  # 25是端口号
        # 登录邮箱
        mailServer.login(self.sender, self.passwd)
        # 发送邮件
        mailServer.sendmail(self.sender, [towho,], msg.as_string())
        # 退出邮箱
        mailServer.quit()

