from tkinter import*
from tkinter import ttk
from ttkthemes import ThemedTk
import random

window=ThemedTk(theme='yaru')
window.title("Guess the number")
window.geometry('500x400')
window.configure(bg="#dfb6ea")

num=0
a=0
m=0
tries=0

def leave():
    window.destroy()

def randomnumber():
    global num
    global m
    num = random.randint(0, 100)
    m=str(num)


def ent(event):
    global tries
    a = entry.get()
    tries=tries+1

    trieslabel.configure(text="TRIES:"+str(tries))

    if  a>m:
        imagelabel.configure(image=downarrowphoto)
    elif a<m:
        imagelabel.configure(image=uparrowphoto)
    else:
        imagelabel.configure(image=correctphoto)
        entry.configure(state="disabled")
    entry.delete(0, END)

dicephoto=PhotoImage(file="dice.png",)
correctphoto=PhotoImage(file="correct.png")
uparrowphoto=PhotoImage(file="uparrow.png")
downarrowphoto=PhotoImage(file="downarrow.png")
logophoto=PhotoImage(file="logo.png")

label1=Label(window,text="uess The Number",font=("Stencil",25),bg="#dfb6ea",fg="#610F7F")
instlabel=Label(window,text="In this game you will have to find the number\nthat was randomly chosen!\n"
                                "Try to guess it with the least possible tries",font=("Arial",15),bg="#dfb6ea",fg="#610F7F")
imagelabel=Label(window,bg="#dfb6ea",image=dicephoto)
imagelabel2=Label(window,bg="#dfb6ea",image=logophoto)
entry=ttk.Entry(window,text="",font=("Arial",12),width=45,)
buttonrandom=ttk.Button(window,text="RANDOM",command=randomnumber())
buttonexit=ttk.Button(window,text="EXIT",command=leave)
window.bind('<Return>',ent)
trieslabel=Label(window,text="TRIES:",font=("Arial",12),bg="#dfb6ea",fg="#4D7EA8")

label1.place(x=120,y=40)
instlabel.place(x=50,y=80)
imagelabel.place(x=70,y=200)
buttonrandom.place(x=350,y=200)
entry.place(x=50,y=350)
buttonexit.place(x=350,y=250)
trieslabel.place(x=230,y=160)
imagelabel2.place(x=68,y=5)

window.mainloop()

