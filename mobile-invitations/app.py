import math
import datetime
from flask import Flask,render_template,jsonify,request,redirect
from flask_pymongo import PyMongo

app=Flask(__name__)
# 몽고디비 연결 
app.config['MONGO_URI']='mongodb://localhost:27017/local'
mongo=PyMongo(app)

@app.route('/write',methods=["POST"])
def write():
  # html form 태그에서 data가져오기
  name = request.form.get('name')
  content=request.form.get('content')
  # 데이터 추가
  mongo.db['wedding'].insert_one({'name':name,'content':content})
  # redirect('경로')
  # 해당 경로로 이동
  return redirect('/')

@app.route('/')
def index():
  # 입력된 날짜와 현재 시간과의 차이 변수에 저장
  now =datetime.datetime.now()
  wedding=datetime.datetime(2022,12,19,0,0,0)
  diff=(wedding-now).days 
  
  # db 데이터 가져오기 - limit & skip
  page= int(request.args.get('page',1) )
  limit=3
  skip=(page-1)*limit
  
  guestbooks=mongo.db['wedding'].find().limit(limit).skip(skip)
  
  # count_documents 문서에 대한 개수 찾기
  # 파라미터로 값을 넣지 않아도 되지만, 
  # 모든 문서의 개수를 알고자 한다면 빈 값{}을 넣어줘야함
  count=mongo.db['wedding'].count_documents({})
  max_page=math.ceil(count/limit)
  pages=range(1,max_page+1)

  return render_template('index.html',diff=diff,guestbooks=guestbooks,pages=pages)

if __name__ == '__main__':
  app.run()