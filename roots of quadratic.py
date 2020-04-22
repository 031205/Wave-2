import math
a = input('Input the value of a: ')
b = input('Input the value of b: ')
c = input('Input the value of c: ')
a = float(a)
b = float(b)
c = float(c)
if a != 0 :
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0 :
        squareroot = math.sqrt(b ** 2 - 4 * a * c)
        realroot1 = (-b + squareroot) / (2 * a)
        realroot2 = (-b - squareroot) / (2 * a)
        print('Two real roots')
        print('The values of the real roots are',realroot1,'and',realroot2)
    elif discriminant == 0 :
        realroot = -b / (2 * a)
        print('One real root')
        print('The value of the real root is',realroot)
    elif discriminant < 0 :
        print('Does not have any real roots')
else:
    print('Error input on the value of a')







