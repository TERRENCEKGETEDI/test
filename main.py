sign = input("enter the arithmetic operator: ")
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if sign == '+':
    pass
elif sign == '-':
    def subtraction(a, b):
        """
        Subtracts two numbers.

        Parameters:
        a (float): The first number.
        b (float): The second number.

        Returns:
        float: The result of subtracting b from a.
        """
        return a - b
elif sign == '*':
    pass
elif sign == '/':
    pass
else:
    print("arithmatic operator not found")