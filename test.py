import MySQLdb
import Tkinter
import tkMessageBox
from Tkinter import *
import os
import mp3play
import time
import tkFileDialog
import sys
import getpass

i=0

def printdb():
    db = MySQLdb.connect('localhost', 'root', '', 'test')

    cursor = db.cursor()
    ch=0
    while ch!=1 :
        ch=int(raw_input("Enter 0 for command Input \nEnter 1 for exit\n"))
        if ch == 1:
            break
        try :
            query = raw_input("Enter Query(without Semicolon)\n")
            cursor.execute(query)
            data = cursor.fetchone()
            if data is None:
                print "Nothing to show\n"
            count = 0
            while data is not None :
                print data
                count = count +1
                data = cursor.fetchone()
            print count
        except:
            print "Bad Syntax "
        temp = raw_input("Enter to continue ...\n")
        os.system('cls')
    cursor.close()
    db.close()

def test():
    tkMessageBox.showinfo("Hello","World")

def gui():
    t=Tkinter.Tk()
    t.minsize(width=333,height=333)
    B= Tkinter.Button(text ="Hello World", command = test )
    B.pack()
    t.mainloop()
    print "Hello World"

def song():
    root = Tk()
    filename = "H:\eagle get"+"/"+"01 - Jiyo Re Bahubali - DownloadMing.SE.mp3"
    f= mp3play.load(filename)
    play = lambda :f.play()
    Button = Tkinter.Button(root,text="Play Song" , command=play)
    Button.pack()
    root.mainloop()

def select(event):
    widget = event.widget
    select= widget.curselection()
    picked  = widget.get(select[0])
    print picked

def listsong():
    filename = "E:\cinema songs\Dhruva\Dhruva (2016) ~320Kbps"
    songs= os.listdir(filename)
    root = Tk()
    root.minsize(width=666,height=666)
    box = Listbox(root,width = 333, height= 333)
    box.bind('Select',select)
    box.pack()
    for x in songs :
        box.insert(END,x)


    root.mainloop()

def frame():
    root = Tk()
    sep =Frame(height= 760 ,width=1368, bd =1 , relief =SUNKEN)
    sep.pack(fill= X , padx=2, pady=2)
    root.mainloop()

def playSongs(songs,index):
    global i,f,location
    try:
        if f.ispaused() and i==index:
            f.unpause()
        else:
            print "Hello"
            if index <0 :
                index=0
            if index >= len(songs):
                index=len(songs)-1
            i=index
            filename =  location+"/"+str(songs[index])
            print filename
            f= mp3play.load(filename)
            f.play()
            print f.isplaying(),f.ispaused(),f.volume(100),i
            print "World"
    except:
        if index <0 :
            index=0
        if index >= len(songs):
            index=len(songs)-1
        i=index
        filename = location + "/" + str(songs[index])
        f = mp3play.load(filename)
        f.play()
        print f.isplaying(), f.ispaused(), f.volume(100), i

def pause(songs,index):
    global i,f
    try:
        if f.isplaying() :
            f.pause()
    except:
        pass

def nop():
    global root
    filewin = Toplevel(root)
    button = Button(filewin, text="NO Operation")
    button.pack()

<<<<<<< HEAD
def nav():
    global root
=======
def allButton():
    global i,songs,location,root
    location="E:\cinema songs\Dhruva\Dhruva (2016) ~320Kbps"
    i=0
    songs = os.listdir(location)
    root = Tk()
    root.minsize(width=100,height=100)
    root.resizable(width=False,height=False)
>>>>>>> 7f2570c27b32376baa0e4c4281881d84c67319aa
    MenuBar = Menu(root)
    fileMenu = Menu(MenuBar, tearoff=0)
    fileMenu.add_command(label="New", command=nop)
    fileMenu.add_command(label="Open", command=nop)
    fileMenu.add_command(label="Save", command=nop)
    fileMenu.add_command(label="Save as...", command=nop)
    fileMenu.add_command(label="Close", command=nop)
    fileMenu.add_separator()

    fileMenu.add_command(label="Exit", command=root.quit)
    MenuBar.add_cascade(label="File", menu=fileMenu)
    editMenu = Menu(MenuBar, tearoff=0)
    editMenu.add_command(label="Undo", command=nop)

    editMenu.add_separator()

    editMenu.add_command(label="Cut", command=nop)
    editMenu.add_command(label="Copy", command=nop)
    editMenu.add_command(label="Paste", command=nop)
    editMenu.add_command(label="Delete", command=nop)
    editMenu.add_command(label="Select All", command=nop)

    MenuBar.add_cascade(label="Edit", menu=editMenu)
    helpMenu = Menu(MenuBar, tearoff=0)
    helpMenu.add_command(label="Help Index", command=nop)
    helpMenu.add_command(label="About...", command=nop)
    MenuBar.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=MenuBar)


def allButton():
    global i,songs,location,root
    location="H:\Music\English"
    i=0
    songs = os.listdir(location)
    root = Tk()
    root.minsize(width=100,height=100)
    nav()
    pauseCommand = lambda : pause(songs,i)
    playCommand= lambda : playSongs(songs,i)
    nextCommand = lambda : playSongs(songs,i+1)
    prevCommand = lambda :playSongs(songs,i-1)
    browseCommand=lambda :fileDialogue()
    image1=PhotoImage(file="src/play.gif")
    play=Tkinter.Button(root,image=image1,command=playCommand)
    image2=PhotoImage(file="src/pause.gif")
    pau=Tkinter.Button(root,image=image2,command=pauseCommand)
    image3=PhotoImage(file="src/next_track.gif")
    next=Tkinter.Button(root,image=image3,command=nextCommand)
    image4=PhotoImage(file="src/previous_track.gif")
    prev = Tkinter.Button(root,image=image4,command = prevCommand)
    image5 = PhotoImage(file="src/browse.gif")
    brow=Tkinter.Button(root,image=image5,command=browseCommand)
    play.pack(side="left")
    pau.pack(side="left")
    next.pack(side="left")
    prev.pack(side="left")
    brow.pack(side="left")
    root.mainloop()

def fileDialogue():
    global location,songs,i
    root= Tk()
    file= tkFileDialog.askdirectory(parent=root,title="Choose a folder")
    print file
    location=file
    songs=os.listdir(location)
    i=0
    print location,songs[0]
    root.destroy()

def setup():
    os.system('cls')
    print "Please Run apache and mysql from xampp before procedding"
    try:
        temp=raw_input("Enter to continue....")
        username = raw_input("Enter Username of mysql : ")
        password= getpass.getpass("Enter Password for mysql :")
        database=raw_input("Enter exisiting Database name : ")
        test=list(password)
        db= MySQLdb.connect('localhost',username,password,database)
        cursor = db.cursor()
        cursor.execute("select version()")
        print cursor.fetchone()

    except:
        print "Unable to setup try again"

if __name__ == '__main__':
    print len(sys.argv),sys.argv
    if len(sys.argv) >2 :
        print "Wrong Input"
        exit()
    if sys.argv[1] == 'setup' :
        setup()
    printdb()
