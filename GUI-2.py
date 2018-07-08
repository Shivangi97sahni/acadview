#1
from tkinter import *
root=Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

DICT={'xyz':123,'qwe':456,'rty':789,'uio':101,'pas':121,'dfg':678,'hjk':564,'lzx':434,'cvb':343,'nmq':544}
mylist=Listbox(root,yscrollcommand=scrollbar.set)
for i in DICT:
    mylist.insert(END,i,DICT[i])
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)

#2
def insert():
    DICT['klk']=112
    print(DICT)

button=Button(root,text='Insertion',command=insert)
button.pack()
root.mainloop()