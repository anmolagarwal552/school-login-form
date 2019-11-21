from tkinter import *
root = Tk()
root.geometry('301x301')
root.title('JLU ADMISSION FORM')
root.maxsize(300,300)
root.minsize(300,300)
def pri():
    with open('record.txt', "a") as f:
        f.write(f'NAME IS {name01.get()}\n AGE IS {age01.get()}\n EMAIL IS {email01.get()}\n NUMBER IS {number01.get()}\n D.O.B IS {dob01.get()} \n \n \n \n \n')
lb = Label(root ,text="J.L.U STUDENT FORM",fg="black",font=30).pack()

f1 = Frame(root,relief=SUNKEN,bg='black')
f1.pack(fill=BOTH)
name = Label(f1 ,text="NAME :",bg="black",fg="white").grid()
age = Label(f1 ,text="AGE :",bg="black",fg="white").grid()
email = Label(f1 ,text="EMAIL :",bg="black",fg="white").grid()
number = Label(f1 ,text="NUMBER :",bg="black",fg="white").grid()
dob = Label(f1 ,text="D.O.B :",bg="black",fg="white").grid()


name01 = StringVar()
age01 = StringVar()
email01 = StringVar()
number01 = StringVar()
dob01 = StringVar()

name1  =  Entry(f1,textvariable = name01).grid(row=0,column=1)
age1   =  Entry(f1,textvariable = age01).grid(row=1,column=1)
email1 =  Entry(f1,textvariable = email01).grid(row=2,column=1)
number1=  Entry(f1,textvariable = number01).grid(row=3,column=1)
dob1   =  Entry(f1,textvariable = dob01).grid(row=4,column=1)

b1 =Button(f1,text="SUBMIT",bg="red",fg="white",padx=6,command=pri).grid()
b2 = Button(f1,text="EXIT",padx=10)
b2.grid(column=2)
b2.bind('<Double-1>',quit)
f2 = Frame(root,relief=SUNKEN,bg='black')
f2.pack(fill=BOTH)
b3 =Button(f2,text="OPEN RECORD",bg="red",fg="white",padx=6,command=pri).grid()
lxb = Label(root ,text="~ BY ANMOL",fg="black",font=30).pack(anchor="ne")
root.mainloop()
