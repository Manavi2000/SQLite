import sqlite3

#create the connection 
# In this case it will create the connection to db, we mention name in it if the db exist 
# we will be able to use it or if db don't exist then new db will be created with this name. 
con = sqlite3.connect('customer.db')

#after running it we saw that db is craeted. 

# In case we want a db for little calulation then we used this menthod, that we will 
# be able to do action on it, afterward it would be deleted. 
#con = sqlite3.connect(':memory:')

# cusror is used to perform action over the table, create cursor from it. 
cursor = con.cursor()

# Now using cursor we will excute command on db
# Now we have used """"""" : as it allow to enter the command in mutiple line also which increase readablility. 
# cursor.execute("""CREATE TABLE customers (
#     first_name TEXT, 
#     last_name TEXT,
#     email TEXT  
#     )""")

# DATATTYPE
# NULL : it exist or not 
# INTEGER : number 
# REAL : decimal 
# TEXT : string
# BLOB : as it is i.e image, png

#Adding value to table : 
# cursor.execute("""INSERT INTO customers 
#                VALUES 
#                ('Mary', 'Brown', 'Mary@gmail.com')
#                """)

#adding multiple value to table : 

# many_customers=[('Was','Yadav', 'a@ibm.com'),
#                ('Text', 'Kim', 'kim@inm.com'),
#                ('OM', 'abv', 'abv@om.com')]
# cursor.executemany("""INSERT INTO customers VALUES (?,?,?)""", many_customers)

cursor.execute("""SELECT * FROM customers""")
#cursor.fectchall() : will fect all the information but to see on the bacsh you need to print it. 
#cursor.fectone(): will fetch the first one only.
#cursor.fectmany(3) : will fect number of input we mentioned. 
#print(cursor.fetchall()) # return the python list [(),()] in this form. 
# print(cursor.fetchone()[0])
# print(cursor.fetchone()[1])
# print(cursor.fetchone()[2])

items = cursor.fetchall()
for item in items: 
    print(item)
    
# each will be printed as tuple 
# way to format the output of the databse. 
# ('Jhon', 'Elder', 'john@gmail.com')
# ('Tim', 'Old', 'TIMAn@gmail.com')
# ('Mary', 'Brown', 'Mary@gmail.com')
# ('Was', 'Yadav', 'a@ibm.com')
# ('Text', 'Kim', 'kim@inm.com')
# ('OM', 'abv', 'abv@om.com')
print("NAME "+"\t\t"+"EMAIL")
for item in items: 
    print(item[0] + "\t\t"+item[2])
    
    
#primmary id : unique value in the table. 
# So sqlite create this id on it own. we don;t have to create it 
# to see it print the rowid, if we specify that we don't want primary key then it will not create it own
# but majorly we want it only
cursor.execute("""SELECT rowid,* FROM customers""")
print(cursor.fetchall())
print('Command excuted succesfully')
# it will commit our changes, 
con.commit()

#logical oprator can also be used here.  =, >= , <= 
cursor.execute("""SELECT * FROM customers WHERE first_name = 'Jhon'
               """)
print(cursor.fetchall())
cursor.execute("""SELECT * FROM customers WHERE last_name LIKE 'ki%'
               """)
print(cursor.fetchall())
cursor.execute("""SELECT * FROM customers WHERE email LIKE '%.com'
               """)
print(cursor.fetchall())

#everytime we create a connection we try to cclose it 
con.close()