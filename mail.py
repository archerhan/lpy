# 
# Description: 
# Author: ArcherHan
# Date: 2020-12-17 18:20:52
# LastEditors: ArcherHan
# LastEditTime: 2020-12-17 18:29:06
#

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    sender = 'archerhan1990@outlook.com'
    receivers = ['1158208694@qq.com']
    message = MIMEText('用Python发送邮件示例代码', 'plain', 'utf-8')
    message['Form'] = Header('Archer', 'utf-8')
    message['To'] = Header('JJ', 'utf-8')
    message['Subject'] = Header('示例代码邮件主题', 'utf-8')
    smtper = SMTP('smtp.outlook.com')
    smtper.login(sender, '999')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成')


if __name__ == "__main__":
    main()