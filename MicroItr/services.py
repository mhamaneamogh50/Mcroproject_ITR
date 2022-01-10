from tkinter import*
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk

#Gonfig Dash
root= Tk()

width= root.winfo_screenwidth()

height= root.winfo_screenheight()

root.geometry("%dx%d" %(width,height))

root.title('Hospital Management ')



#Background image
load=Image.open('background.jpeg')
img=ImageTk.PhotoImage(load)
panel = Label (root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

#ExitLoop
root.mainloop()
