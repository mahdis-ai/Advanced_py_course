import mysql.connector
cnx=mysql.connector.connect(user='root',host='localhost',password='mahdis8731abd',database='empolyee')
cur=cnx.cursor()
query=("SELECT * FROM employers ORDER BY height DESC,weight ASC")
cur.execute(query)
result=cur.fetchall()
for i in result:
    print(i[0],i[1],i[2])