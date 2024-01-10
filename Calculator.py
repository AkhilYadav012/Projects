from tkinter import *
def do():
    a=int(t1.get())
    b=int(t2.get())
    c=a+b
    t3.delete(0,"end")
    t3.insert(0,c)
def sub():
    a=int(t1.get())
    b=int(t2.get())
    c=a-b
    t3.delete(0,"end")
    t3.insert(0,c)
def div():
    a=int(t1.get())
    b=int(t2.get())
    c=a/b
    t3.delete(0,"end")
    t3.insert(0,c)
def mul():
    a=int(t1.get())
    b=int(t2.get())
    c=a*b
    t3.delete(0,"end")
    t3.insert(0,c)


myframe=Tk()
myframe.geometry("300x300")
myframe.title("Calculator")
l1=Label(myframe,text="Enter First no.",bg="#87CEEB",width=30)
l2=Label(myframe,text="Enter Second no.",bg="#87CEEB",width=30)
l3=Label(myframe,text="Result",bg="#87CEEB",width=30)
t1=Entry(myframe,width=35)
t2=Entry(myframe,width=35)
t3=Entry(myframe,width=35)
b1=Button(myframe,text="+",command=do)
b2=Button(myframe,text="-",command=sub)
b3=Button(myframe,text="÷",command=div)
b4=Button(myframe,text="x",command=mul)
l1.place(x=20,y=30)
t1.place(x=20,y=60)
l2.place(x=20,y=90)
t2.place(x=20,y=120)
l3.place(x=20,y=150)
t3.place(x=20,y=180)
b1.place(x=20,y=210,width=30)
b2.place(x=50,y=210,width=30)
b3.place(x=80,y=210,width=30)
b4.place(x=110,y=210,width=30)
myframe.mainloop()