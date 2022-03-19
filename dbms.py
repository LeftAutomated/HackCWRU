import sqlite3


def connect():
    # Connect to user.db
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user (id INT PRIMARY KEY, discordId VARCHAR(50), happy INT, sad INT)")
    # Connect to positive.db and negative.db
    words_conn = sqlite3.connect("databases/positive.db")
    words_cur = negative_conn.cursor()
    words_cur.execute("CREATE TABLE IF NOT EXISTS positive (id INT PRIMARY KEY, word VARCHAR(30))")
    words_cur.execute("CREATE TABLE IF NOT EXISTS negative (id INT PRIMARY KEY, word VARCHAR(30))")
    # Commit and close
    conn.commit()
    conn.close()

def insert(discordId, happy, sad):
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO user VALUES(NULL,?,?,?)",(discordId, happy, sad))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(discordId=""): #Only one section should be able to be inputted, so to avoid error set default values to ""
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE discordId=?",(discordId)) #OR so that only one section can be inputted to get values
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(discordId):
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM user WHERE discordId=?",(discordId,))
    conn.commit()
    conn.close()

def update(discordId, happy, sad):
    conn = sqlite3.connect("databases/user.db")
    cur = conn.cursor()
    cur.execute("UPDATE user SET happy=?,sad=? WHERE discordId=?",(happy, sad, discordId))
    conn.commit()
    conn.close()
