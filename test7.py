from Tkinter import *
import MySQLdb
import os
import tkFileDialog

def callDb():
    with open('Credential.txt','r') as f:
        lines=f.readlines()
    username=lines[0].split('\n')[0]
    password=lines[1].split('\n')[0]
    host=lines[2].split('\n')[0]
    database=lines[3].split('\n')[0]
    db = MySQLdb.connect(host,username,password,database)
    return db

def playId(playlistname):
    db=callDb()
    cursor=db.cursor()
    query="select max(playlistid) from playlist"
    cursor.execute(query)
    temp=cursor.fetchone()[0]
    if temp == None :
        playlistid=1
    else:
        playlistid = int(temp) +1

    query='select playlistid from playlist where playlistname like "'+str(playlistname)+'"'
    try:
        cursor.execute(query)
        print cursor.fetchone()[0]
        return
    except Exception as e:
        print e
        exit()
    """
    if data != None:
        print "already exists"
        return
    query="insert into playlist VALUES ("+str(playlistid)+",'"+str(playlistname)+"')"
    print query
    cursor.execute(query)
    db.commit()
    return
    """


def retrieve_input(root,textBox):
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)
    root.destroy()
    playId(inputValue)
    insertPlaylist(inputValue)
    return


def CreatePlaylist():
    root = Tk()
    textBox = Text(root, height=2, width=10)
    textBox.pack()
    buttonCommit = Button(root, height=1, width=10, text="Commit",
                          command=lambda: retrieve_input(root,textBox))
    buttonCommit.pack()
    mainloop()

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

def getTrack(file):
    track =[]
    for x in os.listdir(file):
            if x.endswith(".mp3"):
                track.append(x)
    #print location,songs[0]
    return track


def insertPlaylist(playname):
    db=callDb()
    file = fileDialogue()
    track=getTrack(file)
    #print len(track)
    cursor=db.cursor()
    for x in track:
        query='select count(*) from track where track_name like "'+x+'"'
        cursor.execute(query)
        data=cursor.fetchone()[0]
        if data != 0 :
            try:
                print "Success"
                query='select playlistid from playlist where playlistname like "'+playname+'"'
                cursor.execute(query)
                playid=cursor.fetchone()[0]
                query='select trackid from track where track_name like "'+x+'"'
                cursor.execute(query)
                trackid=cursor.fetchone()[0]
                query='insert into contains VALUES ('+str(playid)+','+str(trackid)+')'
                print query
                cursor.execute(query)
                db.commit()
            except Exception as e:
                print e
                break
        else:
            print "Not inside track first add in track"
            break




#insertPlaylist()

CreatePlaylist()