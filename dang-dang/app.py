from flask import Flask,render_template,jsonify,request,redirect
from flask_pymongo import PyMongo

# flask연결
app=Flask(__name__)
# mongo db 연결
app.config['MONGO_URI']='mongodb://localhost:27017/local'
mongo=PyMongo(app)

# index
@app.route('/')
def index():
  product_db=mongo.db.product
  products=product_db.find()
  return render_template('list.html',products=products)

# detail
@app.route('/detail')
def detail():
  product_db=mongo.db.product
  product=product_db.find_one({'title':request.args.get('title')})

  return jsonify({
    'title':product.get('title'),
    'content':product.get('content')
  })


# writepage
@app.route('/writepage')
def writepage():
  return render_template('write.html')

# write
@app.route('/write',methods=['POST'])
def write():
  product_db=mongo.db.product
  product_db.insert_one({
    'title':request.form.get('title'),
    'content':request.form.get('content'),
    'price':request.form.get('price'),
    'location':request.form.get('location')
  })
  
  return redirect('/')


# 실행
if __name__ == '__main__':
  app.run()