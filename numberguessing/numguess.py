from tkinter import *
import tkinter
import tkinter.messagebox
import random

chotabheem=Tk()
chotabheem.minsize(600,600)
chotabheem.title("Number guessing game (NGG)")

def greet():

    myName=choco.get()
    tkinter.messagebox.showinfo("Name","Hello, "+ myName +" take a guess between 1-100")

number=random.randint(1,100)

def Pneumonoultramicroscopicsilicovolcanoconiosis():

    guess=sneeze.get()
    guess=int(guess)
    myName=choco.get()

    if(guess<number):
        tkinter.messagebox.showinfo("Low","Your guess is too low")
    
    elif(guess>number):
        tkinter.messagebox.showinfo("High","Your guess is too high")

    elif(guess==number):
        tkinter.messagebox.showinfo("Well","Well done!")



wellabel=Label(chotabheem,text="Welcome to NGG",font=("Arial",35,"bold"))
wellabel.pack()

name=Label(chotabheem,text="Plz put ur name/username: ",font=("calibri",18,"bold"))
name.place(x=10,y=120)

choco=Entry(chotabheem,width=25)
choco.place(x=30,y=170)

bus=Button(chotabheem,text="Insert",font=("calibri",12,"bold"),command=greet)
bus.place(x=300,y=170)

achoo=Label(chotabheem,text="Plz guess a number: ",font=("calibri",18,"bold"))
achoo.place(x=10,y=370)

sneeze=Entry(chotabheem,width=25)
sneeze.place(x=30,y=420)

car=Button(chotabheem,text="Guess",font=("calibri",12,"bold"),command=Pneumonoultramicroscopicsilicovolcanoconiosis)
car.place(x=300,y=420)




chotabheem.mainloop()