# Mini calculator using python 

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
operation=input("enter the operation you want to perform (+,-,*,%,**):")
if operation=="+":
    print("the sum of two number is:",a+b)
elif operation=="-":
    print("the difference of two number is:",a-b)
if operation=="*":
    print("the product of two number is:",a*b)
elif operation=="%":
    if b==0:
        print("division by zero is not allowed")
    else:
        print("the remainder of two number is:",a%b)
elif operation=="**":
    print("the power of two number is:",a**b)
else:
    print("Invalid operation")
print("Thank you for using this calculator")