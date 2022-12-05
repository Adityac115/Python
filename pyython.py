hello = 'aditya'
world = hello
hello = 'no'
print(hello ,world )

name = input('name: ')
age = input('age : ')
print("hello" ,name ,"you are ", age, " years old");

x= 10
y =3
result = (x %y) *3
print(result)
num = input("Number :")
print(int(num) - 5) 


hello = "adittya"
print(hello.count('d'))


a="Aditya "
b='kushwaha '
print(a + b)


x=input('Name: ')
if x == 'aditya':
    print('You are great')
else:
    print("you are not aditya")
print('this alsways run')
 
 
x=["hello", 4 ,5, 'adi']
print(x.pop(0))

x[0]="aditya"
print(x)


for i in range(-10,-1,-2):
    print('hello')



x=[3,4,5,6,7,8]

for i,elements in enumerate(x):
    print(i,elements)



x=[0,1,2,3,4,5,6,7,8]
y=['hi','hello','goodbye','cya','sure']


sliced=x[0:4]
s2=x[:4]
s3=x[2:]
s4=x[::2]
s5=x[2::]
s6=x[::-1]
print(sliced)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)


x=set()
# or
s={2,3}
s2={4,5}
print(type(s))
s.add(4)
s.remove(2)

print(4 in s)
print(s.union(s2))
   

x={'key':4}

for key, values in x.items():
    print(key,values)
    
    
#################################

h=[h%5 for h in range(10)]
print(h) 



u=[[1 for u in range(10)] for u in range(5)]
print(u)


u = [i for i in range(50) if i%6 ==0 ]
print(u)


def func(x,y):
    print('run',x,y)
    return x*y , x/y
 
r1,r2=func(5,6)   
print(r1,r2)


def func(*x,**y):
    print(*x,**y)
    
func(1,2,3,4,5,'one'= 0,'two'=1)

x=[1,2,3,4,5,6,7,8,9,10]

mp=filter(lambda i:  i%2==0, x)
print(list(mp))


x=f'hello my age is {6+9} '
print(x)


print(f'hello my age is {10+10}')
