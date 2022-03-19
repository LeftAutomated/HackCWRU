import sqlite3

# User database functions
def userConnect():
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user (id INT PRIMARY KEY, discordId VARCHAR(50), happy INT, sad INT)")
    conn.commit()
    conn.close()

def userInsert(discordId, happy, sad):
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO user VALUES(NULL,?,?,?)",(discordId, happy, sad))
    conn.commit()
    conn.close()

def userView():
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")
    rows = cur.fetchall()
    conn.close()
    return rows

def userSearch(discordId=""): #Only one section should be able to be inputted, so to avoid error set default values to ""
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE discordId=?",(discordId,)) #OR so that only one section can be inputted to get values
    rows = cur.fetchall()
    conn.close()
    return rows

def userDelete(discordId):
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM user WHERE discordId=?",(discordId,))
    conn.commit()
    conn.close()

def userUpdate(discordId, happy, sad):
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("UPDATE user SET happy=?,sad=? WHERE discordId=?",(happy, sad, discordId))
    conn.commit()
    conn.close()


# Words database functions
def wordConnect():
    words_conn = sqlite3.connect("databases/words.db")
    words_cur = words_conn.cursor()
    conn.commit()
    conn.close()
