__author__ = 'Misys'
import socket

HOST = ""
PORT = 2015

connection = socket.socket()
connection.bind((HOST, PORT))

print("Waiting for connections...")
connection.listen(1)
client, clientAddress = connection.accept()
print("Host " + str(clientAddress) + " connected!")

while True:
    message = client.recv(1024)
    if message:
        print(message.decode())

client.close()