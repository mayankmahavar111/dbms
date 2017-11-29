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

def checkPlaylist(db):
    query="select playlistid from playlist where playlistname='mostplayed'"
    cursor=db.cursor()
    cursor.execute(query)
    temp=cursor.fetchone()
    if temp==None:
        query="select max(playlistid) from playlist"
        cursor.execute(query)
        playid=int(cursor.fetchone()[0])
        query='insert into playlist (playlistid,playlistname) VALUES ('+str(playid)+',"mostplayed"'+')'
        print query
        cursor.execute(query)
        db.commit()
    return


def main():
    db=callDb()
    checkPlaylist(db)

main()