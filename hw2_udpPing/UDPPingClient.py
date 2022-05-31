import time
from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(1, 11):
    try:
        begin = time.time()
        message = "Ping {} {}".format(i, begin)
        clientSocket.sendto(message.encode(), ('127.0.0.1', 12000))
        recv = clientSocket.recv(1024)
        print(recv.decode())
    except timeout:
        print("Request timed out")

