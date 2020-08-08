"""
@author: Arpit Somani
"""

import string
dict={}
data=""
file=open("op_file.txt","w")
#this file must be empty, so that secret will written here.
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
with open("ip_file.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print("Secret is written")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
        print(data)
    file.close()
