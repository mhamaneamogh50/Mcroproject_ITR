
from tkinter import*
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from Dashboard import *

def loginpage():
    uname=e1.get()
    password=e2.get()

    if(uname=="" and password==""):
        messagebox.showinfo("","Blank not allowed")
    
    elif(uname=="Admin" and password=="Admin@123"):
        messagebox.showinfo("","Login Successful")
        mainwin()

    else:
        messagebox.showinfo("","Invalid login credentials")
    
    

    

root=Tk()
root.title("Login")
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()

#setting tkinter window size
root.geometry("%dx%d" %(width,height))
root.configure(background="Light blue")

load=Image.open('wl.jpg')
img=ImageTk.PhotoImage(load)
panel = Label (root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
# img.place (x = 0, y = 0)




Label(root,text="--Hospital Name--",font=("Arial", 25),bg="lightblue").place(x=550,y=50)
Label(root,text="Username",font=("Arial", 15),bg="lightblue").place(x=500,y=250)
Label(root,text="Password",font=("Arial", 15),bg="lightblue").place(x=500,y=300)

e1=Entry(root,font=("Arial", 15))
e1.place(x=650,y=250)

e2=Entry(root,font=("Arial", 15))
e2.place(x=650,y=300)
e2.config(show="*")

Button(root,text="Login",command=loginpage,height=2,width=10,font=("Arial", 15),bg="lightblue").place(x=650,y=350)
loginpage()
root.mainloop()
