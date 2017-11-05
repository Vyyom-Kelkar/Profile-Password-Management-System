from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///test.sqlite')
app = Flask(__name__)
api = Api(app)

class Admin_Setting(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from admin_setting") # This line performs query and returns json result
        return {'admin_setting': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

class Users(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from users;")
        result = {'users': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Old_Password(Resource):
    def get(self, user_Id):
        conn = db_connect.connect()
        query = conn.execute("select * from old_password where userId = %d"  %int(user_Id))
        result = {'old_password': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        

api.add_resource(Admin_Setting, '/admin_setting') # Route_1
api.add_resource(Users, '/users') # Route_2
api.add_resource(Old_Password, '/old_password/<user_Id>') # Route_3


if __name__ == '__main__':
     app.run(port='5002')