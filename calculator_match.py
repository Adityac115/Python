a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
operator=input("Enter operation: ")
match operator:
    case '+':
        print(f"operation you used: + ,and the  result is {a+b}")
    case '-':
        print(f"operation you used: - ,and the result is {a-b}")
    case '*':
        print(f"operation you used: * ,and the result is {a*b}")
    case '%':
        print(f"operation you used: % ,and the result is {a%b}")
    case '/':
        print(f"operation you used: / ,and the result is {a/b}")