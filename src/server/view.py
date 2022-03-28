import configparser
from time import sleep
from tkinter import *
from pathlib import Path
import datetime
import threading

from proxy_geeks import setUpProxy
# from proxy_geeks import create_config_file, Server


class View():
    def __init__(self):
        self.my_dir = Path(__file__).parent
        # self.stop_thread =threading.Event()
        self.threadFlag = None

        self.root = Tk()
        self.root.title("Proxy")
        self.root.configure(bg="#1A1F1F")
        self.root.iconbitmap(self.my_dir / "assets/proxyserver16.ico")
        self.root.geometry("230x300")
        self.root.minsize(230, 300)
        self.root.maxsize(230, 300)


        self.titleLabel = Label(self.root, text="Proxy Server", font=("Courier", 18, "bold"), bg="#1A1F1F", fg="white")

        self.lastrunningtime = ""
        self.initial_time = datetime.datetime.utcnow()
        print("Initial "+ str(self.initial_time))

        self.runtimeLabel = Label(self.root, text="Runtime: "+ self.lastrunningtime + "", bg="white")
        self.importantLabel = Label(self.root, text="IMPORTANT:\nConfigure proxy settings as \nlocalhost with \nport#: 4444", bg="red", fg="white")

        self.titleLabel.grid(row= 0, column=0, pady=10, ipady=10)
        self.runtimeLabel.grid(row= 3, column=0, pady=10)
        self.importantLabel.grid(row= 4, column=0, pady=10)

        self.startStop_btn = Button(self.root, text= "Start", padx=75, bg="#519744", fg="white", command=self.start_stopEvt)
        # startStop_btn = Button(root, text= "Stop", padx=75, bg="#AE1111", fg="white", command=start_stopEvt)
        self.startStop_btn.grid(row=1, column=0, pady=10)

        self.logs_btn = Button(self.root, text="Logs", padx=75, bg="white", command=self.get_logs)
        self.logs_btn.grid(row=2, column=0, pady=10, padx=20)

        self.updateRunTime(self.initial_time)
        self.root.mainloop()

    def  start_stopEvt(self):
        if self.startStop_btn["text"]=="Start":
            self.startStop_btn["text"] = "Stop"
            self.startStop_btn.config(bg="#AE1111")
            sleep(3)
        
            self.threadFlag = False
            self.thrd = threading.Thread(target = setUpProxy, args=())
            self.thrd.setDaemon(True)
            
            self.thrd.start()
            
        elif self.startStop_btn["text"]=="Stop":
            
            self.startStop_btn["text"] = "Start"
            self.startStop_btn.config(bg="#519744")
            
            self.threadFlag = True
            

    def get_logs(self):
        pass

    def updateRunTime(self, initial_time):
        sleep(5)
        current_time = datetime.datetime.utcnow()
        print("Current "+ str(current_time))
        self.lastrunningtime = str(current_time -  initial_time)
        print(self.lastrunningtime)

    def endThread(self):
        # self.stop_thread.set()
        # self.thrd = None
        pass
    




# def  start_stopEvt():
    
    
#     if startStop_btn["text"]=="Start":
#         startStop_btn["text"] = "Stop"
#         startStop_btn.config(bg="#AE1111")
#         sleep(3)
    
#         thrd = threading.Thread(target = setUpProxy, args=())
#         thrd.setDaemon(True)
#         thrd.start()
        
#         # setUpProxy()
        
#     elif startStop_btn["text"]=="Stop":
        
#         startStop_btn["text"] = "Start"
#         startStop_btn.config(bg="#519744")
        
        

# def get_logs(self):
#     pass

# def updateRunTime(self, initial_time):
#     sleep(5)
#     current_time = datetime.datetime.utcnow()
#     print("Current "+ str(current_time))
#     lastrunningtime = str(current_time -  initial_time)
#     print(lastrunningtime)

# my_dir = Path(__file__).parent

# root = Tk()
# root.title("Proxy")
# root.configure(bg="#1A1F1F")
# root.iconbitmap(my_dir / "assets/proxyserver16.ico")
# root.geometry("230x300")
# root.minsize(230, 300)
# root.maxsize(230, 300)


# titleLabel = Label(root, text="Proxy Server", font=("Courier", 18, "bold"), bg="#1A1F1F", fg="white")

# lastrunningtime = ""
# initial_time = datetime.datetime.utcnow()
# print("Initial "+ str(initial_time))

# runtimeLabel = Label(root, text="Runtime: "+ lastrunningtime + "", bg="white")
# importantLabel = Label(root, text="IMPORTANT:\nConfigure proxy settings as \nlocalhost with \nport#: 4444", bg="red", fg="white")

# titleLabel.grid(row= 0, column=0, pady=10, ipady=10)
# runtimeLabel.grid(row= 3, column=0, pady=10)
# importantLabel.grid(row= 4, column=0, pady=10)

# startStop_btn = Button(root, text= "Start", padx=75, bg="#519744", fg="white", command=start_stopEvt)
# # startStop_btn = Button(root, text= "Stop", padx=75, bg="#AE1111", fg="white", command=start_stopEvt)
# startStop_btn.grid(row=1, column=0, pady=10)

# logs_btn = Button(root, text="Logs", padx=75, bg="white", command=get_logs)
# logs_btn.grid(row=2, column=0, pady=10, padx=20)

# updateRunTime(initial_time)
# root.mainloop()

View()