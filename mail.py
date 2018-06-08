#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import os
import sys
import getopt
import smtplib
import email.mime.text
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from subprocess import *
reload (sys)
sys.setdefaultencoding('utf8')
def gmailsend(username,password,mailfrom,mailto,subject,content):
    HOST = 'smtp.gmail.com'
    PORT = 25
    try:
        msg = MIMEText(unicode(content).encode('utf-8'))
        msg['from'] = mailfrom
        msg['to'] = mailto
        msg['Reply-To'] = mailfrom
        msg['Subject'] = subject
        smtp = smtplib.SMTP(HOST,PORT)
        smtp.set_debuglevel(0)
        smtp.starttls()
        smtp.login(username,password)
        smtp.sendmail(mailfrom, mailto, msg.as_string())
        print msg.as_string()
        smtp.close()
    except Exception,err:
        print "Send mail failed. Error: %s" % err
def main():
    to=sys.argv[1]
    subject=sys.argv[2]
    content=sys.argv[3]
    gmailsend('aikeredward@gmail.com','undufrbrqlokvthn','aikeredward@gmail.com',to,subject,content)
if __name__ == "__main__":
    main()
