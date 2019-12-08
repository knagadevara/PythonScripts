from flask import Flask , jsonify , request
from flask_restful import Api , Resource

app = Flask(__name__)
api = Api(app)

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



if __name__=="__main__":
    app.run(host='0.0.0.0' , debug=True)