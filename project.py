import sqlite3

# con = sqlite3.connect('client.db')

# cursor = con.cursor()
# cursor.execute("""CREATE TABLE cleintDB ( 
#             first_name TEXT,
#             last_name TEXT, 
#             number TEXT)""")
# cursor.execute("""INSERT INTO cleintDB VALUES 
#                ('AAAA', 'BBBBB', '989878909'),
# ('CCCC', 'DDDD', '872348909'),
# ('EEEE', 'FFFF', '19078909'),
# ('GGGG', 'HHHH', '9887878909'),
#                ('HHHHH', 'BBBBB', '889878909'), 
#                ('IIIII', 'DDDD', '172348909'),
#                ('JJJJ', 'FFFF', '29078909'),
#                ('KKK', 'HHHH', '0887878909')""")

# Commit is needed after the insert, update, delete
# in case commit is not done then these change are temporary
# con.commit()
# cursor.execute('SELECT rowid, * FROM cleintDB')
# items=cursor.fetchall()
# for item in items:
#     print(item)

# Query the DB and return all records 
def show_all(): 
    # connect to db 
    con = sqlite3.connect('client.db')
    # create cursor 
    cursor = con.cursor()
    cursor.execute('SELECT rowid, * FROM cleintDB')
    items=cursor.fetchall()
    for item in items:
        print(item)
    # close connection
    cursor.close()

def add_one(): 
    con = sqlite3.connect('client.db')
    cursor = con.cursor()
    cursor.execute("INSERT INTO cleintDB VALUES ('RRRRR', 'NNNNNN', '12344556')")
    con.commit()
    con.close()
    
def add_value(first_name, last_name, number): 
    con = sqlite3.connect('client.db')
    cursor = con.cursor()
    cursor.execute("INSERT INTO cleintDB VALUES (?, ?, ?)", (first_name, last_name, number))
    con.commit()
    con.close()

def delete_one(id):
    con = sqlite3.connect('client.db')
    cursor = con.cursor()
    cursor.execute("DELETE FROM cleintDB WHERE rowid = (?)", id)
    con.commit()
    con.close()

# The way I implemented it 
# def add_many(list): 
#     con = sqlite3.connect('client.db')
#     cursor = con.cursor()
#     for item in list: 
#      cursor.execute("INSERT INTO cleintDB VALUES (?, ?, ?)", (item[0], item[1], item[2]))
#     con.commit()
#     con.close()

# executemany is new way to do it. 
def add_many(list): 
    con = sqlite3.connect('client.db')
    cursor = con.cursor()
    cursor.executemany("INSERT INTO cleintDB VALUES (?, ?, ?)", (list))
    con.commit()
    con.close()

def number_lookup(number):
    con = sqlite3.connect('client.db')
    cursor = con.cursor()
    cursor.execute('SELECT rowid, * FROM cleintDB WHERE number = (?)', (number,))
    item = cursor.fetchall()
    for i in item: 
        print(i)
    con.close()