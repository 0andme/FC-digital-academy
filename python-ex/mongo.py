from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db=client.local
name='fastcampus'
collection=db[name]

# 컬렉션의 데이터 전부 가져오기
# rows=collection.find()
# for row in rows: print(row)

# 컬렉션의 데이터 한개만 가져오기
# row=collection.find_one()
# print(row)

# 컬렉션에 데이터 넣기 
# collection.insert_one({
#   'title':'패스트 캠퍼스',
#   'content':'2주차 서버만들기 몽고티비 실습'
# })


# 컬렉션에서 특정 키와 값을 갖는 데이터 찾기
row=collection.find_one({'title':'패스트 캠퍼스?'})
print('res=',row)
