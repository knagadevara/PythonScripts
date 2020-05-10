# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 03:09:25 2019

@author: saikarthik.n
"""

from flask import Flask , jsonify , request
from flask_restful import Api , Resource
from pymongo import MongoClient
import bcrypt
import requests
import subprocess
import simplejson as json
import os

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
mydb = client["WhoAmI"]
mycoll = mydb["CanYouFindMe"]

tocken_count = 0

## Pre Registrattion Checks
def RegisterCheckData(postedData):
    if "user_name" not in postedData or "first_name" not in postedData or "last_name" not in postedData or "password" not in postedData:
        StatusCode = 301
        Message = "Missing Mandatory Parameters"
        return StatusCode, Message
    elif len(postedData["password"]) < 6 or len(postedData["password"]) >= 13 or len(postedData["user_name"]) < 5 or len(postedData["user_name"]) >= 13 :
        StatusCode = 302
        Message = "Please give a value which is more than 6 characters to 12 characters"
        return StatusCode, Message
    else:
        StatusCode = 200
        Message = "Successfully created the User"
        return StatusCode, Message

def checkUserExists(user_name):
    try:
        mycoll.find_one({ "user_name"  : user_name })["user_name"]
    except Exception:
        user = 0
    else:
        user = 1
    if user > 0:
        StatusCode = 303
        Message = "Username already exist, please choose another"
        return StatusCode , Message


def checkCred(user_name , password):
    try:
        password = password.encode("utf8")
        pass_user1 = mycoll.find_one({ "user_name"  : user_name })["password"]
        pass_user2 = mycoll.find_one({ "user_name"  : user_name })["user_name"]
    except Exception:
        CallFalse = 1
    else:
        CallFalse = 0
    if CallFalse == 1:
        StatusCode = 310
        Message = "Username or Password not found"
        return StatusCode , Message
    else:
        if bcrypt.checkpw(password , pass_user1) and user_name == pass_user2:
            StatusCode = 220
            Message = "Authentication Success"
            return StatusCode , Message
        else:
            StatusCode = 305
            Message = "Authentication Error, Invalid Username or Password"
            return StatusCode , Message

## Post registeration
def ClassifyMeCheckData(postedData):
    if "user_name" not in postedData  or "password" not in postedData or "url" not in postedData:
        StatusCode = 301
        Message = "Missing Mandatory Parameters"
        return StatusCode, Message
    else:
        StatusCode = 200
        Message = "Successfully created the User"
        return StatusCode, Message

def CheckTokenExists(user_name):
    try:
        global tocken_count
        tocken_count = mycoll.find_one({ "user_name"  : user_name})["token"]
    except Exception:
        CallFalse = 1
    else:
        CallFalse = 0
    if CallFalse == 1:
        StatusCode = 310
        Message = "Username not found"
        return StatusCode , Message
    else:
        if tocken_count <= 0 :
            StatusCode = 306
            Message = "Unable to Store, no Tokens"
            return StatusCode, Message
        else:
            StatusCode = 220
            Message = "Token Exists"
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

            ## Inserting the values in DB
            UStatusCode = checkUserExists(user_name)
            if UStatusCode == 303:
                result = {"Status": UStatusCode,
                          "Message": "Username already exist, please choose another"}
                return jsonify(result)

            hpass = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())

            insert_result = mycoll.insert_one(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "user_name" : user_name,
                    "password" :  hpass,
                    "token" : 10
                }
            )
            if insert_result.acknowledged:
                SendResponse = {
                "Message": Message,
                "Status Code": StatusCode,
                "Transaction" : "Registered for the API"
                    }
                return jsonify(SendResponse)

            else:
                SendResponse = {
                "Message": Message,
                "Status Code": StatusCode,
                "Transaction" : "Unable to register!! Error in Transaction"
                    }
                return jsonify(SendResponse)

class ClassifyMe(Resource):
    def post(self):
        getPostedData = request.get_json()
        StatusCode, Message = ClassifyMeCheckData(getPostedData)
        SendResponse = {
                "Message": Message,
                "Status Code": StatusCode
            }

        if StatusCode != 200:
            return jsonify(SendResponse)
        else:
            user_name = str(getPostedData["user_name"]).strip().lower()
            password = str(getPostedData["password"]).strip()
            url = str(getPostedData["url"]).strip()
            
            StatusCode , Message = checkCred(user_name , password)
            TokenCode , TokenMsg = CheckTokenExists(user_name)
            
            if TokenCode != 220:
                SendResponse = {
                "Message" : TokenMsg,
                "Status Code" : TokenCode
                }
                return jsonify(SendResponse)

            if StatusCode != 220:
                SendResponse = {
                "Message" : Message,
                "Status Code" : StatusCode
                }
                return jsonify(SendResponse)
            else:
                ur = requests.get(url)
                retJSON = {}
                ## Opening a flie in binary write format
                os.chdir("/usr/src/app/")
                with open("temp.jpg" , "wb") as f:
                    f.write(ur.content)
                    proc = subprocess.Popen(r'/usr/src/app/python -m /usr/src/app/classify_image.py --model_dir=.  --image_file=./temp.jpg')
                    proc.communicate()[0]
                    proc.wait()
                    with open("text.txt") as g:#/usr/src/app/
                        retJSON = json.load(g)
                mycoll.update_one(
                            { "user_name" : user_name } ,
                            {
                                "$set":
                                    {
                                        "token" : tocken_count - 1
                                        }})

                return jsonify(retJSON)

def checkPara(postedData):
    if "user_name" not in postedData  or "refil_count" not in postedData or "admin_user_name" not in postedData:
        StatusCode = 301
        Message = "Missing Mandatory Parameters"
        return StatusCode, Message
    try:
        pass_user2 = mycoll.find_one({ "user_name"  : postedData["user_name"] })["user_name"]
    except Exception:
        CallFalse = 1
    else:
        CallFalse = 0
    if CallFalse == 1:
        StatusCode = 310
        return StatusCode
    else:
        if postedData["user_name"] == pass_user2:
            StatusCode = 220
            return StatusCode
        else:
            StatusCode = 305
            return StatusCode

class ReFillCredits(Resource):
    def post(self):
        getPostedData = request.get_json()
        StatusCode = checkPara(getPostedData)
        if StatusCode != 220:
            SendResponse = {
                "Message" : "Authentication Error, Invalid Username or Password",
                "Status Code" : StatusCode
                }
            return jsonify(SendResponse)

        user_name = str(getPostedData["user_name"]).strip().lower()
        admin_user_name = str(getPostedData["admin_user_name"]).strip().lower()
        refil_count = int(getPostedData["refil_count"])

        if admin_user_name == "Karthik@123":
            refilled = mycoll.update_one(
                { "user_name" : user_name } ,
                {
                    "$set":
                    {
                    "token" : tocken_count + refil_count
                    }})

            if refilled.acknowledged:
                UserResponse = {
                "Message" : "Recharge Successfull",
                "Status Code" : 201
                }
                return jsonify(UserResponse)
            else:
                UserResponse = {
                "Message" : "Recharge Failed",
                "Status Code" : 501
                }
                return jsonify(UserResponse)

# =============================================================================
## API Router
api.add_resource(Register , "/register")
api.add_resource(ClassifyMe , "/whoami")
api.add_resource(ReFillCredits , "/recharge")
# =============================================================================

if __name__=="__main__":
    app.run(host="0.0.0.0" , debug=True)