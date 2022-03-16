from ast import Pass
from contextlib import nullcontext
from http.client import ImproperConnectionState

# Imports
import socket #Package used to simplify writing network servers
import sys #Allows python runtime environment manipulation
import threading #module that makes working with threads more simply

class Proxy:
    def __init__(self):
        self.listening_port = 6500
        self.buffer_size = 8192 #Used to define the maximum data bytes to be received at once
        self.max_connection = 7 #Used to define how many backlog of requests our sockets can handle before refusing new connections
        
    try:
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates a new socket object of socket type SOCK_STREAM and address family AF_INET
    