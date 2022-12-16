from flask import Flask,render_template,jsonify

app = Flask(__name__)

#  / 경로일 때 hello_world 함수가 실행
# render_template 함수를 통해 외부 html 파일을 실행
@app.route('/')
def hello_world():
    return render_template("hello_world.html")

#  /fc 경로에서 fast_campus 함수가 실행
@app.route('/fc')
def fast_campus():
  res = []
  for i in range(10):
    res.append({
      'title':str(i)+'title'
    })
  return jsonify(res)

  
  

# 파이썬 파일을 직접 실행했다면 app을 실행하라는 뜻
# 해당 파일이 다른 곳에서도 사용되는 경우도 있음.
# __name__ 변수는 해당 파일이 실행되는 형태에 따라 값이 바뀐다.
# 해당 파일을 직접 실행하면 __main__이 나오고
# from import를 통해 파일을 실행하면 해당 파일 명이 나온다 
if __name__ == '__main__':
    app.run()