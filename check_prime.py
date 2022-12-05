num=int(input('Enter the number you want to check whether its prime or not: '))
x=[x for x in range(2,num) if num%x==0] 
if num==0 or num==1:    print(num,"is not a prime number")
elif len(x)==0:   print(num,"is a prime number!!")
else:    print(num,"is not a prime number!!")