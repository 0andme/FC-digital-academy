import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
# 웹크롤링
# res=requests.get('https://www.yes24.com/24/category/bestseller')
# soup=BeautifulSoup(res.text,'html.parser')

# mongodb설정
client = MongoClient('mongodb://localhost:27017/')
db=client.local
collect_name='yes24'
collection=db[collect_name]



# 웹 크롤링 코드 및 컬렉션에 데이터 추가 
# for i in range(20):
  
#   idx=str(i+1)
#   if idx=='19':
#     idx='19_line'
#   elif idx=='20':
#     idx='20_line'

#   sstr='.num'+idx+' > p:nth-child(3) > a:nth-child(1)'
#   ts=soup.select_one(sstr)

#   collection.insert_one({
#     "title":ts.text
#   })
 

# 컬렉션에 들어간 데이터 확인 
rows=collection.find()

for row in rows:
  print(row)
