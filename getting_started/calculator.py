# Input two numbers
# Find sum, difference, product and quotient of numbers

n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))

total = n1 + n2
diff = n1 - n2
prod = n1 * n2
quotient = n1 / n2
int_division = n1 // n2
remainder = n1 % n2

print('Sum of %d and %d is %d'%(n1, n2, total))
print('Difference between %d and %d is %d'%(n1, n2, diff))
print('Product of %d and %d is %d'%(n1, n2, prod))
print('Quotient of %d and %d is %.2f'%(n1, n2, quotient))
print('Result of integer divion %d by %d is %d'%(n1, n2, int_division))
print('Remainder while dividing %d by %d is %d'%(n1, n2, remainder))