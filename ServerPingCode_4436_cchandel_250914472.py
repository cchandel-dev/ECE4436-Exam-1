'''
Created on 18-Oct-2020

@author: 12267
'''
# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(("127.0.0.1", 12000))
while True:
# Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
# Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(2048)
    print("message recieved: " + message.decode())
# Capitalize the message from the client
    message = message.decode().upper()
# If rand is less is than 3, we consider the packet lost and do not respond
    if rand < 3:
        print("loss" + str(rand))
# Otherwise, the server responds
    else:
        print("message sending")
        serverSocket.sendto(message.encode(), address)
        print("message sent")