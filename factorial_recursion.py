def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)

num=int(input("enter the number: "))
print("the factorial of the number is: ",fact(num))