import socket
import time

HOST = '192.168.163.129'
PORT = 11010

while True:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    s.sendall('led')
    data = s.recv(1024)
    print data[0:3]
    print data[3:6]
    print data[6:9]
    time.sleep(1)
s.close()
