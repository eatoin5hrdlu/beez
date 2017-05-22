#!/usr/bin/python
from __future__ import print_function
import poplib, time, subprocess

userpass = eval(open('secrets','r').read())

def getCurrentIP() :
    M = poplib.POP3_SSL('pop.googlemail.com','995')
    M.user(userpass['login'])
    M.pass_(userpass['password'])
    print(M.getwelcome())
    numMessages = len(M.list()[1])
    print(str(numMessages)+ " messages available");
    header = "Subject: IP "
    hlen = len(header)
    for m in range(numMessages):
        latest = numMessages-m
        j = M.retr(latest)[1]
        for k in j:
            if header in k :
                myip = k[hlen:]
                return(myip)
                break
    return('1.1.1.1')
    
lastIP = '1.1.1.1'
myIP   = '1.2.3.4'
while(1) :
    myIP = getCurrentIP()
    if (lastIP == myIP) :
        print("IPs are the same")
        time.sleep(30)
    else :
        lastIP = myIP
    print("LAUNCH: ssh -R 21847:localhost:21847 peter@"+myIP)
    subprocess.call(["ssh","-R","21847:localhost:21847","peter@"+myIP])
    print("returned from ssh sesssion")
    time.sleep(10)
        






