from tkinter import *
from random import*



#création de la fenêtre principal
fen = Tk()
fen.title("Vortex")
fen.minsize(710,500)
fen.maxsize(710,500)
fen.config(background="bisque")

list_int=[1,2,3,4,5,6,7,8,9]
tab=[]
win=[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

for k in range (3) :
    column=[]
    for i in range (3) :
        rnd=choice(list_int)
        list_int.remove(rnd)
        column.append(rnd)
    tab.append(column)

def vortex_1():

    first_tab=tab[0][0]
    tab[0][0]=tab[1][0]
    tab[1][0]=tab[1][1]
    tab[1][1]=tab[0][1]
    tab[0][1]=first_tab
    boitenb1=Frame(fen,bd=10,bg="#41B87F",relief=RAISED)
    boitenb1.place(x=200,y=100)
    labelnb1=Label(boitenb1,text=tab[0][0], width="6", height="3")
    labelnb1.grid()

    boitenb2=Frame(fen,bd=10,bg="#41B87F",relief=RAISED)
    boitenb2.place(x=325,y=100)
    labelnb2=Label(boitenb2,text=tab[1][0], width="6", height="3")
    labelnb2.grid()

    boitenb4=Frame(fen,bd=10,bg="#41B87F",relief=RAISED)
    boitenb4.place(x=200,y=200)
    labelnl4=Label(boitenb4,text=tab[0][1], width="6", height="3")
    labelnl4.pack()

    boitenb5=Frame(fen,bd=10,bg="#41B87F",relief=RAISED)
    boitenb5.place(x=325,y=200)
    labelnb5=Label(boitenb5,text=tab[1][1], width="6", height="3")
    labelnb5.grid()
    if tab == win:
        print("bravo")
def vortex_2():
    first_tab=tab[0][1]
    tab[0][1]=tab[1][1]
    tab[1][1]=tab[1][2]
    tab[1][2]=tab[0][2]
    tab[0][2]=first_tab

    boitenb4=Frame(fen,bd=10,bg="#41B87F",relief=RAISED)
    boitenb4.place(x=200,y=200)
    labelnl4=Label(boitenb4,text=tab[0][1], width="6", height="3")
    labelnl4.pack()

    boitenb5=Frame(fen,bd=10,bg="#41B87F",relief=RAISED)
    boitenb5.place(x=325,y=200)
    labelnb5=Label(boitenb5,text=tab[1][1], width="6", height="3")
    labelnb5.grid()

    boitenb7=Frame(fen,bd=10,bg="#41B87F",relief=RAISED)
    boitenb7.place(x=200,y=300)
    labelnl7=Label(boitenb7,text=tab[0][2], width="6", height="3")
    labelnl7.pack()

    boitenb8=Frame(fen,bd=10,bg="#41B87F",relief=RAISED)
    boitenb8.place(x=325,y=300)
    labelnb8=Label(boitenb8,text=tab[1][2], width="6", height="3")
    labelnb8.grid()
    if tab == win:
        print("bravo")
def vortex_3():
    first_tab=tab[1][0]
    tab[1][0]=tab[2][0]
    tab[2][0]=tab[2][1]
    tab[2][1]=tab[1][1]
    tab[1][1]=first_tab

    boitenb2=Frame(fen,bd=10,bg="#41B87F",relief=RAISED)
    boitenb2.place(x=325,y=100)
    labelnb2=Label(boitenb2,text=tab[1][0], width="6", height="3")
    labelnb2.grid()

    boitenb3=Frame(fen,bd=10,bg="#41B87F",relief=RAISED)
    boitenb3.place(x=450,y=100)
    labelnb3=Label(boitenb3,text=tab[2][0], width="6", height="3")
    labelnb3.grid()

    boitenb6=Frame(fen,bd=10,bg="#41B87F",relief=RAISED)
    boitenb6.place(x=450,y=200)
    labelnb6=Label(boitenb6,text=tab[2][1], width="6", height="3")
    labelnb6.grid()

    boitenb5=Frame(fen,bd=10,bg="#41B87F",relief=RAISED)
    boitenb5.place(x=325,y=200)
    labelnb5=Label(boitenb5,text=tab[1][1], width="6", height="3")
    labelnb5.grid()
    if tab == win:
        print("bravo")
def vortex_4():
    first_tab=tab[1][1]
    tab[1][1]=tab[2][1]
    tab[2][1]=tab[2][2]
    tab[2][2]=tab[1][2]
    tab[1][2]=first_tab

    boitenb9=Frame(fen,bd=10,bg="#41B87F",relief=RAISED)
    boitenb9.place(x=450,y=300)
    labelnb9=Label(boitenb9,text=tab[2][2], width="6", height="3")
    labelnb9.grid()

    boitenb5=Frame(fen,bd=10,bg="#41B87F",relief=RAISED)
    boitenb5.place(x=325,y=200)
    labelnb5=Label(boitenb5,text=tab[1][1], width="6", height="3")
    labelnb5.grid()

    boitenb6=Frame(fen,bd=10,bg="#41B87F",relief=RAISED)
    boitenb6.place(x=450,y=200)
    labelnb6=Label(boitenb6,text=tab[2][1], width="6", height="3")
    labelnb6.grid()

    boitenb8=Frame(fen,bd=10,bg="#41B87F",relief=RAISED)
    boitenb8.place(x=325,y=300)
    labelnb8=Label(boitenb8,text=tab[1][2], width="6", height="3")
    labelnb8.grid()

    if tab == win:
        print("bravo")

fleche1=PhotoImage(file="fleche1.png")
framebtn1=Frame(fen,bd=5,bg="#41B87F",relief=RAISED)
framebtn1.place(x=275,y=170)
btn1=Button(framebtn1,image=fleche1,command = vortex_1)
btn1.grid()

fleche2=PhotoImage(file="fleche2.png")
framebtn2=Frame(fen,bd=5,bg="#41B87F",relief=RAISED)
framebtn2.place(x=275,y=270)
btn2=Button(framebtn2,image=fleche2,command = vortex_2)
btn2.grid()

fleche3=PhotoImage(file="fleche3.png")
framebtn3=Frame(fen,bd=5,bg="#41B87F",relief=RAISED)
framebtn3.place(x=400,y=170)
btn3=Button(framebtn3,image=fleche3,command = vortex_3)
btn3.grid()

fleche4=PhotoImage(file="fleche4.png")
framebtn4=Frame(fen,bd=5,bg="#41B87F",relief=RAISED)
framebtn4.place(x=400,y=270)
btn4=Button(framebtn4,image=fleche4,command = vortex_4)
btn4.grid()

framebtn0=Frame(fen,bd=5,bg="#41B87F",relief=RAISED)
framebtn0.place(x=330,y=400)
btn0=Button(framebtn0, text= "Quitter", command = fen.destroy)
btn0.grid()

boitetitre=Frame(fen, bd=5,bg="#41B77F",relief=RAISED)
label=Label(boitetitre,text="Vortex",font=("Courrier",30),bg="#41B77F",fg="white")
label.pack()
boitetitre.place(x=292,y=0)

vortex_1()
vortex_2()
vortex_3()
vortex_4()

fen.mainloop()

