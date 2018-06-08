#!/usr/bin/env python
import smtplib  
import sys  
import email.mime.text  
# my test mail  
mail_username='aikeredward@gmail.com'  
mail_password='undufrbrqlokvthn'  
from_addr = mail_username  
to_addrs=('donxan@gmail.com')  
  
# HOST & PORT  
HOST = 'smtp.gmail.com'  
PORT = 25  
  
# Create SMTP Object  
smtp = smtplib.SMTP()  
print 'connecting ...'  
  
# show the debug log  
smtp.set_debuglevel(1)  
  
# connet  
try:  
    print smtp.connect(HOST,PORT)  
except:  
    print 'CONNECT ERROR ****'  
# gmail uses ssl  
smtp.starttls()  
# login with username & password  
try:  
    print 'loginning ...'  
    smtp.login(mail_username,mail_password)  
except:  
    print 'LOGIN ERROR ****'  
# fill content with MIMEText's object   
# msg = email.mime.text.MIMEText('Hi ,I am leehark')  
msg = email.mime.text.MIMEText(unicode(content).encode('utf-8')
msg['From'] = mail_username
# msg['To'] = to_addrs  
msg['To'] = sys.argv[1]
# msg['Subject']='hello , today is a special day'  
msg['Subject'] = subject
subject = sys.argv[2]
content = sys.argv[3]
print msg.as_string()  
smtp.sendmail(from_addr,to_addrs,subject,content)
smtp.quit() 
