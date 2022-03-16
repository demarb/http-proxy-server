#Autogenerated imports; need to check their relevance
# from ast import Pass
# from contextlib import nullcontext
# from http.client import ImproperConnectionState

# Imports
import socket #Package used to simplify writing network servers
#import sys #Allows python runtime environment manipulation | Could use for exiting sys.exit()
import threading #module that makes working with threads more simply

class Proxy:
    def __init__(self):
        self.listening_port = 6500
        self.buffer_size = 8192 #Used to define the maximum data bytes to be received at once
        self.max_connection = 7 #Used to define how many backlog of requests our sockets can handle before refusing new connections
        self.skt = None
        # self.connection = None
        # self.address = None
        # self.data_stream = None
        
    def define_socket(self):
        #Our Server must create, bind, listen, then accept in that order where accept may repeat as needed
        
        try:
            self.skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates a new socket object of socket type SOCK_STREAM and address family AF_INET
            self.skt.bind(('', self.listening_port)) #Binds socket to address
            self.skt.listen(self.max_connection) #Enables our server to accept connections with maximum backlog specified by parameter passed
        except Exception as e:
            print(e)
            
        while True:
            try:
                self.accept_connection()
            except Exception as e:
                print(e)
                #self.skt.close()
                break # Need to exit our while loop more efficiently        
        
        self.skt.close()
            
    def accept_connection(self):
        connection, address = self.skt.accept() #Methods returns a key value pair of a new Socket object:connection and address bound to socket at next end of connection
        data_stream = connection.recv(self.buffer_size) # Stream of data being sent between our connection 
        #To be fixed:  start_new_thread(conn_string(connection, data_stream, address))
        
        