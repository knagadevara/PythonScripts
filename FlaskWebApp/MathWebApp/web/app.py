from flask import Flask , jsonify , request
from flask_restful import Api , Resource
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

## Establishing the database connection
DBclient = MongoClient("mongodb://db:27017")
## Creating a database
db_house = DBclient.HouseDB
## Creating a Collection
house_room = db_house["Room"]
## Creatig a Document inside Collection
RoomOcc = house_room.insert(
   {    
       "no_of_occupants" : 0
   } 
)


class No_Mem(Resource):
    def get(self):
        ext_mem = house_room.find( {} )[0]["no_of_occupants"]
        cur_mem = ext_mem + 1
        house_room.update( {} , {"$set": {"no_of_occupants": cur_mem } } )
        return "This Page Presently has  {0} Visitors".format(cur_mem)


def checkData(postedData , FuncName):
    if FuncName == 'add' or FuncName == 'sub' or FuncName == 'mul':
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        else:
            return 200
    elif FuncName == 'div':
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        elif postedData['x'] == 0 or postedData['y'] == 0:
            return 302
        else:
            return 200

class Add(Resource):

    def post(self):
        jsnData = request.get_json()
        status_code = checkData(jsnData , "add")
        if(status_code!=200):
            restMap = {
            "Message" : "Missing parameter",
            "Status Code" : status_code
            }
            return jsonify(restMap)
        else:
            x = jsnData['x']
            y = jsnData['y']
            x = int(x)
            y = int(y)
            ret = x + y
            restMap = {
                'message' : ret ,
                'Status Code' : status_code
                }
            return jsonify(restMap)


class Sub(Resource):

    def post(self):
        jsnData = request.get_json()
        status_code = checkData(jsnData , "sub")
        if(status_code!=200):
            restMap = {
            "Message" : "Missing parameter",
            "Status Code" : status_code
            }
            return jsonify(restMap)
        else:
            x = jsnData['x']
            y = jsnData['y']
            x = int(x)
            y = int(y)
            ret = x - y
            restMap = {
                'message' : ret ,
                'Status Code' : status_code
                }
            return jsonify(restMap)

class Div(Resource):

    def post(self):
        jsnData = request.get_json()
        status_code = checkData(jsnData , "div")
        if(status_code!=200):
            restMap = {
            "Message" : "Missing parameter or Zero Division Error",
            "Status Code" : status_code
            }
            return jsonify(restMap)
        else:
            x = jsnData['x']
            y = jsnData['y']
            x = int(x)
            y = int(y)
            ret = x / y
            restMap = {
                'message' : ret ,
                'Status Code' : status_code
                }
            return jsonify(restMap)


api.add_resource(Add , "/add")
api.add_resource(Sub , "/sub")
api.add_resource(Div , "/div")
api.add_resource(No_Mem , "/mem")


if __name__=="__main__":
    app.run(host='0.0.0.0' , debug=True)