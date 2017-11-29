from Tkinter import *
import MySQLdb


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

    query="insert into playlist VALUES ("+str(playlistid)+",'"+str(playlistname)+"')"
    print query
    cursor.execute(query)
    db.commit()

def retrieve_input(root,textBox):
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)
    root.destroy()
    playId(inputValue)



def CreatePlaylist():
    root = Tk()
    textBox = Text(root, height=2, width=10)
    textBox.pack()
    buttonCommit = Button(root, height=1, width=10, text="Commit",
                          command=lambda: retrieve_input(root,textBox))
    buttonCommit.pack()
    mainloop()

CreatePlaylist()