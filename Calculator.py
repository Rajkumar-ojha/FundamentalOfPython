# Python Calculator
op=input("enter an operator (+ - * /):")
num1=float(input("enter the 1st number:"))
num2=float(input("enter the 2nd number:"))

if op == "+":
    result = num1 + num2
    print(round(result))
elif op == "-":
    result = num1 - num2
    print(round(result,3))
elif op =="*":
    result = num1 * num2
    print(round(result,3))
elif op == "/":
    result = num1 / num2
    print(round(result,3))
else:
    print(f"{op} is not valid operator")