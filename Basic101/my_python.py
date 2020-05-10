#!/usr/bin/python3.6

# print("Hello again!!, Karthik")

# my_nam = "Karthik"
# my_age = 28
# str(28)
# print(f"Hi i am {my_nam} , and i am {my_age}")
# print("Hello i am {1} and i am {0} years old".format(my_nam,my_age))

# print(type(my_age) ,type(my_nam))

def intervine(str1 , str2):
   zstr =  list(zip(str1 , str2))
   mystr = ''.join(''.join(x) for x in zstr)
   return mystr

print(intervine('kaa', 'idk'))
