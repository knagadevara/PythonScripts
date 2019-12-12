from pymongo import MongoClient

## Establishing the database connection
DBclient = MongoClient("mongodb://192.168.56.108:27017")
## Creating a database
db_talk = DBclient.nagadevara
## Creating a Collection
i_am_user = db_talk["Users"]

dict1 = {
"user_name" : "knagdsd3",
"password" : "Su222n23",
"First_Name" : "Sai Karthik" ,
"Last_Name" : "Nagadevara"
}

dict2 = {
"user_name" : "sazzi",
"password" : "12gr",
"First_Name" : "Shashi" ,
"Last_Name" : "Gorrela"
}

#i_am_user.insert(dict1 , dict2)
#def verifyPw(user_name):
#    PassUser = i_am_user.find_one({"User_Name" : user_name} , { "Password" : 1 } )
#    PassUser = i_am_user.find_one({"User_Name" : user_name} , { "Password" : 1 } )[0]['Password']
#   PassUser = i_am_user.find_one({"User_Name" : user_name})
#   pass_user = pu['password']
#   pu = [x[0] for x in PassUser.values()]
#   return pu

get_Pass = i_am_user.find({ "user_name"  : 'knagdsd3'})[0]['password']

print(get_Pass)

# for s in get_Pass:
#     print(s)