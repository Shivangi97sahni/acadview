#1
from tkinter import *
r= Tk()
r.title("Welcome")
lbl = Label(r, text="Hello world").grid(column=0, row=0)
btn = Button(r, text="Exit",command=exit).grid(column=0, row=1)
r.mainloop()

#2
from tkinter import *
r= Tk()
r.title("Welcome")
lbl = Label(r, text="Hello world").grid(column=0, row=0)
btn = Button(r, text="Exit", command=exit).grid(column=0, row=1)
def fun():
    print("welcome to the hello world")
btn1=Button(r,text="click me",command=fun).grid(column=1,row=1)
r.mainloop()

#3
from tkinter import *
root = Tk()
label=Label(root,text="old text")
def click():
  label.config(text="ghjjg")
b1 = Button(root, text="click me",command=click)
label.pack()
b1.pack()
root.mainloop()

#4

from tkinter import *
r = Frame()
r.pack()
ent = Entry(r)
ent.pack(side=TOP)
ent.insert(0,"type here....")
ent.focus()
def display():
    print("This is the input:",ent.get())
widget = Button(r,text="Hello GUI World",command=display)
widget.pack(side=LEFT,expand=YES,fill=Y)
widget.mainloop()