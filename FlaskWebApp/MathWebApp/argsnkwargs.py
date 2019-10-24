from datetime import datetime

# def mytestfun(*,d):
#     return d
# def mytestfun2(a, *, b=1):
#     return 'a:{0} , b:{1}'.format(a , b)
# def mytestfun3(c=1 , * , b):
#     return None
# ## def testfunc4(a , b=1 , c) Throws error non-defaulr argument follows default argument
# def testfunc4(a , c, b=1):
#     return '{}{}{}'.format(a,b,c)

# ## testfunc4(b=2,'1',c=3) ## this throws out an error, keyword args follow positional args.
# testfunc4(1,21)
# ## mytestfun(1) ##ypeError: mytestfun() takes 0 positional arguments but 1 was given
# mytestfun(d=1)
# ## mytestfun2(1,2,3) ## TypeError: mytestfun2() takes 1 positional argument but 3 were given
# mytestfun2(1,b=3)
# mytestfun3(b=1)

# ## Notes: We have to declare Arguments/Parameters in the below order, anything that appears after the * is a keyword argument
# def funcProper(Positional_Parameters = 1, * , Keyword_Parameters = 1):
#     return
# ## Positional parameter has a default value of 1 same goes with keyword, it can be called in below ways.
# funcProper()
# funcProper(1)
# funcProper(1,Keyword_Parameters=3)
# funcProper(Keyword_Parameters=3)

# def logger_func(message, *, dt=None):
#     dt = dt or datetime.utcnow()
#     print('message: {0} dateLogger: {1}'.format(message , dt))

# logger_func("Hello Father!")
# logger_func('Hello Son!' , dt='Ancient')

my_list = (1 , 2 , 3 , 4)

def func_nu(d=my_list):
    print(d)

func_nu(['a' , 'b'])
print(my_list)