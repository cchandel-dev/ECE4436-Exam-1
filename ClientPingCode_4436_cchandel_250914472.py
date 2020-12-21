'''
Created on 18-Oct-2020

@author: 12267
'''
import time
from socket import *

for i in range(10):
        # Create a UDP socket
        clientSocket = socket(AF_INET,SOCK_DGRAM);
        clientSocket.settimeout(2.0)     # Set timeout to 2 seconds
        # Assign IP address and port number to socket
        serverName = '127.0.0.1';
        serverPort = 12000;
        message = input("Input lowercase sentence:");
        starttime = time.time();
        clientSocket.sendto(message.encode(), (serverName, serverPort));
        modifiedMessage ='';
        while  modifiedMessage =='':
                modifiedMessage, clientaddress = clientSocket.recvfrom(2048);
                endtime = time.time();
                RTT= endtime-starttime;
                print ("Messaged received: " + modifiedMessage.decode());
                print("RTT: " + str(RTT));
