from flask import Flask , jsonify , request
from flask_restful import Api , Resource
from pymongo import MongoClient
#from bcrypt import hashpw, gensalt

app = Flask(__name__)
api = Api(app)

## Establishing the database connection
DBclient = MongoClient("mongodb://db:27017")
## Creating a database
db_talk = DBclient.UserTalks
## Creating a Collection
i_am_user = db_talk["API_users"]
tocken_count = 0
def RegisterCheckData(postedData):
    uname_count = i_am_user.find({ "user_name"  : postedData['user_name'] })[0]['user_name']
    if 'user_name' not in postedData or 'first_name' not in postedData or 'last_name' not in postedData or 'password' not in postedData:
        StatusCode = 301
        Message = "Missing Mandatory Parameters"
        return StatusCode, Message
    elif len(postedData['password']) < 6 or len(postedData['password']) >= 13 or len(postedData['user_name']) < 5 or len(postedData['user_name']) >= 13 :
        StatusCode = 302
        Message = "Please give a value which is more than 6 characters to 12 characters"
        return StatusCode, Message
    elif uname_count == postedData['user_name']:
        StatusCode = 303
        Message = "Username already exist, please choose another"
        return StatusCode, Message
    else:
        StatusCode = 200
        Message = "Successfully created the User"
        return StatusCode, Message
def ICommentCheckData(postedData):
    pass_user = i_am_user.find({ "user_name"  : postedData['user_name'] })[0]['password']
    global tocken_count
    tocken_count = i_am_user.find({ "user_name"  : postedData['user_name'] })[0]['token']
    if 'user_name' not in postedData or 'password' not in postedData or 'sentence' not in postedData:
        StatusCode = 304
        Message = "Missing Mandatory Parameters"
        return StatusCode, Message
    elif postedData['password'] != pass_user:
        StatusCode = 305
        Message = "Authentication Error"
        return StatusCode, Message
    elif tocken_count <= 0 :
        StatusCode = 306
        Message = "Unable to Store, no Tokens"
        return StatusCode, Message
    else:
        StatusCode = 200
        Message = "Comments stored Successfully"
        return StatusCode, Message

class Register(Resource):
    def post(self):
        getPostedData = request.get_json()
        StatusCode, Message = RegisterCheckData(getPostedData)
        SendResponse = {
                "Message": Message,
                "Status Code": StatusCode
            }

        if StatusCode != 200:
            return jsonify(SendResponse)
        else:
            user_name = str(getPostedData["user_name"]).strip().lower()
            password = str(getPostedData["password"]).strip()
            first_name = str(getPostedData["first_name"]).strip().lower()
            last_name = str(getPostedData["last_name"]).strip().lower()
            #hpass = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
            ## Inserting the values in DB
            i_am_user.insert_one(
                {
                    "first_name": first_name,
                    "last_ name": last_name,
                    "user_name" : user_name,
                    "password" : password,
                    "sentence" : "",
                    "token" : 6
                }
            )
            return jsonify(SendResponse)

class iComment(Resource):
    def post(self):
        getPostedData = request.get_json()
        StatusCode, Message = ICommentCheckData(getPostedData)
        SendResponse = {
                "Message": Message,
                "Status Code": StatusCode
                        }

        if StatusCode != 200:
            return jsonify(SendResponse)
        else:
            user_name = str(getPostedData["user_name"]).strip().lower()
            password = str(getPostedData["password"]).strip()
            comment = str(getPostedData["sentence"]).strip()
            i_am_user.update_one(
            { "user_name" : user_name } ,
            {
                "$set":
                {
                "sentence" : comment,
                "token" : tocken_count - 1
                }})
            return jsonify(SendResponse)

api.add_resource(Register , "/register")
api.add_resource(iComment , "/comment")

if __name__=="__main__":
    app.run(host='0.0.0.0' , debug=True)