# Find the roots of quadratic equation

a = int(input('Please enter the value of a: '))
b = int(input('Please enter the value of b: '))
c = int(input('Please enter the value of c: '))

r1 = (-1*b + (b**2-4*a*c)**0.5)/(2*a)
r2 = (-1*b - (b**2-4*a*c)**0.5)/(2*a)

if r1 == r2:
    print('Root for the quadratic equation is ', str(r1))
else:
    print('Root for the quadratic equation are ', str(r1), 'and', str(r2))
