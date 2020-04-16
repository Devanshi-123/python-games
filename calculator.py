# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 10:26:47 2020

@author: DELL
"""

from tkinter import *
from tkinter import messagebox


window=Tk()
window.title(" Calculator")
window.geometry("250x400+300+300")
window.resizable(0,0)
data = StringVar()
lbl=Label(window,text="label",font=('Helvetica','20'),anchor= SE,bg="white",fg="black",textvariable=data)
lbl.pack(expand= True, fill = "both")


val= ""
A=0
operator=""

def btn0_pressed():
    global val
    val=val+"0"
    data.set(val)


def btn1_pressed():
    global val
    val=val+"1"
    data.set(val)


def btn2_pressed():
    global val
    val=val+"2"
    data.set(val)
    

def btn3_pressed():
    global val
    val=val+"3"
    data.set(val)
    

def btn4_pressed():
    global val
    val=val+"4"
    data.set(val)
    

def btn5_pressed():
    global val
    val=val+"5"
    data.set(val)
    

def btn6_pressed():
    global val
    val=val+"6"
    data.set(val)
    

def btn7_pressed():
    global val
    val=val+"7"
    data.set(val)
    

def btn8_pressed():
    global val
    val=val+"8"
    data.set(val)
    

def btn9_pressed():
    global val
    val=val+"9"
    data.set(val)
    
def btnplus_pressed():
    global A
    global val
    global operator
    A=int(val)
    val=val+"+"
    operator="+"
    data.set(val)
    
def btnminus_pressed():
    global A
    global val
    global operator
    A=int(val)
    val=val+"-"
    operator="-"
    data.set(val)
    
def btnmul_pressed():
    global A
    global val
    global operator
    A=int(val)
    val=val+"*"
    operator="*"
    data.set(val)
    
def btndiv_pressed():
    global A
    global val
    global operator
    A=int(val)
    val=val+"/"
    operator="/"
    data.set(val)
    
def btnC_pressed():
    global A
    global val
    global operator
    val = ""
    operator = ""
    A = 0
    data.set(val)
    
def result():
    global A
    global val
    global operator
    val2=val
    if operator == "+" :
        x=int((val2.split("+")[1]))
        c=A+x
        data.set(c)
        val=str(c)
    elif operator == "-" :
        x=int((val2.split("-")[1]))
        c=A-x
        data.set(c)
        val=str(c)
    elif operator == "*" :
        x=int((val2.split("*")[1]))
        c=A*x
        data.set(c)
        val=str(c)
    elif operator == "/":
        x=int((val2.split("/")[1]))
        if x==0:
            A=0
            val=""
            data.set(val)
            messagebox.showerror("Sorry","Division by 0 not allowed")
        else:
            c=A/x
            data.set(c)
            val=str(c)
        
        








btnrow1=Frame(window)
btnrow1.pack(expand=True,fill="both")

btnrow2=Frame(window)
btnrow2.pack(expand=True,fill="both")

btnrow3=Frame(window)
btnrow3.pack(expand=True,fill="both")

btnrow4=Frame(window)
btnrow4.pack(expand=True,fill="both")

btn1 = Button(btnrow1,text="1",font=("Helvetica","22"),relief=GROOVE,border=0,command = btn1_pressed)
btn1.pack(expand=True,fill="both",side= LEFT)
btn2 = Button(btnrow1,text="2",font=("Helvetica","22"),relief=GROOVE,border=0,command = btn2_pressed)
btn2.pack(expand=True,fill="both",side= LEFT)
btn3 = Button(btnrow1,text="3",font=("Helvetica","22"),relief=GROOVE,border=0,command = btn3_pressed)
btn3.pack(expand=True,fill="both",side= LEFT)
btnplus = Button(btnrow1,text="+",font=("Helvetica","22"),relief=GROOVE,border=0,command = btnplus_pressed)
btnplus.pack(expand=True,fill="both",side= LEFT)


btn4 = Button(btnrow2,text="4",font=("Helvetica","22"),relief=GROOVE,border=0,command = btn4_pressed)
btn4.pack(expand=True,fill="both",side= LEFT)
btn5 = Button(btnrow2,text="5",font=("Helvetica","22"),relief=GROOVE,border=0,command = btn5_pressed)
btn5.pack(expand=True,fill="both",side= LEFT)
btn6 = Button(btnrow2,text="6",font=("Helvetica","22"),relief=GROOVE,border=0,command = btn6_pressed)
btn6.pack(expand=True,fill="both",side= LEFT)
btnminus = Button(btnrow2,text="-",font=("Helvetica","22"),relief=GROOVE,border=0,command = btnminus_pressed)
btnminus.pack(expand=True,fill="both",side= LEFT)


btn7 = Button(btnrow3,text="7",font=("Helvetica","22"),relief=GROOVE,border=0,command = btn7_pressed)
btn7.pack(expand=True,fill="both",side= LEFT)
btn8 = Button(btnrow3,text="8",font=("Helvetica","22"),relief=GROOVE,border=0,command = btn8_pressed)
btn8.pack(expand=True,fill="both",side= LEFT)
btn9= Button(btnrow3,text="9",font=("Helvetica","22"),relief=GROOVE,border=0,command = btn9_pressed)
btn9.pack(expand=True,fill="both",side= LEFT)
btnmul = Button(btnrow3,text="*",font=("Helvetica","22"),relief=GROOVE,border=0,command = btnmul_pressed)
btnmul.pack(expand=True,fill="both",side= LEFT)


btnC = Button(btnrow4,text="C",font=("Helvetica","22"),relief=GROOVE,border=0,command = btnC_pressed)
btnC.pack(expand=True,fill="both",side= LEFT)
btn0 = Button(btnrow4,text="0",font=("Helvetica","22"),relief=GROOVE,border=0,command = btn0_pressed)
btn0.pack(expand=True,fill="both",side= LEFT)
btnequal = Button(btnrow4,text="=",font=("Helvetica","22"),relief=GROOVE,border=0,command=result)
btnequal.pack(expand=True,fill="both",side= LEFT)
btndiv = Button(btnrow4,text="/",font=("Helvetica","22"),relief=GROOVE,border=0,command = btndiv_pressed)
btndiv.pack(expand=True,fill="both",side= LEFT)


window.mainloop()