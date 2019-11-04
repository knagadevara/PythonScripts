a = [1, 2, 3]
b = [1, 2, 3]

print('a: {0}, b: {1}'.format(hex(id(a[0])) , hex(id(b[0]))))

print(a[0] is b[0])

print(a is None)

#always use sys.intern('') to compare two strings, as it creats the same objects
# Hyper variable definations.
## avg = num and totla/num
## returnt the first character of the string if exists else return empty string
## Programming in general
#count = (input("Enter Somethings: ") and int(count)) or ''
#count = input("Enter Somethings: ") and count and int(count) or 1
## cannot do type casting in the same time of conditional initialization as the memory address still dosent exist.
count = input("Enter No of Subjects: ")
total = input("Enter The total sum: ")
count = count and int(count) or ''
total = count and int(total) or ''
avg = count and total/count or 'N/A'
print(avg)

name = input()
if len(name) > 0 and name is not '':
    print(name[0])

if name:
    print(name[0])
else:
    print('')
i = (name and name[0]) or 'NO'
print(i)

# variable unpacking.
a = 0,9,8,7
b = 1,2,3,4
x,*y,z = 'a','b','c','d','e'
c = *a,*b