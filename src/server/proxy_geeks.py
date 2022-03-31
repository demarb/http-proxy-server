import configparser
import socket
import threading
from time import sleep

class Server:
    #Server Constructor
    def __init__(self):
        
        print("[SERVER BOOTING] : ...")
        
        self.create_config_file()

        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        
        self.dead = False
        
        
        self.HOST_NAME = self.config['SERVERCONFIG']['HOST_NAME']
        self.BIND_PORT = int(self.config['SERVERCONFIG']['BIND_PORT'])
        self.MAX_REQUEST_LEN = int(self.config['SERVERCONFIG']['MAX_REQUEST_LEN'])
        self.CONNECTION_TIMEOUT = int(self.config['SERVERCONFIG']['CONNECTION_TIMEOUT'])

        # Create a TCP socket
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Re-use the socket
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # bind the socket to a public host, and a port   
        self.serverSocket.bind((self.HOST_NAME, self.BIND_PORT))
        
        self.serverSocket.listen(10) # become a server socket
        # self.__clients = {}
        
        print(f"[SERVER LISTENING] : Server listening on port {self.BIND_PORT}")
    
    #Method called by view to establish connection and allow listening    
    def establish_connection(self):
        while True:
            #Check for flag if main thread should be killed
            if self.dead == True:
                print(f"[MAIN THREAD INTERRUPTED] : Terminating listening stream connection")
                break
            
            # Establish the connection
            (clientSocket, client_address) = self.serverSocket.accept()
            print(f"[NEW CONNECTION] : {client_address} connected.")
            print(f"[ACTIVE THREAD COUNT] : {threading.active_count()}")
            
            d = threading.Thread(target = self.proxy_thread, args=(clientSocket, client_address))
            d.setDaemon(True)
            d.start()
            sleep(1)
    
    #Cleans up request and sends data back and forth between client, server and web host    
    def proxy_thread(self, clientSocket, client_address):       
        # get the request from browser
        request = clientSocket.recv(self.MAX_REQUEST_LEN)
        print(f"[REQUEST LENGTH] : {len(request)}")

        # parse the first line
        first_line = request.split(b'\n')[0]

        # get url
        url = first_line.split(b' ')[1]
        
        http_pos = url.find(b"://") # find pos of ://
        if (http_pos==-1):
            temp = url
        else:
            temp = url[(http_pos+3):] # get the rest of url

        port_pos = temp.find(b":") # find the port pos (if any)

        # find end of web server
        webserver_pos = temp.find(b"/")
        if webserver_pos == -1:
            webserver_pos = len(temp)

        webserver = ""
        port = -1
        if (port_pos==-1 or webserver_pos < port_pos): 

            # default port 
            port = 80 
            webserver = temp[:webserver_pos] 

        else: # specific port 
            port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
            webserver = temp[:port_pos] 
            
            ################################
            
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.settimeout(self.CONNECTION_TIMEOUT)
        s.connect((webserver, port))
        s_addr = (webserver, port)
        s.sendall(request)
        
        #Sends data until data sent completely sent or thread interrupted
        while 1:
            #Check for flag if thread should be killed
            if self.dead == True:
                print(f"[THREAD INTERRUPTED] : Terminated during data transmission")
                break
            
            
            # receive data from web server
            print(f"[SERVER] : Retrieving data from {s_addr}")
            data = s.recv(self.MAX_REQUEST_LEN)
            print(f"[DATA] : {len(data)} data from {s_addr}")

            
            if (len(data) > 0):
                print(f"[SERVER] : Sending data to {client_address}")
                clientSocket.send(data) # send to browser/client
            else:
                print(f"[SERVER] : Data Successfully sent to {client_address}")
                break
        
        clientSocket.close()
        s.close()

    def create_config_file(self):
            config_object = configparser.ConfigParser()
            
            config_object["SERVERCONFIG"] = {
            "HOST_NAME": "",
            "BIND_PORT": "4444",
            "MAX_REQUEST_LEN": "4096",
            "CONNECTION_TIMEOUT": "60"
            }

            #Write the above sections to config.ini file
            with open('config.ini', 'w') as conf:
                config_object.write(conf)
