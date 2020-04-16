# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:46:37 2020

@author: DELL
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:45:09 2020

@author: DELL
"""

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
window = Tk()


window.title("Ready to hang! if not guess the correct word in less than 4 chances")
window.geometry("800x500")




chances=5;
image_paths=['hang.jpg','img1.jpg','img2.jpg','img3.jpg','img4.png','img5.jpg']

img = Image.open(image_paths[chances])
img = img.resize((200,200),Image.ANTIALIAS)
img= ImageTk.PhotoImage(img)


panel=Label(window,image = img)
panel.grid(row=0,column=0)

answer_arr = []




def clicked(alphabet):
    global chances
    answer="INVERT";
    if alphabet in answer:
        if alphabet=='I':
            btn01["text"] = alphabet;
        elif alphabet=='N':
            btn02["text"] = alphabet;
        elif alphabet=='V':
            btn03["text"] = alphabet;
        elif alphabet=='E':
            btn04["text"] = alphabet;
        elif alphabet=='R':
            btn05["text"] = alphabet;
        elif alphabet=='T':
            btn06["text"] = alphabet;
    else:
        chances=chances-1;
        txt="Chances Remaining" + str(chances);
        label1.configure(text=txt)
        image = Image.open(image_paths[chances])
        image = image.resize((200,200),Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(image)
        
        panel.configure(image=imgnew)
        panel.image = imgnew
            
        if chances<0:
            messagebox.showinfo("Oops","no more chances left,you are hanged")
            window.destroy()
    if btn01["text"]=='I' and btn02["text"]=='N'and btn03["text"]=='V'and btn04["text"]=='E' and btn05["text"]=='R' and btn06["text"]=='T' :
        messagebox.showinfo("Congratulations","Great u guessed it right")
        window.destroy()
    print(chances)
        
    
btn01 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','15'))
btn01.grid(row=0,column=1)
btn02 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','15'))
btn02.grid(row=0,column=2)
btn03 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','15'))
btn03.grid(row=0,column=3)
btn04 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','15'))
btn04.grid(row=0,column=4)
btn05 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','15'))
btn05.grid(row=0,column=5)
btn06 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','15'))
btn06.grid(row=0,column=6)

btn1 = Button(window,text="A",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("A"))
btn1.grid(row=1,column=1)
btn2 = Button(window,text="R",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("R"))
btn2.grid(row=1,column=2)
btn3 = Button(window,text="B",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("B"))
btn3.grid(row=1,column=3)
btn4 = Button(window,text="Z",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("Z"))
btn4.grid(row=1,column=4)
btn5 = Button(window,text="T",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("T"))
btn5.grid(row=1,column=5)
btn6 = Button(window,text="I",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("I"))
btn6.grid(row=1,column=6)
btn7 = Button(window,text="C",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("C"))
btn7.grid(row=1,column=7)
btn8 = Button(window,text="X",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("X"))
btn8.grid(row=1,column=8)
btn9 = Button(window,text="O",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("O"))
btn9.grid(row=2,column=2)
btn10 = Button(window,text="Y",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("Y"))
btn10.grid(row=2,column=3)
btn11 = Button(window,text="P",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("P"))
btn11.grid(row=2,column=4)
btn12 = Button(window,text="N",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("N"))
btn12.grid(row=2,column=5)
btn13 = Button(window,text="D",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("D"))
btn13.grid(row=2,column=6)
btn14 = Button(window,text="W",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("W"))
btn14.grid(row=2,column=7)
btn15 = Button(window,text="V",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("V"))
btn15.grid(row=3,column=3)
btn16 = Button(window,text="S",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("S"))
btn16.grid(row=3,column=4)
btn17 = Button(window,text="L",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("L"))
btn17.grid(row=3,column=5)
btn18 = Button(window,text="U",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("U"))
btn18.grid(row=3,column=6)
btn19 = Button(window,text="M",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("M"))
btn19.grid(row=4,column=4)
btn20 = Button(window,text="E",bg="sky blue",fg="black",width=3,height=1,font=('Helvetica','15'),command=lambda: clicked("E"))
btn20.grid(row=4,column=5)

label1 = Label(window,text="Chances reamaining 5")
label1.grid(row=5,column=0)



window.mainloop()


        
