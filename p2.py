import socket
from threading import Thread

mySocket = socket.socket()
mySocket.connect("127.0.0.1", 5431)

def send():
    while True:
        qwe = input("Число для отправки -> ")
        mySocket.send(qwe.encode("utf-8"))
        
def answer():
    while True:
        ans = mySocket.recv(1024)
        print(ans.decode("utf-8"))

tread1 = Thread(target=send)
tread2 = Thread(target=answer)
tread1.start()
tread2.start()