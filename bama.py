import requests
from bs4 import BeautifulSoup
import re 
import mysql.connector
cnx=mysql.connector.connect(user='root',host='localhost',password='mahdis8731abd',database='bama_cars')
cur=cnx.cursor()
query =( "INSERT INTO cars_info(name,model,us,location,price) " 
            "VALUES(%s,%s,%d,%s,%d)")
#for i in range(0,100):
r=requests.get('https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true')
soup=BeautifulSoup(r.text,'html.parser')
cars=soup.find_all('li',class_="car-list-item-li")
for car in cars:
    fname=car.find('span',class_="ad-title-span").text
    usage=car.find('p',class_="price hidden-xs").text
    
    print(usage)
    location=car.find('span',class_="provice-mobile").text
    price=car.find('span',attrs={'itemprop':'price'}).get('content')
    if(len(re.findall(r'د‌ر‌ک‌ر‌ا‌ک(.*)',usage))!=0 and re.findall(r'د‌ر‌ک‌ر‌ا‌ک(.*)',usage)[0]=='ر‌ف‌ص'):
        us='0'
    elif usage=='-':
        us='0'
    else:
        us=re.findall(r'د‌ر‌ک‌‌ر‌‌ا‌ک(.*)',usage)[0]
    us=re.sub(r',','',usage)
    fname=re.sub(r'\s+','',fname).strip()
    if (re.findall(r'(.*)،.*،.*',fname)==[]):
        name=re.findall(r'(.*)،.*',fname)[0]
    else:
        name=re.findall(r'(.*)،.*،.*',fname)[0]
    if (re.findall(r'.*،(.*)،.*',fname)==[]):
        model=re.findall(r'.*،(\d*\w*\d*)',fname)[0]
    else:
        model=re.findall(r'.*،(.*)،.*',fname)[0]
    #data=(name,model,int(usage),location,int(price))
    #cur.execute(query,data)
    #cnx.commit()
cnx.close()