from Tkinter import *
from PIL import ImageTk,Image
import Tkinter
import Tkinter as tk
import os

i=0
def callback():
    global i,root
    x=os.listdir('albumart/')
    temp='albumart/'+x[i]
    x = Image.open(temp)
    x = x.resize((600, 600))
    img2 = ImageTk.PhotoImage(x)
    panel.configure(image=img2)
    panel.image = img2
    i=i+1
root = tk.Tk()

img = ImageTk.PhotoImage(Image.open('albumart/(ABCD) - Sparkshell.com.jpg'))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
Button=Tkinter.Button(root,command=callback)
Button2=Tkinter.Button(root,command=callback)
Button.pack()
Button2.pack()
root.mainloop()

"""
root =Tk()

x=Image.open('albumart/3 Idiots.jpg')
x=x.resize((600,600))
img =ImageTk.PhotoImage(x)

imglabel=Label(root,image=img).grid(row=1,column=1)

root.mainloop()
"""