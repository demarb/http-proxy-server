#proxxy Server
#this is what i have been working on, so far it has not run properly. the error is that it demand for the define of raw_input
from distutils.command.build_scripts import first_line_re
from email import message
from logging.config import listen
from re import L
import socket
import sys
from _thread import *

try:
    listing_port = raw_input("[*] Enter listening port number: ")
    listening_port = int(raw_input("[*] Enter listening port number: "))
except KeyboardInterrupt:
    print("\n [*] User Requesting an interrupt")
    print("[*] Apllication Exiting ....")
    sys.exit()

max_conn = 5 #max connection queues to hold
buffer_size = 4096 # max socket buffer size

def start():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #initiate socket
        s.bind(('', listening_port)) #bind socket for listen
        s.listen(max_conn) #start listing for incoming connection
        print("[*] initiate sockets complete")
        print("[*] socket binded successfull")
        print("[*] server start successful [ %d ]\n " % ((listening_port)))
    except Exception: #, e:  #run here if fail
        print("[*] unable to initialize socket")
        sys.exit(2)

    while 1:
        try:
            conn, addr = s.accept() #accept connection from client browser
            data = conn.recv(buffer_size) # recieve client data
            start_new_thread(conn_string, (conn, data, addr) ) #start threa
        except KeyboardInterrupt: # if blocked run
            s.close()
            print("\n [*] proxy server shutting down")
            sys.exit(1)
    s.close()

def conn_string(conn, data, addr):#client browser request appear here
    try:
        first_line = data.split('\n') [0]
        url = first_line.split(' ')[1]

        http_pos = url.find(" ://") #fing the position of ://
        if (http_pos==-1):
            temp = 1
        else:

            temp = url[http_pos+3:] # get the rest of the url

        port_pos = temp.find(" : ") #find the pos of the port if any

        webserver_pos = temp.find (" / ") #find the end of the web server
        if webserver_pos ==-1:
            webserver_pos = len(temp)
        webserver = " "
        port= -1
        if (port_pos==-1 or webserver_pos < port_pos): # deflault port
            port = 80 
            webserver = temp[:webserver_pos]
        else: #specific port
            port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
            webserver = temp[:port_pos]

        proxy_server(webserver, port, conn, addr, data)
    except Exception: #, e:
        pass


def proxy_server(webserver, port, conn, data, addr):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(data)

        while 1: #read on;y or data to from end webserver
            reply = s.recv(buffer_size)

            if (len(reply) > 0):
                conn.send(reply) #send reply to clieint
                #send notification tp proxy server
                dar = float(len(reply))
                dar = float(dar / 1024)
                dar = "%.3" % (str(dar))
                dar = "%s KB" % (dar)
                #print a custom message for request complete
                print("[*] Request Done: %s => %s <=" % (str(addr[0]), str(dar)))
            else: # break connection if receiving data fail
                break
        s.close()
        conn.close()
    except socket.error (value, message):
        s.close()
        conn.close()
        sys.exit(1)

start()
