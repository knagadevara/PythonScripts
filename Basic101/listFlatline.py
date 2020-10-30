### ---- ### Flatten a list ### ---- ###
mylist =  [ 11 , 12 , 13 , [ 1 , 1 , 2 , [ 3 , 4, [1, 5, 6 , [7]]], 8, [9, 10] , 9 ] ]
newList = []

# exampDict = dict()
def uniqMe(lst):
    uniq = [] 
    duplicate = []
    exampDict = dict()
    for i in lst:
        if lst.count(i) > 1:
            exampDict[i] = lst.count(i)
            duplicate.append(i)           
        else:
            exampDict[i] = 1
            uniq.append(i)
    return print("Repeted: ", exampDict , "\nUniq Items: ", uniq , "\nDuplicate Items: ", duplicate )

def listOut(lstr):  
    for items in lstr:
        if type(items) == list:
            listOut(items)
        else:
            newList.append(items)  

listOut(mylist)
uniqMe(newList)