import sqlite3


def connect():
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user (id INT PRIMARY KEY, discordTag VARCHAR(20), discordId VARCHAR(50), happy INT, sad INT)")
    conn.commit()
    conn.close()

def insert(discordTag, discordId, happy, sad):
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO user VALUES(NULL,?,?,?,?)",(discordTag, discordId, happy, sad))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(discordTag="", discordId=""): #Only one section should be able to be inputted, so to avoid error set default values to ""
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE discordTag=? OR discordId=?",(discordTag, discordId)) #OR so that only one section can be inputted to get values
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(discordId):
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM user WHERE discordId=?",(discordId,))
    conn.commit()
    conn.close()

def update(discordTag, discordId, happy, sad):
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("UPDATE user SET discordTag=?,happy=?,sad=? WHERE discordId=?",(discordTag, happy, sad, discordId))
    conn.commit()
    conn.close()
