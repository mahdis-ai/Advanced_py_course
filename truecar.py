import requests
import re
from bs4 import BeautifulSoup
import mysql.connector
cnx=mysql.connector.connect(user='root',host='localhost',password='mahdis8731abd',database='cars')
cur=cnx.cursor()
car_name=input()
query =( "INSERT INTO sale(price,uses) " 
            "VALUES(%s,%s)")
i=0
for page in range(0,100):
    if (page==0):
        r=requests.get('https://www.truecar.com/used-cars-for-sale/listings/?sort[]=best_match')
    else:
        r=requests.get('https://www.truecar.com/used-cars-for-sale/listings/?page='+str(page+1)+'&sort[]=best_match')
    soup= BeautifulSoup(r.text,'html.parser')
    value=soup.find_all('div',class_="card-content vehicle-card-body order-3")
    for val in value:
        name=val.find('span',class_="vehicle-header-make-model text-truncate")
        price=val.find('div',{'class':'heading-3 margin-y-1 font-weight-bold','data-test':'vehicleCardPricingBlockPrice'} )
        use=val.find('div',attrs={'class':'font-size-1 text-truncate','data-test':"vehicleMileage"})
        if ( name.text==car_name):
            data=(price.text,use.text)
            cur.execute(query,data)
            cnx.commit()
            i+=1
        if(i>=20):
            break
    if(i>=20):
        break
cnx.close()



