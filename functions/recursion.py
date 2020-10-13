# Find factorial of a number
def factorial(n):
    if n==1 :
        return 1 # Exit condition
    else:
        return n * factorial(n-1) # Base condition

print(factorial(5))