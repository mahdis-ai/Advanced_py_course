import mysql.connector
from sklearn import tree 
from sklearn.preprocessing import OneHotEncoder
cnx=mysql.connector.connect(user='root',host='localhost',password='mahdis8731abd',database='bama_cars')
cur=cnx.cursor()
cur.execute("SELECT * FROM cars_info")
enc = OneHotEncoder(handle_unknown='ignore')
x=[]
y=[]
data=cur.fetchall()
for row in data:
    x.append([row[2],row[3]])
    y.append(row[5])
clf=tree.DecisionTreeClassifier()
clf.fit(x,y)
s=input("enter usage and year of car\n").split()
new_data=[s]
#test data
#new_data=[[19520,1387]]
ans=clf.predict(new_data)
print(ans[0])