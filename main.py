from multiplication import multiplication

sign = input("enter the arithmetic operator: ")
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if sign == '+':
   pass 
elif sign == '-':
    pass
elif sign == '*':
   print(multiplication(num1,num2))
elif sign == '/':
    pass
else:
    print("arithmatic operator not found")