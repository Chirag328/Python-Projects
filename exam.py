import mysql.connector

# 1. Creating a Database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    charset='utf8'  
)

mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE college')
print('Database created successfully')

# 2. Creating a Table
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    charset='utf8'  
)

mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE students(F_name varchar(20), L_name varchar(20), Age int(10), Conatact_no int(11))')
print('Table created successfully')

# 3. Insert into Table
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    charset='utf8'  
)

mycursor = mydb.cursor()
sql = "INSERT INTO students(F_name, L_name, Age, Contact_no) VALUEs(%s,%s,%s,%s)"
val = ("Madhukar", "Bhagat", 18, 1234567890)
mycursor.execute(sql,val)
mycursor.commit()

#4. Fetch from Table
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    charset='utf8'  
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
    
#5. Update in the Table
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    charset='utf8'  
)

mycursor = mydb.cursor()
mycursor.execute("UPDATE students SET Contact_no=0987654321 WHERE Contact=1234567890")
mycursor.commit()

#6. Delete Table
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    charset='utf8'  
)

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE students")
print("Table deleted")


#6. Delete Database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    charset='utf8'  
)

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE college")
print("Database deleted")