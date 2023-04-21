print('hi')

if 5 > 3:
        print('5 is > 3')
        print('test')

#comment 
print('a')

''' Multiline Comment 
Test
Test
Test
'''
print('b')

#variables
x=5
print(x)
x="x"
print(x)    
x=int(3)
print(x)
y=str(3)
print(y)
x = float(x)
print (x)
print(type(x))
X='Caps X'
print(X)

x,y='a', 5
print (x), print(y)
fruits = ['orange', 'banana', 'lemon']
print (fruits)
print(x,y,fruits+fruits)

#function
def myfunction():
 global z 
 z = 'global'
 print('function ' + X + z)
myfunction()
print(z)

for x in 'banana':
    print('b' in x)
    
try:
    err = 10/0
except ZeroDivisionError as ex:
 print(str.format("Exception: {}" , ex))

 #err = 10/0


with open('questions1.txt', 'r') as f:
    print(f.read())

with open('questions1.txt','w') as f:
    f.write('hello')

with open('questions1.txt', 'r') as f:
    print(f.read())

a,b = 5, 6
if a>b:
    print(str.format("{} is greater than {}", a, b))
else:
    print(str.format("{} is lesser than {}", a, b))

