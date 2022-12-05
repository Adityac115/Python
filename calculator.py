a= int(input("enter 1st NUmber: "))         
b= int(input("enter 2nd Number: "))
op= input("which operation you want to perform: ")

if(op=='+'):
    print('result is: ',a+b )
elif op=='-':
    print('result is: ',a-b)
elif op=='*':
    print('result is: ',a*b)
elif op=='%':
    print('result is: ',a%b)
elif op=='/':
    print('result is: ',a/b)
    
else:
    print('unknown operator')