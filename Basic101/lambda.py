
# users =  [ { 'Name' : 'Karthik' , 'Age' : 27 , 'comments' : [] } , {'Name' : 'Kiran' , 'Age' : 27 , 'comments' : ['Its Good!!'] } ]

# def my_users():
#     for x in users:
#         for a , b in x.items():
#             if a == 'comments' and len(b) != 0 :
#                 print(b)
            
        
# usr_c = filter(lambda a: len(a['comments']) == 0, users)

# print(list(usr_c))

# names = [ 'agastya' , 'muni' , 'arjun' , 'bheema' , 'abhimanyu' ]

# for n in names:
#     print(min()

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]


myname = lambda: echo('Karthik')

myname.__call__
# for s in songs:
#     print(s['playcount'])

print(min(songs, key=lambda s: s['playcount'])['title'])