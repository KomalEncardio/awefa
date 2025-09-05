def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def prod(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return "Cannot divide it by zero"
    else:
        return float(a/b)
    
def exponent(a,b):
    if b == 0:
        return 1
    else:
        return exponent(a,b-1)
    
import math


def log(a,b):
    return math.log(a,b)

def factorial(a):
    return math.factorial(a)

