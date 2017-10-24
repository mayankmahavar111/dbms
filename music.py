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
import mutagen
import re
from mutagen.mp3 import MP3
from PIL import ImageTk,Image

i=0

def printdb():
    db = createDb()
    cursor = db.cursor()
    ch=0
    os.system('cls')
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
        except Exception as e:
            print e
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
    global i, f, location
    try:
        if f.ispaused() and i == index:
            f.unpause()
        else:
            if index < 0:
                index = 0
            if index >= len(songs):
                index = len(songs) - 1
            i = index
            filename =str(songs[index])
            f = mp3play.load(filename)
            f.play()
            art(songs,i)
            print filename,f.isplaying(), f.ispaused(), f.volume(100), i
    except:
        if index < 0:
            index = 0
        if index >= len(songs):
            index = len(songs) - 1
        i = index
        filename =str(songs[index])
        f = mp3play.load(filename)
        f.play()
        art(songs, i)
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

def art(songs,i):
    global root,panel
    db=callDb()
    cursor=db.cursor()
    query=getQuery('get album')
    query=query.format(
        track_name=songs[i].split('/')[-1]
    )
    try:
        cursor.execute(query)
        temp= cursor.fetchone()[0]
        quer=getQuery('get image')
        quer=quer.format(
            albumid=temp
        )
        cursor.execute(quer)
        temp=cursor.fetchone()[0]
        x = Image.open(temp)
        x = x.resize((600, 600))
        img = ImageTk.PhotoImage(x)
        #print "hello"
        panel.configure(image=img)
        panel.image = img
        #print "World"
        root.mainloop()
    except Exception as e:
        print e
        pass
    cursor.close()
    db.close()
    pass

def nav():
    global root
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


def allButton(songs):
    global i, root,panel
    i = 0
    root = Tk()
    root.minsize(width=100,height=100)
    root.resizable(width=False,height=False)
    nav()
    print "Hello World"
    pauseCommand = lambda : pause(songs,i)
    playCommand= lambda : playSongs(songs,i)
    nextCommand = lambda : playSongs(songs,i+1)
    prevCommand = lambda :playSongs(songs,i-1)
    browseCommand=lambda :fileDialogue()
    img=Image.open('naruto-02.jpg')
    temp=img.resize((600,600))
    img = ImageTk.PhotoImage(temp)
    panel = Tkinter.Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
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
    #print file
    location=file
    songs=os.listdir(location)
    i=0
    #print location,songs[0]
    root.destroy()
    return file

def setup():
    os.system('cls')
    try:
        db= createDb()
        cursor = db.cursor()
        temp=raw_input("Do you want to setup new database(Y/N) : ")
        if 'Y' in temp or 'y' in temp:
            os.system('cls')
            database=raw_input("Enter new database name : ")
            try:
                cursor.execute("create database "+database)
                cursor.execute('use '+database)
            except Exception as e:
                print e
                cursor.execute("show databases")
                print cursor.fetchall()
                temp=raw_input("Enter to continue ...")
            os.system('cls')
        temp=raw_input("Do You Want to setup Tables (Y/N) : ")
        if 'Y' in temp or 'y' in temp :
            text=read().split(";")
            for x in text:
                try:
                    print x
                    cursor.execute(x+';')
                except Exception as e:
                    print e
            cursor.execute("show tables")
            print cursor.fetchall()
            """
            try:
            cursor.execute(text)
            cursor.execute("show tables")
            print "Total Tables are : "
            print cursor.fetchall()
            except Exception as e :
            print e
            """
        print "Succesfully Setup"
        print "run insert command to add songs initialy"
    except:
        print "Unable to setup try again"

def read():
    text=""
    f= open('tables.sql')
    lines=f.read()
    lines= re.split('\n |\n\t |',lines)
    for x in lines:
        text= text + " "+ x
    return text

def storCredentials(username,password,host,databse):
    f= open('Credential.txt','wb')
    f.write(username+'\n'+password+'\n'+host+'\n'+databse)
    f.close()

def callDb():
    lines=[]
    with open('Credential.txt','r') as f:
        lines=f.readlines()
    username=lines[0].split('\n')[0]
    password=lines[1].split('\n')[0]
    host=lines[2].split('\n')[0]
    database=lines[3].split('\n')[0]
    db = MySQLdb.connect(host,username,password,database)
    return db


def createDb():
    print "Please Run apache and mysql from xampp before procedding"
    try:
        temp = raw_input("Enter to continue....")
        os.system('cls')
        username = raw_input("Enter Username of mysql : ")
        password = getpass.getpass("Enter Password for mysql :")
        database = raw_input("Enter exisiting/Current Database name : ")
        test = list(password)
        db = MySQLdb.connect('localhost', username, password, database)
        cursor = db.cursor()
        cursor.execute("select version()")
        print cursor.fetchone()
        storCredentials(username,password,'localhost',database)
        return db
    except Exception as e:
        print e

def check(db):
    try:
        print "Checking the choosen database is fit for insert track or not"
        cursor=db.cursor()
        track=['TrackId','Album_name','AlbumId','Track_name','Location','Released_date','length','Favourite']
        cursor.execute("select column_name from information_schema.columns where table_name='track'")
        data = cursor.fetchall()
        data= list(set(data))
        print len(data)
        if len(data) < len(track):
            print "Tables are not created succesfully. setup again"
        count =0
        for i in range(len(data)):
            if data[i][0] in track :
                count =  count + 1
            #print re.split('( |,) ',data[0])[0] in track
        if len(track) == count :
            print "Fit to procced"
        else:
            print "Not enough entities to proceed ..."
            exit()
    except Exception as e:
        print e
        exit()

def display(track):
    root= Tk()
    root.maxsize(width=400,height=400)
    destroyCommand = lambda  : root.destroy()
    box = Listbox(root)
    button =Button(root,text="Add",command = destroyCommand,width=10)
    #back=Button(root,text="Back",command=insert,width=10)
    box.pack()
    for x in track:
        box.insert(END,x)
    button.pack()
    #back.pack()
    root.mainloop()


def getTrack(file):
    track =[]
    for x in os.listdir(file):
            if x.endswith(".mp3"):
                track.append(x)
    #print location,songs[0]
    return track

def showTable(x):
    for row in x:
        print row

def getFlag(data,key):
    for x in data:
        if x[0] == key:
            return False
    return True

def getRelid(a,b):
    for x in a :
        #print x,a
        if x[0]==b[0] and x[1] == b[1]:
            return False
    return True

def getid(x):
    if x is None:
        return 1
    else:
        return int(x)+1

def getQuery(x):
    if x=="insert_album":
        return """insert into album (albumid,album_name,No_Of_Tracks) VALUES ("{albumid}","{album_name}","{length}")"""
    if x=="insert_track":
        return """insert into track (trackid,albumid,album_name,track_name,location,released_date,length,favourite ) VALUES ("{trackid}","{albumid}","{album_name}","{track_name}","{track_location}","{released_date}","{track_length}",0)"""
    if x=="insert_art":
        return """insert into album_art (albumartid,image,albumid) values ("{artid}","{image}","{albumid}")"""
    if x=="insert_genre":
        return """insert into genre (genreid,genrename) VALUES ("{genreid}","{genre_name}")"""
    if x=="insert_type":
        return """insert into type (albumid,trackid,genreid) VALUES ("{albumid}","{trackid}","{genreid}")"""
    if x=="get album":
        return """select albumid from track where track_name="{track_name}"  """
    if x=="get image":
        return """select image from album_art where albumid="{albumid}" """

def query(db,file,tracks,index):
    cursor=db.cursor()
    if index == 'insert':
        try:
            for x in tracks:
                try:
                    cursor.execute("select max(trackid) from track")
                    data =  cursor.fetchone()
                    trackid=getid(data[0])
                    cursor.execute("select max(albumid) from album")
                    data=cursor.fetchone()
                    albumid=getid(data[0])
                    details= filedetails(x,file)
                    #print details
                    #print "hello"
                    album_name = str(details.get('TALB'))
                    track_name = x
                    #print "world"
                    track_location = str(details.filename)
                    released_date = str(details.get('TDRC'))
                    track_length = int(tracklength(x,file))
                    genre_name=str(details.get('TCON'))
                    try:
                        image=details.tags['APIC:'].data
                    except:
                        pass


                    #album Table
                    album_sql=getQuery('insert_album')
                    album_sql=album_sql.format(
                        albumid=albumid,
                        album_name=album_name,
                        length=len(tracks)
                    )
                    cursor.execute("select album_name from album")
                    if getFlag(cursor.fetchall(),album_name):
                        cursor.execute(album_sql)
                        db.commit()


                    #Track Table
                    q='select albumid from album where album_name="'+album_name+'"'
                    #print q
                    cursor.execute(q)
                    albumid=cursor.fetchone()[0]
                    insert_sql= getQuery('insert_track')
                    #sql = """insert into track (trackid,album_name,track_name,location,released_date,length,favourite ) VALUES (%d,%s,%s,%s,%s,%d,0) """,(trackid,album_name,track_name,track_location,released_date,track_length)
                    format_sql =insert_sql.format(
                        trackid=trackid,
                        albumid=albumid,
                        album_name=album_name,
                        track_name=track_name,
                        track_location=file,
                        released_date=released_date,
                        track_length=track_length
                    )
                    cursor.execute("select track_name from track ")
                    data=cursor.fetchall()
                    if getFlag(data,track_name):
                        cursor.execute(format_sql)
                        print "Track id ", "=", trackid
                        print format_sql
                        db.commit()

                    #Album Art Table
                    cursor.execute('select max(albumartid) from album_art')
                    artid = getid(cursor.fetchone()[0])
                    cursor.execute('select image from album_art')
                    art_sql=getQuery('insert_art')
                    if getFlag(cursor.fetchall(),'albumart/'+str(album_name)+'.jpg'):
                        try:
                            with open('albumart/'+str(album_name)+'.jpg','wb') as f :
                                f.write(image)
                            art_sql = art_sql.format(
                                artid=artid,
                                image='albumart/' + str(album_name)+'.jpg',
                                albumid=albumid
                            )
                        except:
                            art_sql = art_sql.format(
                                artid=artid,
                                image='None',
                                albumid=albumid
                            )
                        cursor.execute(art_sql)
                        db.commit()


                    #Genre Table
                    cursor.execute('select max(genreid) from genre')
                    genreid=getid(cursor.fetchone()[0])
                    genre_sql=getQuery('insert_genre')
                    cursor.execute('select genrename from genre')
                    if getFlag(cursor.fetchall(),genre_name):
                        genre_sql=genre_sql.format(
                            genreid=genreid,
                            genre_name=genre_name
                        )
                        cursor.execute(genre_sql)
                        db.commit()

                    #Type Relationship

                    #print "Hello"
                    q = 'select trackid from track where track_name="' + track_name + '"'
                    cursor.execute(q)
                    trackid = cursor.fetchone()[0]
                    q = 'select genreid from genre where genrename="' + genre_name + '"'
                    cursor.execute(q)
                    genreid = cursor.fetchone()[0]
                    type_sql=getQuery('insert_type')
                    cursor.execute('select albumid,trackid from type')
                    data=cursor.fetchall()
                    #print "World"
                    b=[albumid,trackid]
                    if getRelid(data,b):
                        type_sql=type_sql.format(
                            albumid=albumid,
                            genreid=genreid,
                            trackid=trackid
                        )
                        cursor.execute(type_sql)
                        db.commit()
                except:
                    continue

            cursor.execute("select * from track")
            showTable(cursor.fetchall())
        except Exception as e:
            print  e
        return


def insert():
    try:
        db=createDb()
        check(db)
        #print "hello"
        file=fileDialogue()
        track=getTrack(file)
        #print "world"
        print len(track)
        display(track)
        query(db,file,track,'insert')
        #filedetails(track,file)

    except Exception as e:
        print e

def tracklength(track,file):
    #print "hello"
    x= MP3(file+"/"+track)
    #print "world"
    return x.info.length

def filedetails(track,file):
    d= mutagen.File(file+'/'+track)
    return d

def getSong(data):
    songs=[]
    for x in data:
        songs.append(x[1]+'/'+x[0])
    return songs

def musicplayer():
    db = callDb()
    cursor = db.cursor()
    cursor.execute('select version()')
    # print cursor.fetchone()[0]
    cursor.execute('select track_name,location from track order BY rand()')
    data = cursor.fetchall()
    songs = getSong(data)
    cursor.close()
    db.close()
    allButton(songs)

if __name__ == '__main__':
    try:
        if len(sys.argv) >2 :
            print "Wrong Input"
            exit()
        if sys.argv[1] == 'setup' :
            setup()
        if sys.argv[1] == 'insert':
            insert()
        if sys.argv[1] == 'prompt':
            printdb()
        if sys.argv[1] == 'musicplayer':
            musicplayer()
    except Exception as e:
        print e