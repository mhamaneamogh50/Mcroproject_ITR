
from tkinter import *
import tkinter as tk
import sqlite3
import tkinter.messagebox
from PIL import Image,ImageTk
from tkinter import ttk


def Home():

    global root
    global panel
    global load
    global conn
    global c
    global img
    global img1
    global img3
    global img4
    global img5
    global img6
    global imgv
    global b1
    global b2
    global b3
    global b4
    global b5
    global load1
    global render1
    global render2
    global render3
    global render4
    global render5
    global render6
    global render7
    global render8
    global render9
    global submit

    root = Tk()
    


    root.geometry("1500x900")

    root.title("Registration Form")

    load=Image.open('bg2.png')
    img=ImageTk.PhotoImage(load)
    panel = Label (root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")


    conn = sqlite3.connect('registration.db')
    c = conn.cursor()

    #Button 1
    img1= PhotoImage(file ='button8.png')
    b1 =Button (root, image=img1, bd=0)
    b1.place (x = 50, y = 200)
    #Button 2
    img3= PhotoImage(file ='button9.png')
    b2 =Button (root, image=img3, bd=0)
    b2.place (x =50, y = 300)
    #Button 3
    img4= PhotoImage(file ='button10.png')
    b3 =Button (root, image=img4, bd=0)
    b3.place (x =50, y = 400)
    #Button 4
    img5= PhotoImage(file ='button7.png')
    b4 =tk.Button(root, image=img5, bd=0)
    b4.place (x =50, y = 500)
    #Button 5
    img6= PhotoImage(file ='button6.png')
    b5 =Button (root, image=img6, bd=0)
    b5.place (x =50, y = 600)

    load1=Image.open('1263.jpg')
    render1=ImageTk.PhotoImage(load1)
    imgv= Label (root, image = render1)
    imgv.place (x = 50, y = 0)



    regno = Image.open('Reg_no.png')
    render2 = ImageTk.PhotoImage(regno)
    regis_no = Label(root,image=render2)
    regis_no.place(x=500,y=245)

    ent_regno = Entry(root)
    ent_regno.place(x=650,y=250)

    name_img = Image.open('pat_name.png')
    render4 = ImageTk.PhotoImage(name_img)
    name = Label(root,image=render4)
    name.place(x=800,y=245)

    ent_name = Entry(root, width=25)
    ent_name.place(x=950,y=250)

    email_img = Image.open('email.png')
    render5 = ImageTk.PhotoImage(email_img)
    email = Label(root,image=render5)
    email.place(x=500,y=345)

    ent_email = Entry(root, width=30)
    ent_email.place(x=630,y=350)

    gend_img = Image.open('gender.png')
    render6 = ImageTk.PhotoImage(gend_img)
    gender = Label(root,image=render6)
    gender.place(x=830,y=345)

    gend_var = IntVar()
    Radiobutton(root, text="Male",padx = 5, variable=gend_var,bg="lightblue", value=1).place(x=950,y=350)
    Radiobutton(root, text="Female",padx = 20, variable=gend_var,bg="lightblue", value=2).place(x=1050,y=350)

    age_img = Image.open('age.png')
    render7 = ImageTk.PhotoImage(age_img)
    age = Label(root, image=render7)
    age.place(x=520,y=445)


    ent_age = Entry(root)
    ent_age.place(x=630,y=450)

    add_img = Image.open('address.png')
    render8 = ImageTk.PhotoImage(add_img)
    address = Label(root, image=render8)
    address.place(x=800,y=445)

    ent_add = Entry(root, width=30)
    ent_add.place(x=950,y=450)

    ph_img = Image.open('phone.png')
    render9 = ImageTk.PhotoImage(ph_img)
    phone = Label(root, image=render9)
    phone.place(x=500,y=545)

    ent_phone = Entry(root)
    ent_phone.place(x=650,y=550)

    table = Image.open('table.png')
    render10 = ImageTk.PhotoImage(table)
    butt = Button(root,image=render10, command=Table_screen)
    butt.place(x=900,y=600)



    def add_info():
        val1 = ent_regno.get()
        val2 = ent_name.get()
        val3 = ent_email.get()
        val4 = ent_age.get()
        val5 = ent_add.get()
        val6 = ent_phone.get()

        if(val1== '' or val2 =='' or val3=='' or val4=='' or val5 =='' or val6 ==''):
                tkinter.messagebox.showinfo("Warning", "Please fill up all boxes")

        else:
            


            sql = "INSERT INTO 'patient' (regno, name, email , age , address, phone) VALUES(?,?,?,?,?,?)"
            c.execute(sql, (val1, val2, val3, val4, val5, val6))
            conn.commit()
            tkinter.messagebox.showinfo("Registration Successful")


    sub = Image.open('submit.png')
    render3 = ImageTk.PhotoImage(sub)
    submit = Button(root, image=render3, command=add_info).place(x=700,y=600)

    root.mainloop()

def Table_screen():
    
    global show
    global trv
    

    root = tk.Tk()
    root.geometry("1000x500")
    root.title("Database table")

    

    show = c.execute('SELECT * FROM patient')
    trv = ttk.Treeview(root, selectmode='browse')
    trv.grid(row=1,column=1,padx=20,pady=20)
    trv["columns"] = ("1","2","3","4","5","6")
    trv['show'] = 'headings'
    trv.column("1",width=30,anchor='c')
    trv.column("2",width=200,anchor='c')
    trv.column("3",width=200,anchor='c')
    trv.column("4",width=30,anchor='c')
    trv.column("5",width=200,anchor='c')
    trv.column("6",width=80,anchor='c')

    trv.heading("1",text="Id")
    trv.heading("2",text="Patient Name")
    trv.heading("3",text="Email")
    trv.heading("4",text="Age")
    trv.heading("5",text="Address")
    trv.heading("6",text="Phone No")

    

    for data in show:
        trv.insert("",'end',iid=data[0],values=(data[0],data[1],data[2],data[3],data[4],data[5]))


Home()
