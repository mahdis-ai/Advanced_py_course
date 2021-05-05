import requests
from bs4 import BeautifulSoup
import os
r=requests.get('https://resume.io/app/resumes/13302485/edit')
soup=BeautifulSoup(r.text,'html.parser')
resume=soup.find('canvas',class_="sc-jUiVId sc-kecUPG diSTrk")
path=os.getcwd()
path=os.path.join(path,'res.pdf')
print(resume)