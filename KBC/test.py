from tkinter import *
import random as rd
import time as t
root=Tk()
to='ho'
def work():
    root.config(bg='black')
    centerlabel.destroy()
image=PhotoImage(file='Image\\50-50.png')
centerlabel=Button(root,image=image,bg='black',width=300,height=200,command=work,to='hi')
centerlabel.grid(row=0,column=0)

root.mainloop()