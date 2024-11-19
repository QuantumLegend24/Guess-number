from tkinter import *
from tkinter.ttk import *
from time import strftime
import tkinter.font as font

root=Tk()
root.title("Clock in The Netherlands")
root.config(bg="white")

mytimeclocktimeclock_label=Label(root,font=("calibri",100,"bold"),background="black",foreground="white")
mytimeclocktimeclock_label.pack(anchor="center")

def time():

    string=strftime("%W:%H:%M:%S:%p")
    mytimeclocktimeclock_label.config(text=string)
    mytimeclocktimeclock_label.after(1000,time)


time()


root.mainloop()