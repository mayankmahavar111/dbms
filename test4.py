
from Tkinter import *
import os
import MySQLdb


def listSong(track):
    root= Tk()
    root.maxsize(width=400,height=400)
    destroyCommand = lambda  : root.destroy()
    box = Listbox(root)
    button =Button(root,text="play",command = destroyCommand,width=10)
    #back=Button(root,text="Back",command=insert,width=10)
    box.pack()
    for x in track:
        box.insert(END,x.split('/')[-1])
    button.pack()
    #back.pack()
    root.mainloop()

def showList(temp,cursor):
   test=[]
   for x in temp:
      test.append(getLocation(cursor,x))
   listSong(test)

def getLocation(cursor,x):
   query="select location from track where track_name like '%"+x[0]+"%'"
   print query
   try:
      cursor.execute(query)
      return cursor.fetchone()[0]+'/'+x[0]
   except Exception as e:
      print e

def doubleSearch(text,table):
   if 'track' in table:
      temp='select track_name from type,'+table[0]+','+table[1]+' where '
      temp+=table[0]+'.'+get(table[0]) +" like '%"+text+"%'"
      temp+=' or '+table[1]+'.'+get(table[1]) + " like '%"+text+"%'"
      temp+=' and type.'+table[0]+'id='+table[0]+'.'+table[0]+'id'
      temp+=' and type.'+table[1]+'id='+table[1]+'.'+table[1]+'id'
      return temp
   else:
      temp = 'select track_name from type,track,' + table[0] + ',' + table[1] + ' where '
      temp += table[0] + '.' + get(table[0]) + " like '%" + text + "%'"
      temp += ' or ' + table[1] + '.' + get(table[1]) + " like '%" + text + "%'"
      temp += ' and type.' + table[0] + 'id=' + table[0] + '.' + table[0] + 'id'
      temp += ' and type.' + table[1] + 'id=' + table[1] + '.' + table[1] + 'id'
      temp+= ' and type.trackid=track.trackid'
      return temp
def singleSearch(text,table):
   temp="select "+table+"."+get(table)+" from "+table+" where "+get(table)+" like '%"+text+"%' "
   #temp+=" and type."+table+"id"+"="+table+"."+table+"id"
   #temp+=" and type.trackid=track.trackid"
   return temp


def join(text):
   temp = "select track.track_name from track inner JOIN  TYPE ON TYPE.Trackid = track.trackid inner join  album ON TYPE.albumid=album.albumid inner JOIN  genre on TYPE.genreid = genre.genreid"
   temp += " and track.track_name like '%" + text + "%'"
   temp += " or album.album_name like '%" + text + "%'"
   temp += " and track.album_name = album.album_name"
   temp += " and type.trackid=track.trackid"
   temp += " and type.genreid =  genre.genreid"
   return temp

def get(x):
   if x.lower() =='album':
      return 'album_name'
   if x.lower() == 'track':
      return 'track_name'
   if x.lower() == 'genre':
      return 'genrename'
   return ''

def showTable(x):
   for row in x:
     print row
   print len(x)

def callDb():
    with open('Credential.txt','r') as f:
        lines=f.readlines()
    username=lines[0].split('\n')[0]
    password=lines[1].split('\n')[0]
    host=lines[2].split('\n')[0]
    database=lines[3].split('\n')[0]
    db = MySQLdb.connect(host,username,password,database)
    return db


def allstates(lng,dic,textBox,root):
   os.system('cls')
   x= lng.state()
   test=[]
   for i in range(len(x)):
      if x[i] == 1 :
         test.append(dic[i])
         print dic[i],' is selected'
   text=textBox.get("1.0","end-1c")
   text=text.split('\n')[0]
   if len(test)==0:
      temp=join(text)
   if len(test)==1:
      temp=singleSearch(text,test[0])
   if len(test)==2:
      temp=doubleSearch(text,test)
   """
   temp='select * from '
   temp2=[]
   for i in test:
      temp2.append(i)
   temp+=','.join(temp2)
   temp+=" where "
   temp2=len(test)
   if temp2>1:
      for i in test:
         temp+=i+"."+test[i]+' like "%'+text+'%"'
         if temp2>1:
            temp += " or "
         temp2-=1
      temp2=len(test)
      temp+=" and "
      for i in test:
         if temp2==1:
            temp+=i+"."+"albumid"
            break
         temp+=i+"."+"albumid"+"="
         temp2-=1
   else:
      for i in test:
         temp += test + ' like "%' + text + '%"'
   """
   print temp
   db=callDb()
   cursor=db.cursor()
   try:
      cursor.execute(temp)
      temp=cursor.fetchall()
      showTable(temp)
   except Exception as e:
      print e
      pass
   root.destroy()
   showList(temp,cursor)


class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)


def Search():
   root = Tk()
   dic=['Artist', 'Album', 'track','Genre']
   lng = Checkbar(root,dic )
   lng.pack(side=TOP,  fill=X)
   lng.config(relief=GROOVE, bd=2)
   textBox = Text(root, height=2, width=10)
   textBox.pack()
   searchCommand= lambda :allstates(lng,dic,textBox,root)
   Button(root, text='Search', command=searchCommand).pack(side=RIGHT)
   root.mainloop()


Search()