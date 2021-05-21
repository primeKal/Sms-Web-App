import sqlite3


#
# command = '''CREATE TABLE IF NOT EXISTS sms(no INTEGER PRIMARY KEY, sender TEXT,destination TEXT, message TEXT
# ,Mid TEXT,Api TEXT)'''

# cursor.execute(command)
# cursor.execute('INSERT INTO sms VALUES (1, "+2511111", "+2511343434", "dummy message", "dummyid", "SMPP")')
# cursor.execute('INSERT INTO sms VALUES (2, "+251134343", "+251115565", "dummy message", "dummyid", "SMPP")')
# cursor.execute('INSERT INTO sms VALUES (3, "+251665432", "+251116565", "dummy message", "dummyid", "SMPP")')
# cursor.execute('INSERT INTO sms VALUES (4, "+251567656", "+2511111565", "dummy message", "dummyid", "SMPP")')
#
#
# print(type(result))

def fetch_all_list():
    connection = sqlite3.connect("Messages,db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM sms")
    result = cursor.fetchall()
    print(type(result))
    return result


def save_data(no, sender, dest, mess, mid, api):
    connection = sqlite3.connect("Messages,db")
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO sms VALUES (?,?,?,?,?,?)', (no, sender, dest, mess, mid, api))
    connection.commit()
    print("saved")


def fetcha_data(no):
    print(no, "fetch starting")
    print(type(no))
    connection = sqlite3.connect("Messages,db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM sms WHERE no=?", (no,))
    result = cursor.fetchall()
    print(type(result))
    return result

def fetch_sener():
    print("fetch senders")
    connection = sqlite3.connect("Messages,db")
    cursor = connection.cursor()
    cursor.execute("SELECT sender FROM sms")
    send=cursor.fetchall()
    print(send)
    return send

def fetch_destinations():
    print("fetch senders")
    connection = sqlite3.connect("Messages,db")
    cursor = connection.cursor()
    cursor.execute("SELECT destination FROM sms")
    des=cursor.fetchall()
    print(des)
    return des
def save_des(no,orgin,text,mid):
    print("saving messages")
    connection = sqlite3.connect("Messages,db")
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO mo VALUES (?,?,?,?)', (no, orgin, text, mid))
    connection.commit()
    print("saved")

def fetch_mo():
    print("fetch mo")
    connection = sqlite3.connect("Messages,db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mo")
    des=cursor.fetchall()
    print(des)
    return des


#
# command = '''CREATE TABLE IF NOT EXISTS mo(no INTEGER PRIMARY KEY, orgin TEXT, message TEXT
# ,Mid TEXT)'''
# connection = sqlite3.connect("Messages,db")
# cursor = connection.cursor()
# cursor.execute(command)
#
# cursor.execute(command)
# cursor.execute('INSERT INTO mo VALUES (1, "+2511111",  "dummy message", "dummyid")')
# cursor.execute('INSERT INTO mo VALUES (2, "+2511111",  "dummy message", "dummyid")')
# cursor.execute('INSERT INTO mo VALUES (3, "+2511111",  "dummy message", "dummyid")')
# cursor.execute('INSERT INTO mo VALUES (4, "+2511111",  "dummy message", "dummyid")')
#
#
#
# connection.commit()