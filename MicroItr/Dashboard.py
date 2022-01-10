from tkinter import*
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from loginpage import *


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

    dashimage=ImageTk.PhotoImage(Image.open("bg2.png"))

    dashlabel=Label(root,image=dashimage)

    dashlabel.place(x=0,y=0)
     
    #Dashboard Label
    load=Image.open('1263.jpg')
    render=ImageTk.PhotoImage(load)
    img2= Label (root, image = render)
    img2.place (x = 50, y = 0)
    #new Label
    load1=Image.open('Values1.jpg')
    render1=ImageTk.PhotoImage(load1)
    imgv= Label (root, image = render1)
    imgv.place (x = 400, y = 130)
    #Button 1
    img1= PhotoImage(file ='button8.png')
    b1 =Button (root, image=img1, bd=0,command=appoin)
    b1.place (x = 50, y = 120)
    #Button 2
    img3= PhotoImage(file ='button9.png')
    b2 =Button (root, image=img3, bd=0,command=serv)
    b2.place (x =50, y = 220)
    #Button 3
    img4= PhotoImage(file ='button10.png')
    b3 =Button (root, image=img4, bd=0)
    b3.place (x =50, y = 320)
    #Button 4
    img5= PhotoImage(file ='button7.png')
    b4 =tk.Button(root, image=img5, bd=0,command=contact)
    b4.place (x =50, y = 420)
    #Button 5
    img6= PhotoImage(file ='button6.png')
    b5 =Button (root, image=img6, bd=0)
    b5.place (x =50, y = 520)

    #Button 6
    img7= PhotoImage(file ='button11.png')
    b6 =Button (root, image=img7, bd=0,command=about)
    b6.place (x =50, y = 620)

    #Button 7
    img8= PhotoImage(file ='button12.png')
    b7 =Button (root, image=img8, bd=0)
    b7.place (x =50, y = 720)




 
def about():

    global loada1
    global imga1
    global panela1
    global root1
    
    
    top= Toplevel()

    width= top.winfo_screenwidth()

    height= top.winfo_screenheight()

    top.geometry("%dx%d" %(width,height))

    top.title('Hospital Management ')
    print("fopdpd")

    #Background image
    loada1=Image.open('about.jpg')
    imga1=ImageTk.PhotoImage(loada1)
    panela1 = Label (top, image = imga1)
    panela1.pack(fill=BOTH,expand=True)
    
    

def serv():

    global loada2
    global imga2
    global panela2
    global top2
    
    
    top2= Toplevel()

    width= top2.winfo_screenwidth()

    height= top2.winfo_screenheight()

    top2.geometry("%dx%d" %(width,height))

    top2.title('Hospital Management ')
    print("fopdpd")

    #Background image
    loada2=Image.open('serv.jpeg')
    imga2=ImageTk.PhotoImage(loada2)
    panela2 = Label (top2, image = imga2)
    panela2.pack(fill=BOTH,expand=True)



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
    

    #Background image
    loada4=Image.open('CONTACT.png')
    imga4=ImageTk.PhotoImage(loada4)
    panela4 = Label (top4, image = imga4)
    panela4.pack(fill=BOTH,expand=True)





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
    
    
    top3=Toplevel()
    width= top3.winfo_screenwidth()

    height= top3.winfo_screenheight()

    top3.geometry("%dx%d" %(width,height))
    
    top3.title("appoin")
    
    apoin_bg=ImageTk.PhotoImage(Image.open("bg2.png"))

    apoin_lbl=Label(top3,image=apoin_bg)

    apoin_lbl.place(x=0,y=0)

    #Dashboard Label
    loadap=Image.open('1263.jpg')
    renderap=ImageTk.PhotoImage(loadap)
    imgap2= Label (top3, image = renderap)
    imgap2.place (x = 50, y = 0)

    #Button 1
    imgap1= PhotoImage(file ='button8.png')
    bap1 =Button (top3, image=imgap1, bd=0)
    bap1.place (x = 50, y = 120)
    #Button 2
    imgap3= PhotoImage(file ='button9.png')
    bap2 =Button (top3, image=imgap3, bd=0,command=serv)
    bap2.place (x =50, y = 220)
    #Button 3
    imgap4= PhotoImage(file ='button10.png')
    bap3 =Button (top3, image=imgap4, bd=0)
    bap3.place (x =50, y = 320)
    #Button 4
    imgap5= PhotoImage(file ='button7.png')
    bap4 =tk.Button(top3, image=imgap5, bd=0)
    bap4.place (x =50, y = 420)
    #Button 5
    imgap6= PhotoImage(file ='button6.png')
    bap5 =Button (top3, image=imgap6, bd=0)
    bap5.place (x =50, y = 520)

    #Button 6
    imgap7= PhotoImage(file ='button11.png')
    bap6 =Button (top3, image=imgap7, bd=0,command=about)
    bap6.place (x =50, y = 620)

    



#ExitLoop
mainwin()

root.mainloop()
