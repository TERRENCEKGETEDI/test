import divide


from add import add 
sign = input("enter the arithmetic operator: ")
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if sign == '+':
    print(add(num1,num2))
elif sign == '-':
    pass
elif sign == '*':
    pass
elif sign == '/':
    quotient=divide.divide(num1,num2)
    print(f'{num1}/{num2}={quotient}')
else:
    print("arithmatic operator not found")