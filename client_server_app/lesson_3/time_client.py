from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))
tm = s.recv(1024)                
s.close()
print("Текущее время: %s" % tm.decode('utf-8'))
