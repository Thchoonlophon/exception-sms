# C:\Python3.6
# -*- coding:utf-8 -*-
# Project: send_log
# File   : send_email
# @Author: Chenjin QIAN
# @Time  : 2018-09-05 08:03

import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

lpath_os = os.path.dirname(os.path.abspath(__file__))


class SendMail(object):
    def __init__(self, username, passwd, recv, recv_name, title, content, email_host=None,
                 cc=None, cc_name=None, file=None, port=25):
        """
        To init the class
        :param username: The username of sender
        :param passwd: The password of sender
        :param recv: The email address of receiver, the type of this param
                      can be string or list, if there are more than one receiver,
                      you can pass a list here
        :param recv_name: The name of receiver, the type as same as recv
        :param title: The subject of email
        :param content: The content of email
        :param email_host: The mail sending server, for a example: "smtp.163.com"
        :param cc: The cc of this email, the type as same as recv
        :param cc_name: The name of cc, the type as same as recv
        :param file: Email attachments, must be An absolute path
        :param port: The port number of the mail sending server, you can search
                      the actual port number which you wanna use, the default is 25.
        """
        # 发件人邮箱
        self.username = username
        # 邮箱三方客户端授权码
        self.passwd = passwd
        # 收件人
        self.recv = recv
        # 收件人姓名
        self.recv_name = recv_name
        self.cc = cc
        self.cc_name = cc_name
        # 邮件主题
        self.title = title
        # 邮件内容
        self.content = content
        # 附件
        self.file = file
        self.email_host = email_host
        self.port = port
        self.form1 = 'html'
        self.form2 = 'utf-8'
        self.smtp = smtplib.SMTP(self.email_host, port=self.port)

    def send_mail(self):
        msg = MIMEMultipart()
        # 发送内容的对象
        # 处理附件
        if self.file:
            file_path = '{}'.format(os.path.abspath(self.file))
            file_name = file_path.split("\\")[-1]
            att = MIMEApplication(open(self.file, 'rb').read())
            att.add_header('Content-Disposition', 'attachment', filename=file_name)
            msg.attach(att)
            # msg.attach(att)
        # 邮件正文的内容
        msg.attach(MIMEText(self.content, self.form1, self.form2))
        # 邮件主题
        msg['Subject'] = self.title
        # 发送者账号
        msg['From'] = Header(f'{self.username}<{self.username}>', 'utf-8')
        # 接收者账号列表
        if type(self.cc) == list:
            st = [f'{self.recv_name[i]}<{self.recv[i]}>' for i in range(len(self.cc))]
            string = ", ".join(st)
            msg["To"] = Header(string, 'utf-8')
        else:
            msg["To"] = Header(f'{self.recv_name}<{self.recv}>', 'utf-8')
        members = self.recv if type(self.recv) == list else [self.recv]
        if self.cc:
            if type(self.cc) == list:
                st = [f'{self.cc_name[i]}<{self.cc[i]}>' for i in range(len(self.cc))]
                string = ", ".join(st)
                msg["Cc"] = Header(string, 'utf-8')
                members += self.cc
            else:
                msg["Cc"] = Header(f'{self.cc_name}<{self.cc}>', 'utf-8')
                members.append(self.cc)

        # 发送邮件服务器的对象
        self.smtp.login(self.username, self.passwd)
        try:
            print(members)
            self.smtp.sendmail(self.username, members, msg.as_string())
        except Exception as e:
            print(e)

    def __del__(self):
        if self.smtp:
            self.smtp.quit()
