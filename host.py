__author__ = 'Misys'
import socket

HOST = ""
PORT = 2015

connection = socket.socket()
connection.bind((HOST, PORT))

size = 0
while size == 0:
    try:
        size = int(input("How many users should I allow? "))
    except:
        print("Couldn't convert to integer. Did you give me a number?")
        size = 0

print("Waiting for connections...")
connection.listen(size)
clientList = [None] * size
clientAddress = [None] * size
for i in range(size):
    clientList[i], clientAddress[i] = connection.accept()
    print("Client " + clientAddress[i][0] + " connected on port " + str(clientAddress[i][1]) + "!")

while True:
    for client in clientList:
        message = client.recv(1024)
        if message:
            print(message.decode())
