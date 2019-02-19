"""
This function takes in a number and returns the value at that index in the fibonacci sequence
"""
def fibonacci(n):
    num1 = 0
    num2 = 1
    count = 0
    if n == 0: return 0
    elif n == 1: return 1
    else:
        while count < n:
            temp = num1 + num2
            num1 = num2
            num2 = temp
            count += 1
        return num2
"""
This function takes in a number and returns the value at that index in the lucas sequence
"""
def lucas (n):
    num1 = 2
    num2 = 1
    count = 0
    if n == 0: return 2
    elif n == 1: return 1
    else:
        while count < n:
            temp = num1 + num2
            num1 = num2
            num2 = temp
            count += 1
        return num2
"""
This function takes in one required argument and 2 optional arguments. If only one argument is passed in then the function defaults to using the fibonacci sequence.
"""
def sum_series(n, num1=0, num2=1):    
    count = 0
    if n == 0: return 0
    elif n == 1: return 1
    else:
        while count < n:
            temp = num1 + num2
            num1 = num2
            num2 = temp
            count += 1
        return num2