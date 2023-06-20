import eng_to_ipa as pa
import sqlite3 as sq

conn = sq.connect("project.db")
cur = conn.cursor()
fp = open("programs\word.txt","r")
words=fp.read().split('\n')
# print(words)
fp.close()
fp = open('programs\syl.txt','r')
syl=fp.read().split('\n')
# print(syl)
fp.close()

def phone(word):
    phon = pa.convert(word)
    return phon
c=1
for i in words:
    cur.execute("insert into vocabulary values({},'{}','{}','{}')".format(c,i,phone(i),syl[words.index(i)]))
    c+=1
conn.commit()
conn.close()
    


