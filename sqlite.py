import sqlite3

connection = sqlite3.connect("example.db")
cursor = connection.cursor()

#------------------------------------------------------------------------


##Create a Table
cursor.execute('''
Create Table if Not Exists employees(
    id Integer Primary Key,
    name Text Not Null,
    age Integer,
    department text
    )
''')

##Commit the changes
connection.commit()


#------------------------------------------------------------------------


##Insert the data in table
# cursor.execute('''
#     Insert Into employees(name,age,department) values("Ishwar",35,"AI/ML")
# ''')

# cursor.execute('''
#     Insert Into employees(name,age,department) values("Russell",24,"Mechanical")
# ''')

# ##Commit the changes
# connection.commit()

#------------------------------------------------------------------------

##Queery the data
cursor.execute("Select * from employees")
rows=cursor.fetchall()

#Read query data
# for row in rows:
#     print(row)


#------------------------------------------------------------------------
#Update the data
# cursor.execute('''
#     UPDATE employees Set age=19 where name="Ishwar"
# ''')

# ##Commit the changes
# connection.commit()

# #print query data
# for row in rows:
#     print(row)


#------------------------------------------------------------------------
#Delete the data

# cursor.execute('''
#     Delete from employees where name = "Ishwar"
# ''')

# connection.commit()

# for row in rows:
#     print(row)

#------------------------------------------------------------------------
#Close the connection
connection.close()


