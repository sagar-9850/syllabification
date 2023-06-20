import sqlite3 as sq
def splits(word):
    conn = sq.connect("project.db")
    cur = conn.cursor()
    cur.execute("select syllables from vocabulary where word = '"+word+"'") 
    rows = cur.fetchall()
    if len(rows)==0:
        return "#no data#"
    for i in rows:
        print(i[0])
        return i[0]
        

