#!/usr/bin/python3.6

beat_list = (1 , 2 , 3)
el = []
def myfunc(num):
    x = 0
    while x < num:
        i = 0
        while i < len(beat_list):
            el.append(beat_list[i])
            yield(beat_list[i])
            i += 1
        x += 1     

mynum =  myfunc(10)
for s in mynum:
   print(s)