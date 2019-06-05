from socket import *
from random import randint


s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))

while True:
    tm = s.recv(1024)
    print('now time: %s' % tm.decode('ASCII'))
s.close()
