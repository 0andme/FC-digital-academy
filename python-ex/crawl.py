import requests

from bs4 import BeautifulSoup
# 해당 링크를 수집하기 
res=requests.get('https://www.yes24.com/24/category/bestseller')

# 수집한 파일을 분석하기 
soup=BeautifulSoup(res.text,'html.parser')


for i in range(3):
  # 책 제목 가져오기
  idx=str(i+1)

  sstr='.num'+idx+' > p:nth-child(3) > a:nth-child(1)'
  ts=soup.select_one(sstr)
  # 해당 책의 개별 링크 가져오기
  link=ts.attrs.get('href')
  
  res2=requests.get('https://www.yes24.com'+link)
  soup2=BeautifulSoup(res2.text,'html.parser')
 
  # 판매지수에 해당되는 css가져오기
  sale_point=soup2.select_one('.gd_sellNum')

  # 첫번째 판매지수 삭제
  strIdx=sale_point.text.find('판매')
  point=sale_point.text[strIdx+5:]
  # 두번째 판매지수 삭제
  strIdx=point.find('판매')
  point=point[:strIdx-1]
  
  print(ts.text,point)
  


