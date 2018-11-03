from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store,StoreList
import jwt


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='gebbz'
api=Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

jwt=JWT(app,authenticate,identity) # /auth


api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(StoreList,'/stores')

api.add_resource(UserRegister,'/register')


'''
--127.0.0.1:5000/auth
--POST
--HEADERS -- Content-Type -- application/json
--RAW
--{
    "username":"gebbz",
    "password":"gebbz4ever"
}

----------------------------------------
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDA5OTUxOTcsImlhdCI6MTU0MDk5NDg5NywibmJmIjoxNTQwOTk0ODk3LCJpZGVudGl0eSI6MX0.ArGkXGDFJUd5SPTEgNMvsNMHdEKxhl6m0DZrUd-VibE"
}



-----------------
--http://127.0.0.1:5000/item/shoes
--POST
--HEADERS -- Content-Type -- application/json
--RAW
--{
    "price":15:99
}


--http://127.0.0.1:5000/items

--http://127.0.0.1:5000/item/shoes
--GET
--HEADERS -- Authorization -- jwt eyJ0eXAiOiJKV1QiLCJ........


--http://127.0.0.1:5000/item/shoes
--DELETE




--http://127.0.0.1:5000/item/shoes
--PUT
--HEADERS -- Content-Type -- application/json
--RAW
--{
    "price":100
   
}


'''

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)


