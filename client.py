__author__ = 'Misys'
import socket

HOST = input("IP address of the host: ")
PORT = 2015

connection = socket.socket()

print("Connecting....")
try:
    connection.connect((HOST, PORT))
except:
    print("Connection failed!")
    quit()
print("Connection Successful!")

while True:
    message = input(">")
    try:
        connection.sendall(message.encode())
    except:
        print("Couldn't find host! This is probably because you've been disconnected.")
        quit()

connection.close()