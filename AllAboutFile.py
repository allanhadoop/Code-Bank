import socket
import sys
import os,io
from _thread import *

HOST = ' '
PORT = 8888

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket created")
try:
    s.bind((HOST,PORT))
except socket.error as e:
    print("couldnot bind client")
    sys.exit()
print("bind successful")

s.listen(2)
def clienthead(conn):
    conn.send(("u r now connected to server, sending file").encode())
    newpath = os.path.dirname(__file__)
    relpath = "/order.txt"
    path = os.path.join(newpath,relpath)

#    path = 'C:\Users\allan\Desktop\order.txt'
    f = open(path,"r")
    g = f.readline().encode()
    while True:
        conn.send(g)
        print("sent success")
    conn.close()

while 1:
    conn,addr = s.accept()
    start_new_thread(clienthead,(conn,))
s.close()