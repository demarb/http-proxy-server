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

        self.runtimeLabel = Label(self.root, text="Runtime: "+ self.lastrunningtime + "", bg="white")
        self.importantLabel = Label(self.root, text="IMPORTANT:\nConfigure proxy settings as \nlocalhost with \nport#: 4444", bg="red", fg="white")

        self.titleLabel.grid(row= 0, column=0, pady=10, ipady=10)
        self.runtimeLabel.grid(row= 3, column=0, pady=10)
        self.importantLabel.grid(row= 4, column=0, pady=10)

        self.startStop_btn = Button(self.root, text= "Start", padx=75, bg="#519744", fg="white", command=self.start_stopEvt)
        self.startStop_btn.grid(row=1, column=0, pady=10)

        self.logs_btn = Button(self.root, text="Logs", padx=75, bg="white", command=self.get_logs)
        self.logs_btn.grid(row=2, column=0, pady=10, padx=20)

        self.root.mainloop()

    def  start_stopEvt(self):
        if self.startStop_btn["text"]=="Start":
            self.startStop_btn["text"] = "Stop"
            self.startStop_btn.config(bg="#AE1111")
            sleep(3)

            self.server = Server()
            
            self.initial_time = datetime.datetime.utcnow()
            self.lastrunningtime = ""
            
            self.timer_thrd = threading.Thread(target = self.updateRunTime, args=(self.initial_time,))
            self.timer_thrd.setDaemon(True)
            self.timer_thrd.start()
            
            
            
            self.thrd = threading.Thread(target = self.server.establish_connection, args=())
            self.thrd.setDaemon(True)
            
            self.thrd.start()
            
        elif self.startStop_btn["text"]=="Stop":
            
            self.startStop_btn["text"] = "Start"
            self.startStop_btn.config(bg="#519744")
            
            self.server.dead =True
            

    def get_logs(self):
        logs_path = ""
        import webbrowser
        
        for charac in str(self.my_dir):
            if charac == "\\":
                logs_path += "/"
            else:
                logs_path+= charac
        
        webbrowser.open('file:///' + logs_path)

    def updateRunTime(self, initial_time):
        while self.server.dead == False:
            self.current_time = datetime.datetime.utcnow()
            self.lastrunningtime = str(self.current_time -  initial_time)
            self.runtimeLabel["text"] = "Runtime: "+ self.lastrunningtime + ""

View()