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
  # 입력된 날짜와 현재 시간과의 
  now =datetime.datetime.now()
  wedding=datetime.datetime(2022,12,19,0,0,0)
  diff=(wedding-now).days 
  
  # db 데이터 가져오기
  guestbooks=mongo.db['wedding'].find()
  
  return render_template('index.html',diff=diff,guestbooks=guestbooks)

if __name__ == '__main__':
  app.run()