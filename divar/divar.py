import requests
import re
from bs4 import BeautifulSoup
r=requests.get('https://divar.ir/s/tehran')
soup= BeautifulSoup(r.text,'html.parser')
values=soup.find_all('div',class_="post-card-item kt-col-6 kt-col-xxl-4")

for value in values:
    if re.search(r'.*توافقی.*',value.text)!=None:
        t=re.sub(r'.*(ی‌ق‌ف‌ا‌و‌ت).*','  ‌ی‌ق‌ف‌ا‌و‌ت  ',value.text).strip()
        print(t)