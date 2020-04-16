# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 12:40:00 2020

@author: DELL
"""

from tkinter import *
from tkinter import messagebox
import nltk
from nltk.corpus import words
from time import gmtime,strftime
import time
from collections import Counter
nltk.download('words')
word_list = words.words()
Matrix_list=['a','r','b','z','t','n','d','h','m','v','s','x','l','u','g','y','p','k','c','o']


score=0


window = Tk()
window.title("Scrambling words")
window.geometry("600x500")


def checkspells():
    global score
    word = word_check.get();
    if word in word_list:
        dict = Counter(word)
        flag=1
        for key in dict.keys():
            if key not in Matrix_list:
                flag=0
        if flag==1 and len(word)>3:
            score=score+len(word)
            total="Score="+str(score)
            label.configure(text=total)
            print(word)
        else:
            messagebox.showinfo("check","No maching characters found or length is less than 3")
    else:
        print("no word")
        word_check.delete(0,'end')
        
        
def tick(time1=' '):
    time2 = time.strftime("%M:%S")
    if time2!=time1:
        time1=time2;
        timer.configure(text="After 1 min it will close automatically"+time2)
    
    timer.after(200,tick)

def quit_pro():
    messagebox.showinfo("Ooopss!!!","Times up!!! Total score"+str(score))
    window.destroy()
        
btn1= Button(window,text="A",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn1.grid(row=1,column=1)      
btn2= Button(window,text="R",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn2.grid(row=1,column=2) 
btn3= Button(window,text="B",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn3.grid(row=1,column=3) 
btn4= Button(window,text="Z",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn4.grid(row=1,column=4) 
btn5= Button(window,text="T",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn5.grid(row=1,column=5) 

btn6= Button(window,text="N",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn6.grid(row=2,column=1) 
btn7= Button(window,text="D",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn7.grid(row=2,column=2) 
btn8= Button(window,text="H",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn8.grid(row=2,column=3) 
btn9= Button(window,text="M",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn9.grid(row=2,column=4) 
btn10= Button(window,text="V",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn10.grid(row=2,column=5) 

btn11= Button(window,text="E",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn11.grid(row=3,column=1) 
btn12= Button(window,text="X",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn12.grid(row=3,column=2) 
btn13= Button(window,text="L",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn13.grid(row=3,column=3) 
btn14= Button(window,text="U",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn14.grid(row=3,column=4) 
btn15= Button(window,text="G",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn15.grid(row=3,column=5) 

btn16= Button(window,text="Y",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn16.grid(row=4,column=1) 
btn17= Button(window,text="P",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn17.grid(row=4,column=2) 
btn18= Button(window,text="K",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn18.grid(row=4,column=3) 
btn19= Button(window,text="C",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn19.grid(row=4,column=4) 
btn20= Button(window,text="O",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica',20))     
btn20.grid(row=4,column=5) 
        
word_check=Entry(window,width=50)
word_check.configure(highlightbackground="red",highlightcolor="red")
word_check.grid(row=5,column=0,columnspan=6)

btncheck=Button(window,text="submit",bg="green",fg="white",width=5,height=2,font=('Helvetica','10'),command=checkspells)     
btncheck.grid(row=5,column=10)
 
label=Label(window,text="score=0")
label.grid(column=11,row=5)

timer=Label(window,text="You have 1 min")
timer.grid(column=0,row=6,columnspan=6)

tick()
window.after(60000,quit_pro)

window.mainloop()
        
        
        
        
        
        
        
        