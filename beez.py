from __future__ import print_function
import poplib

userpass = eval(open('secrets','r').read())
print(userpass)
M = poplib.POP3_SSL('pop.googlemail.com','995')
M.user(userpass['login'])
M.pass_(userpass['password'])
print(M.getwelcome())
numMessages = len(M.list()[1])
print(str(numMessages)+ " messages available");
for m in range(numMessages):
    j = M.retr(m+1)[1]
    for k in j:
        if "Subject: " in k :
            print(str(m)+": "+ k)
print("END OF Subjects")






