#!/usr/bin/python
# This script sends email with our Internet IP address
# whenever that IP changes
from __future__ import print_function
import smtplib, os, sys, time
from email.mime.image      import MIMEImage
from email.mime.multipart  import MIMEMultipart
from email.mime.text       import MIMEText
COMMASPACE = ', '
import subprocess
getip = ['dig','TXT','+short','o-o.myaddr.l.google.com','@ns1.google.com']

lastip = "1.1.1.1"

while(1) :
    proc = subprocess.Popen(getip, stdout=subprocess.PIPE)
    myip = proc.stdout.read().strip().split()[0]
    myip = myip[1:-1]
    if (myip == lastip) :
        print("Taking a nap...")
        time.sleep(30)
    else :
        time.sleep(10)
        server = smtplib.SMTP( "smtp.gmail.com", 587 )
        server.starttls()
        userpass = eval(open('secrets','r').read())
        server.login( userpass['login'], userpass['password'] )
        mess=myip
        msg = MIMEText(mess,'plain') # Container (outer) email message.
        msg['Subject'] = "IP " + myip
        msg['From'] = 'phagestat@gmail.com'
        msg['To'] = 'phagestat@gmail.com'
        server.sendmail('phagestat@gmail.com', 'phagestat@gmail.com', msg.as_string())
        server.quit()
        lastip = myip
        print("Sent email for new IP = " + str(myip))
        



