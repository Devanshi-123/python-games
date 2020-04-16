# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:29:18 2020

@author: DELL
"""

from tkinter import *
from tkinter import messagebox
window=Tk()




window.title("Welcome to the Gaming Zone")
window.geometry("500x500")


lbl=Label(window,text="Tic-Tac-toe Game",font=('Helvetica','15'))
lbl.grid(row=0,column=0)
lbl=Label(window,text="Player-1 :X",font=('Helvetica','10'))
lbl.grid(row=1,column=0)
lbl=Label(window,text="Player-2 :O",font=('Helvetica','10'))
lbl.grid(row=2,column=0)


turn=1;




def clicked1():
    global turn
    if btn1["text"]==" ":
        if turn==1:
            turn=2
            btn1["text"]="X"
        elif turn==2:
            turn=1
            btn1["text"]="O"
        check()
    else:
        messagebox.showinfo("Invalid","Invalid move try again!")

def clicked2():
    global turn
    if btn2["text"]==" ":
        if turn==1:
            turn=2
            btn2["text"]="X"
        elif turn==2:
            turn=1
            btn2["text"]="O"
        check()
    else:
        messagebox.showinfo("Invalid","Invalid move try again!")


def clicked3():
    global turn
    if  btn3["text"]==" ":
        if turn==1:
            turn=2
            btn3["text"]="X"
        elif turn==2:
            turn=1
            btn3["text"]="O"
        check()
    else:
        messagebox.showinfo("Invalid","Invalid move try again!")

def clicked4():
    global turn
    if btn4["text"]==" ":
        if turn==1:
            turn=2
            btn4["text"]="X"
        elif turn==2:
            turn=1
            btn4["text"]="O"
        check()
    else:
        messagebox.showinfo("Invalid","Invalid move try again!")

def clicked5():
    global turn
    if  btn5["text"]==" ":
        if turn==1:
            turn=2
            btn5["text"]="X"
        elif turn==2:
            turn=1
            btn5["text"]="O"
        check()
    else:
        messagebox.showinfo("Invalid","Invalid move try again!")


def clicked6():
    global turn
    if btn6["text"]==" ":
        if turn==1:
            turn=2
            btn6["text"]="X"
        elif turn==2:
            turn=1
            btn6["text"]="O"
        check()
    else:
        messagebox.showinfo("Invalid","Invalid move try again!")

        
def clicked7():
    global turn
    if btn7["text"]==" ":
        if turn==1:
            turn=2
            btn7["text"]="X"
        elif turn==2:
            turn=1
            btn7["text"]="O"
        check()
    else:
        messagebox.showinfo("Invalid","Invalid move try again!")
        
def clicked8():
    global turn
    if    btn8["text"]==" ":
        if turn==1:
            turn=2
            btn8["text"]="X"
        elif turn==2:
            turn=1
            btn8["text"]="O"
        check()
    else:
        messagebox.showinfo("Invalid","Invalid move try again!")
        
def clicked9():
    global turn
    if  btn9["text"]==" ":
        if turn==1:
            turn=2
            btn9["text"]="X"
        elif turn==2:
            turn=1
            btn9["text"]="O"
        check()
    else:
        messagebox.showinfo("Invalid","Invalid move try again!")
flag = 1


def check():
    global flag
    b1=btn1["text"]
    b2=btn2["text"]
    b3=btn3["text"]
    b4=btn4["text"]
    b5=btn5["text"]
    b6=btn6["text"]
    b7=btn7["text"]
    b8=btn8["text"]
    b9=btn9["text"]
    
    flag=flag+1;
    if b1==b2 and b1==b3 and b1=='X' or b1==b2 and b1==b3 and b1=='O':
        won(b1)
    if b4==b5 and b4==b6 and b4=='X' or b4==b5 and b4==b6 and b4=='O':
        won(b4)
    if b7==b8 and b7==b9 and b7=='X' or b7==b8 and b7==b9 and b7=='O':
        won(b7)
    if b1==b4 and b1==b7 and b1=='X' or b1==b4 and b1==b7 and b1=='O':
        won(b1)
    if b2==b5 and b2==b8 and b2=='X' or b2==b5 and b2==b8 and b2=='O':
        won(b2)
    if b3==b6 and b3==b9 and b3=='X' or b3==b6 and b3==b9 and b3=='O':
        won(b3)
    if b1==b5 and b1==b9 and b1=='X' or b1==b5 and b1==b9 and b1=='O':
        won(b1)
    if b3==b5 and b3==b7 and b3=='X' or b3==b5 and b3==b7 and b3=='O':
        won(b3)
    if flag==10:
        messagebox.showinfo("Tie","Try Again")
        window.destroy()
        
        
def won(player):
    ans="Game complete" + " " + player + " " + "Wins"
    messagebox.showinfo("Congratulations",ans)
    window.destroy()

btn1 = Button(window , text=" ", bg="yellow",fg="black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn1.grid(row=1,column=1)
btn2=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn2.grid(row=1,column=2)
btn3=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn3.grid(row=1,column=3)
btn4=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','20'),command=clicked4)
btn4.grid(row=2,column=1)
btn5=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','20'),command=clicked5)
btn5.grid(row=2,column=2)
btn6=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','20'),command=clicked6)
btn6.grid(row=2,column=3)
btn7=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','20'),command=clicked7)
btn7.grid(row=3,column=1)
btn8=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','20'),command=clicked8)
btn8.grid(row=3,column=2)
btn9=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','20'),command=clicked9)
btn9.grid(row=3,column=3)



window.mainloop()