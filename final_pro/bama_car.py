import requests
from bs4 import BeautifulSoup
import re 
import mysql.connector
cnx=mysql.connector.connect(user='root',host='localhost',password='mahdis8731abd',database='bama_cars')
cur=cnx.cursor()
query ="""INSERT INTO cars_info
              (name,model,us,year, location, price) 
              VALUES (%s, %s, %s,%s, %s, %s)"""
for i in range(0,100):
    r=requests.get('https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page='+str(i))
    soup=BeautifulSoup(r.text,'html.parser')
    cars=soup.find_all('li',class_="car-list-item-li")
    for car in cars:
        fname=car.find('span',class_="ad-title-span").text
        usage=car.find('p',class_="price hidden-xs").text
        usage_edit=re.sub(r',','',usage).strip()
        location=car.find('span',class_="provice-mobile").text
        year_tag=car.find('span',attrs={'class':'price year-label hidden-xs','itemprop':'releaseDate'}).text
        year=re.findall(r'\d*',year_tag)[0]
        price=car.find('span',attrs={'itemprop':'price'}).get('content')
        if (re.findall(r'.*کارکرد(.*)',usage_edit)!=[]):
            us=re.findall(r'.*کارکرد(.*)',usage_edit)[0].strip()
            if( us=='صفر' ):
                us='0'
        else:
            us='0'
        fname=re.sub(r'\s+','',fname).strip()
        if (re.findall(r'(.*)،.*،.*',fname)==[]):
            name=re.findall(r'(.*)،.*',fname)[0]
        else:
            name=re.findall(r'(.*)،.*،.*',fname)[0]
        if (re.findall(r'.*،(.*)،.*',fname)==[]):
            model=re.findall(r'.*،(\d*\w*\d*)',fname)[0]
        else:
            model=re.findall(r'.*،(.*)،.*',fname)[0]
        data=(name,model,int(us),int(year),location,int(price))
        print(data)
        cur.execute(query,data)
        cnx.commit()
cnx.close()