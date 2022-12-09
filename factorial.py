def fact(num):
    product =1;
    for i in range(1,num+1):
        product *= i
    return product

num = int(input("Enter the number: "))
print("the factorial of the number is: ",fact(num))