# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText

def send_email(toList, subject, content):
    mail_host = 'smtp.163.com'
    user = '*******'
    pwd = '*****'
    me = user

    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = ';'.join(toList)

    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(user,pwd)
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.close()
    except Exception, e:
        print str(e)

if __name__ == '__main__':
    send_email(["1206539220@qq.com"],'reminder','call me if you see')
