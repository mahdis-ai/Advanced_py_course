import mysql.connector
import re
cnx=mysql.connector.connect(user='root',host='localhost',password='mahdis8731abd',database='info')
cur=cnx.cursor()
query =( "INSERT INTO passinfo(email,username) VALUES(%s,%s)")


while(True):
    seq1=input('enter email\n')
    result=re.findall(r'\d*\w+\d*\w+@\w+\.\w+',seq1)
    if (len(result)==0 or result[0]!=seq1 ):
        seq1=input("enter the correct form\texpression@string.string\n")
    else:
        break

seq2=input('enter password\n')
if(not(seq2.isalnum())):
    print('invalid password')
data=(seq1,seq2)
cur.execute(query,data)
cnx.commit()
cnx.close()

    