from tkinter import*
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from loginpage import *
import sqlite3


def mainwin():
#Declare all variables as global
    global dashimage
    global load
    global render
    global img2
    global dashlabel
    global load1
    global render1
    global imgv
    global img1
    global b1
    global img3
    global b2
    global img4
    global b3
    global img5
    global b4
    global img6
    global b5
    global img7
    global b6
    global img8
    global b7
    global root
    root= Tk()
    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()
    root.geometry("%dx%d" %(width,height))
    root.title('Hospital Management ')
    # Setting icon of root window
    img=PhotoImage(file='icon2.png')
    root.iconphoto(False, img)
    
    dashimage=ImageTk.PhotoImage(Image.open("bg2.png"))

    dashlabel=Label(root,image=dashimage)

    dashlabel.place(x=0,y=0)
     
    #Dashboard Label
    load=Image.open('final 4.png')
    render=ImageTk.PhotoImage(load)
    img2= Label (root, image = render,bd=1,bg='black')
    img2.place (x = 50, y = 0)
    #new Label
    load1=Image.open('final3.png')
    render1=ImageTk.PhotoImage(load1)
    imgv= Label (root, image = render1)
    imgv.place (x = 415, y = 130)
    #Button 1
    img1= PhotoImage(file ='button8.png')
    b1 =Button (root, image=img1, bd=0,command=appoin)
    b1.place (x = 50, y = 140)
    #Button 2
    img3= PhotoImage(file ='button9.png')
    b2 =Button (root, image=img3, bd=0,command=serv)
    b2.place (x =50, y = 340)
    #Button 3
    img4= PhotoImage(file ='button10.png')
    b3 =Button (root, image=img4, bd=0,command=Home)
    b3.place (x =50, y = 240)
    #Button 4
    img5= PhotoImage(file ='button7.png')
    b4 =tk.Button(root, image=img5, bd=0,command=contact)
    b4.place (x =50, y = 540)
    #Button 5
    img6= PhotoImage(file ='button6.png')
    b5 =Button (root, image=img6, bd=0,command=Log)
    b5.place (x =50, y = 740)

    #Button 6
    img7= PhotoImage(file ='button11.png')
    b6 =Button (root, image=img7, bd=0,command=about)
    b6.place (x =50, y = 640)

    #Button 7
    img8= PhotoImage(file ='button12.png')
    b7 =Button (root, image=img8, bd=0,command=bill)
    b7.place (x =50, y = 440)






 
def Log():
    root.destroy()
    
def about():

    global loada1
    global imga1
    global panela1
    global root1
    global bcb1
    global aboutload
    global renderabt
    global imgabt2
    
    
    top= Toplevel()

    width= top.winfo_screenwidth()

    height= top.winfo_screenheight()

    top.geometry("%dx%d" %(width,height))

    top.title('Hospital Management ')
    # Setting icon of root window
    img=PhotoImage(file='icon2.png')
    top.iconphoto(False, img)

    
    
    print("Program Executed without any bug!!!!!!!!!!!!")
  

    #Background image
    loada1=Image.open('bg2.png')#about.jpg
    imga1=ImageTk.PhotoImage(loada1)
    panela1 = Label (top, image = imga1)
    panela1.place(x=0,y=0)
    
    
    aboutload=Image.open('about.jpg')
    renderabt=ImageTk.PhotoImage(aboutload)
    imgabt2= Label (top, image = renderabt)
    imgabt2.place (x = 70, y = 150)

    #bcb1=Button(top,text="Back",command=maniwin,bd=1)
    #bcb1.place(x=10,y=10)

    
    

def serv():

    global loada2
    global imga2
    global panela2
    global top2
    global imgs1
    global bs1
    global imgs2
    global bs2
    global imgs3
    global bs3
    global imgs4
    global bs4
    global imgs5
    global bs5
    global loads1
    global imgs1
    global renders1
    global loadse2
    global renderse2
    global imgse2
    
    top2= Toplevel()

    width= top2.winfo_screenwidth()

    height= top2.winfo_screenheight()

    top2.geometry("%dx%d" %(width,height))

    top2.title('Hospital Management ')
    # Setting icon of root window
    img=PhotoImage(file='icon2.png')
    top2.iconphoto(False, img)
    print("Program Executed without any bug!!!!!!!!!!!!")

    #Background image
    loada2=Image.open('bg2.png')
    imga2=ImageTk.PhotoImage(loada2)
    panela2 = Label (top2, image = imga2)
    panela2.pack(fill=BOTH,expand=True)


    #Serv Label
    loadse2=Image.open('final 4.png')
    renderse2=ImageTk.PhotoImage(loadse2)
    imgse2= Label (top2, image = renderse2,bd=1,bg='black')
    imgse2.place (x = 50, y = 0)



    #Serv bg
     
    loads1=Image.open('SERVICESIMG.png')
    renders1=ImageTk.PhotoImage(loads1)
    imgs1= Label (top2, image = renders1)
    imgs1.place (x = 500, y = 300)

    imgs1= PhotoImage(file ='button10.png')
    bs1 =Button (top2, image=imgs1, bd=0,command=Home)
    bs1.place (x =50, y = 150)
    #Button 4
    imgs2= PhotoImage(file ='button7.png')
    bs2 =tk.Button(top2, image=imgs2, bd=0,command=contact)
    bs2.place (x =50, y = 250)
    #Button 5
    imgs3= PhotoImage(file ='button6.png')
    bs3 =Button (top2, image=imgs3, bd=0,command=Log)
    bs3.place (x =50, y = 350)

    #Button 6
    imgs4= PhotoImage(file ='button11.png')
    bs4 =Button (top2, image=imgs4, bd=0,command=about)
    bs4.place (x =50, y = 450)

    #Button 7
    imgs5= PhotoImage(file ='button12.png')
    bs5 =Button (top2, image=imgs5, bd=0)
    bs5.place (x =50, y = 550)



def contact():
    
    

    global loada4
    global imga4
    global panela4
    global top4
    
    
    top4= Toplevel()

    width= top4.winfo_screenwidth()

    height= top4.winfo_screenheight()

    top4.geometry("%dx%d" %(width,height))

    top4.title('Hospital Management ')
    # Setting icon of root window
    img=PhotoImage(file='icon2.png')
    top4.iconphoto(False, img)
    

    #Background image
    loada4=Image.open('CONTACT.png')
    imga4=ImageTk.PhotoImage(loada4)
    panela4 = Label (top4, image = imga4)
    panela4.pack(fill=BOTH,expand=True)





def bill():

    global c2
    top7 = Toplevel()                 #TopLevel

    width= top7.winfo_screenwidth()

    height= top7.winfo_screenheight()

    top7.geometry("%dx%d" %(width,height))
    
    conn2 = sqlite3.connect('registration.db')
    c2 = conn2.cursor()

    apoin_bg=ImageTk.PhotoImage(Image.open("bg2.png"))

    apoin_lbl=Label(top7,image=apoin_bg)

    apoin_lbl.place(x=0,y=0)

    loadat1=Image.open('bill.png')
    renderat1=ImageTk.PhotoImage(loadat1)
    imgvat= Label (top7, image = renderat1,bd=0)
    imgvat.place (x = 415, y = 130)

    #Dashboard Label
    loadap=Image.open('final 4.png')
    renderap=ImageTk.PhotoImage(loadap)
    imgap2= Label (top7, image = renderap)
    imgap2.place (x = 50, y = 0)

    #Button 1
    imgap1= PhotoImage(file ='button8.png')
    bap1 =Button (top7, image=imgap1, bd=0)
    bap1.place (x = 50, y = 130)
    #Button 2
    imgap3= PhotoImage(file ='button9.png')
    bap2 =Button (top7, image=imgap3, bd=0)
    bap2.place (x =50, y = 220)
    #Button 3
    imgap4= PhotoImage(file ='button10.png')
    bap3 =Button (top7, image=imgap4, bd=0)
    bap3.place (x =50, y = 320)
    #Button 4
    imgap5= PhotoImage(file ='button7.png')
    bap4 =tk.Button(top7, image=imgap5, bd=0)
    bap4.place (x =50, y = 420)
    #Button 5
    imgap6= PhotoImage(file ='button6.png')
    bap5 =Button (top7, image=imgap6, bd=0)
    bap5.place (x =50, y = 520)

    id_bill = Label(top7, text="Bill Id")
    id_bill.place(x=500,y=350)

    id_ent = Entry(top7)
    id_ent.place(x=600,y=350)

    type_bill = Label(top7, text="Bill Type")
    type_bill.place(x=800,y=350)

    type_ent = Entry(top7)
    type_ent.place(x=900,y=350)

    name_bill = Label(top7, text="Patient Name")
    name_bill.place(x=500,y=450)

    name_ent = Entry(top7)
    name_ent.place(x=600,y=450)

    serv_bill = Label(top7, text="Services")
    serv_bill.place(x=800,y=450)

    serv_ent = Entry(top7)
    serv_ent.place(x=900,y=450)

    price_bill = Label(top7, text="Price")
    price_bill.place(x=500,y=550)

    price_ent = Entry(top7)
    price_ent.place(x=600,y=550)
    
    amt_bill = Label(top7, text="Amount")
    amt_bill.place(x=800,y=550)

    amt_ent = Entry(top7)
    amt_ent.place(x=900,y=550)

    date_bill = Label(top7, text="Date")
    date_bill.place(x=500,y=650)

    date_ent = Entry(top7)
    date_ent.place(x=600,y=650)

    def add_ap():
        global val1
        global val2
        global val3
        global val4
        global val5
        global val6
        global val7

        val1 = id_ent.get()
        val2 = type_ent.get()
        val3 = name_ent.get()
        val4 = serv_ent.get()
        val5 = price_ent.get()
        val6 = amt_ent.get()
        val7 = date_ent.get()
        

        if(val1== '' or val2 =='' or val3=='' or val4=='' or val5=='' or val6=='' or val7==''):
                tkinter.messagebox.showinfo("Warning", "Please fill up all boxes")

        else:

                sql = "INSERT INTO 'billdb' (bill_id, bill_type, pat_name, services, price, amount, date) VALUES(?,?,?,?,?,?,?)"
                c2.execute(sql, (val1, val2, val3, val4, val5, val6, val7))
                conn2.commit()
                tk.messagebox.showinfo("Registration Successful", "Registration Successful")


    add = Button(top7,text="Add", command=add_ap)
    add.place(x=800,y=600)

    butt = Button(top7, text="Table", command=Table_screen)
    butt.place(x=950,y=600)

    print_b = Button(top7, text="Print", command=print_bill)
    print_b.place(x=1050,y=600)

    top7.mainloop()

def Table_screen():
    
    global show
    global trv2
    

    root1 = Toplevel()
    root1.geometry("1000x500")
    root1.title("Database table")


    show = c2.execute('SELECT * FROM billdb')
    trv2 = ttk.Treeview(root1, selectmode='browse')
    trv2.grid(row=1,column=1,padx=20,pady=20)
    trv2["columns"] = ("1","2","3","4","5","6","7")
    trv2['show'] = 'headings'
    trv2.column("1",width=50,anchor='c')
    trv2.column("2",width=100,anchor='c')
    trv2.column("3",width=100,anchor='c')
    trv2.column("4",width=60,anchor='c')
    trv2.column("5",width=60,anchor='c')
    trv2.column("6",width=80,anchor='c')
    trv2.column("7",width=80,anchor='c')

    trv2.heading("1",text="Bill Id")
    trv2.heading("2",text="Bill Type")
    trv2.heading("3",text="Patient Name")
    trv2.heading("4",text="Services")
    trv2.heading("5",text="Price")
    trv2.heading("6",text="Amount")
    trv2.heading("7",text="Date")

    

    for data2 in show:
        trv2.insert("",'end',iid=data2[0],values=(data2[0],data2[1],data2[2],data2[3],data2[4],data2[5],data2[6]))

def print_bill():
    global val1
    top8=Toplevel()
    width = top8.winfo_screenwidth()

    height= top8.winfo_screenheight()

    top8.geometry("%dx%d" %(width,height))

    bill_bg=ImageTk.PhotoImage(Image.open("FINAL_BILL1.png"))
    bill_lbl= Label(top8,image=bill_bg)
    bill_lbl.place(x=0,y=0)

    b_id = Label(top8, text=val1,bg="white")
    b_id.place(x=210,y=135)

    b_type = Label(top8, text=val2, bg="white")
    b_type.place(x=435 ,y=135)
    
    p_id = Label(top8, text=val1, bg="white")
    p_id.place(x=219,y=190)

    p_name = Label(top8, text=val3, bg="white")
    p_name.place(x=242,y=230)

    b_serv = Label(top8, text=val4, bg="white")
    b_serv.place(x=245,y=400)

    b_price = Label(top8, text=val6, bg="white")
    b_price.place(x=545,y=500)


    b_date = Label(top8, text=val7, bg="white")
    b_date.place(x=600,y=135)










def appoin():
    global top3
    global apoin_bg
    global apoin_lbl
    global imgap1
    global bap1
    global imgap3
    global bap2
    global imgap4
    global bap3
    global imgap5
    global bap4
    global imgap6
    global bap5
    global imgap7
    global bap6
    global loadap
    global renderap
    global imgap2
    global loadat1
    global renderat1
    global imgvat
    global Apid
    global Apren
    global ap_id
    global Apn
    global Apren1
    global ap_name
    global Apd
    global Apren2
    global ap_date
    global ap_time
    global Apt
    global Apren3
    global Apad
    global Apren4
    global add
    global loadat2
    global renderat2
    global imgvat1
    
    top3=Toplevel()
    width= top3.winfo_screenwidth()

    height= top3.winfo_screenheight()

    top3.geometry("%dx%d" %(width,height))
    
    top3.title("Appointment")

    #Setting icon of root window
    img=PhotoImage(file='icon2.png')
    top3.iconphoto(False, img)



    
    
    apoin_bg=ImageTk.PhotoImage(Image.open("bg2.png"))

    apoin_lbl=Label(top3,image=apoin_bg)

    apoin_lbl.place(x=0,y=0)



    #new Label
    loadat1=Image.open('ABG.png')
    renderat1=ImageTk.PhotoImage(loadat1)
    imgvat= Label (top3, image = renderat1,bd=0)
    imgvat.place (x = 415, y = 130)


##    loadat2=Image.open('apbox.png')
##    renderat2=ImageTk.PhotoImage(loadat2)
##    imgvat1= Label (top3, image = renderat2,bd=0)
##    imgvat1.place (x = 415, y = 130)


    conn1 = sqlite3.connect('registration.db')
    c1 = conn1.cursor()

    #Dashboard Label
    loadap=Image.open('final 4.png')
    renderap=ImageTk.PhotoImage(loadap)
    imgap2= Label (top3, image = renderap)
    imgap2.place (x = 50, y = 5)

    #Button 1
    imgap1= PhotoImage(file ='button8.png')
    bap1 =Button (top3, image=imgap1, bd=0)
    bap1.place (x = 50, y = 150)
    #Button 2
    imgap3= PhotoImage(file ='button9.png')
    bap2 =Button (top3, image=imgap3, bd=0,command=serv)
    bap2.place (x =50, y = 300)
    #Button 3
    imgap4= PhotoImage(file ='button10.png')
    bap3 =Button (top3, image=imgap4, bd=0,command=Home)
    bap3.place (x =50, y = 450)
    #Button 4
    imgap5= PhotoImage(file ='button7.png')
    bap4 =tk.Button(top3, image=imgap5, bd=0,command=contact)
    bap4.place (x =50, y = 600)
    #Button 5
    imgap6= PhotoImage(file ='button6.png')
    bap5 =Button (top3, image=imgap6, bd=0,command=Log)
    bap5.place (x =50, y = 750)

    #Button 6
    # imgap7= PhotoImage(file ='button11.png')
    # bap6 =Button (top3, image=imgap7, bd=0)
    # bap6.place (x =50, y = 620)
    Apid = Image.open('Apid.png')
    Apren = ImageTk.PhotoImage(Apid)
    ap_id = Label(top3,image=Apren,bd=0)
    ap_id.place(x=500,y=300)

    id_entry = Entry(top3)
    id_entry.place(x=750,y=300)
    
    Apn = Image.open('Apn.png')
    Apren1 = ImageTk.PhotoImage(Apn)
    ap_name = Label(top3,image=Apren1,bd=0)
    ap_name.place(x=500,y=400)

    name_entry = Entry(top3)
    name_entry.place(x=750,y=400)
    
    Apd = Image.open('Apd.png')
    Apren2 = ImageTk.PhotoImage(Apd)
    ap_date = Label(top3,image=Apren2,bd=0)
    ap_date.place(x=500,y=500)

    date_entry = Entry(top3)
    date_entry.place(x=750,y=500)



    Apt = Image.open('Apt.png')
    Apren3 = ImageTk.PhotoImage(Apt)
    ap_time = Label(top3,image=Apren3,bd=0)
    ap_time.place(x=500,y=600)

    time_entry = Entry(top3)
    time_entry.place(x=750,y=600)

    
    def add_ap():
        val1 = id_entry.get()
        val2 = name_entry.get()
        val3 = date_entry.get()
        val4 = time_entry.get()
        

        if(val1== '' or val2 =='' or val3=='' or val4==''):
                tk.messagebox.showinfo("Warning", "Please fill up all boxes")

        else:

                sql = "INSERT INTO 'appointment' (ap_id, ap_name, ap_date , ap_time) VALUES(?,?,?,?)"
                c1.execute(sql, (val1, val2, val3, val4))
                conn1.commit()
                tk.messagebox.showinfo("Registration Successful","done")

    Apad = Image.open('Apad.png')
    Apren4 = ImageTk.PhotoImage(Apad)
    add = Button(top3,image=Apren4, command=add_ap,bd=0,bg='black')
    add.place(x=800,y=700)
 

#patientregistration
def Home():

    global top5
    global panel
    global loadp
    global conn
    global c
    global imgp
    global imgp1
    global imgp3
    global imgp4
    global imgp5
    global imgp6
    global imgpv
    global b1
    global b2
    global b3
    global b4
    global b5
    global loadp1
    global renderp1
    global renderp2
    global renderp3
    global renderp4
    global renderp5
    global renderp6
    global renderp7
    global renderp8
    global renderp9
    global renderp10
    global submit
    global butt
    global table
    global loadpt1
    global renderpt1
    global imgvpt
    
    top5= tk.Toplevel()
    top5.geometry("1500x900")
    top5.title("Patient Registration Form")


    load=Image.open('bg2.png')
    imgp=ImageTk.PhotoImage(load)
    panel = Label (top5, image = imgp)
    panel.pack(side = "bottom", fill = "both", expand = "yes")



    #new Label
    loadpt1=Image.open('PBG.png')
    renderpt1=ImageTk.PhotoImage(loadpt1)
    imgvpt= Label (top5, image = renderpt1,bd=0)
    imgvpt.place (x = 380, y = 130)

    


    conn = sqlite3.connect('registration.db')
    c = conn.cursor()

    #Button 1
    imgp1= PhotoImage(file ='button8.png')
    b1 =Button (top5, image=imgp1, bd=0,command=appoin)
    b1.place (x = 50, y = 150)
    #Button 2
    imgp3= PhotoImage(file ='button9.png')
    b2 =Button (top5, image=imgp3, bd=0,command=serv)
    b2.place (x =50, y = 300)
    #Button 3
    imgp4= PhotoImage(file ='button10.png')#Add grey button 
    b3 =Button (top5, image=imgp4, bd=0)
    b3.place (x =50, y = 450)
    #Button 4
    imgp5= PhotoImage(file ='button7.png')
    b4 =tk.Button(top5, image=imgp5, bd=0,command=contact)
    b4.place (x =50, y = 600)
    #Button 5
    imgp6= PhotoImage(file ='button6.png')
    b5 =Button (top5, image=imgp6, bd=0,command=Log)
    b5.place (x =50, y = 750)

    loadp1=Image.open('final 4.png')
    renderp1=ImageTk.PhotoImage(loadp1)
    imgv= Label (top5, image = renderp1)
    imgv.place (x = 50, y = 0)



    regno = Image.open('Reg_no.png')
    renderp2 = ImageTk.PhotoImage(regno)
    regis_no = Label(top5,image=renderp2)
    regis_no.place(x=400,y=245)

    ent_regno = Entry(top5)
    ent_regno.place(x=550,y=250)

    name_img = Image.open('pat_name.png')
    renderp4 = ImageTk.PhotoImage(name_img)
    name = Label(top5,image=renderp4)
    name.place(x=830,y=245)

    ent_name = Entry(top5, width=25)
    ent_name.place(x=1000,y=250)

    email_img = Image.open('email.png')
    renderp5 = ImageTk.PhotoImage(email_img)
    email = Label(top5,image=renderp5)
    email.place(x=400,y=345)

    ent_email = Entry(top5, width=25)
    ent_email.place(x=550,y=350)

    gend_img = Image.open('gender.png')
    renderp6 = ImageTk.PhotoImage(gend_img)
    gender = Label(top5,image=renderp6)
    gender.place(x=830,y=345)

    gend_var = IntVar()
    Radiobutton(top5, text="Male",padx = 5, variable=gend_var,bg="lightblue", value=1).place(x=1000,y=350)
    Radiobutton(top5, text="Female",padx = 20, variable=gend_var,bg="lightblue", value=2).place(x=1100,y=350)

    age_img = Image.open('age.png')
    renderp7 = ImageTk.PhotoImage(age_img)
    age = Label(top5, image=renderp7)
    age.place(x=400,y=445)


    ent_age = Entry(top5)
    ent_age.place(x=550,y=450)

    add_img = Image.open('address.png')
    renderp8 = ImageTk.PhotoImage(add_img)
    address = Label(top5, image=renderp8)
    address.place(x=830,y=445)

    ent_add = Entry(top5, width=25)
    ent_add.place(x=1000,y=450)

    ph_img = Image.open('phone.png')
    renderp9 = ImageTk.PhotoImage(ph_img)
    phone = Label(top5, image=renderp9)
    phone.place(x=400,y=545)

    ent_phone = Entry(top5)
    ent_phone.place(x=550,y=550)

       
    def add_info():
        val1 = ent_regno.get()
        val2 = ent_name.get()
        val3 = ent_email.get()
        val4 = ent_age.get()
        val5 = ent_add.get()
        val6 = ent_phone.get()

        if(val1== '' or val2 =='' or val3=='' or val4=='' or val5 =='' or val6 ==''):
                tk.messagebox.showinfo("Warning", "Please fill up all boxes")

        else:


                sql = "INSERT INTO 'patient' (regno, name, email , age , address, phone) VALUES(?,?,?,?,?,?)"
                c.execute(sql, (val1, val2, val3, val4, val5, val6))
                conn.commit()
                tk.messagebox.showinfo("Registration Successful","Patient data added succesfully.")


    sub = Image.open('submit.png')
    renderp3 = ImageTk.PhotoImage(sub)
    submit = Button(top5, image=renderp3, command=add_info,bd=0).place(x=700,y=750)

    
    
    def Table_screen():

        global show
        global trv
        global top6
        global data

        top6 = tk.Tk()
        top6.geometry("1000x500")
        top6.title("Database table")

        

        show = c.execute('SELECT * FROM patient')
        trv = ttk.Treeview(top6, selectmode='browse')
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
        

        

    table = Image.open('table.png')
    renderp10 = ImageTk.PhotoImage(table)
    butt = Button(top5,image=renderp10,command=Table_screen,bd=0)
    butt.place(x=900,y=750)

    
    



mainwin()

#ExitLoop


root.mainloop()
