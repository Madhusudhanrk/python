import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "username",
    password = "password",
    dbname = "some"
)
mycursor = mydb.cursor()
mycursor.execute("select * from dbname")
val = mycursor.fetchall()
for i in val:
    print(i)

# del student 
#del from student where condition

# update student set(name="dfadf") where condition

#insert into student(c,c2,c3)values(v,v2,v3)
#create table student (cname,int,unique)