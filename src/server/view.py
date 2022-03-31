import configparser
from time import sleep
from tkinter import *
from pathlib import Path
import datetime
import threading

from proxy_geeks import *


class View():
    def __init__(self):
        self.my_dir = Path(__file__).parent

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

            self.server = Server()
            self.threadFlag = False
            self.thrd = threading.Thread(target = self.server.establish_connection, args=())
            self.thrd.setDaemon(True)
            
            self.thrd.start()
            
        elif self.startStop_btn["text"]=="Stop":
            
            self.startStop_btn["text"] = "Start"
            self.startStop_btn.config(bg="#519744")
            
            self.server.dead =True
            

    def get_logs(self):
        pass

    def updateRunTime(self, initial_time):
        sleep(5)
        current_time = datetime.datetime.utcnow()
        print("Current "+ str(current_time))
        self.lastrunningtime = str(current_time -  initial_time)
        print(self.lastrunningtime)

View()