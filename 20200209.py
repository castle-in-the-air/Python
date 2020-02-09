import math

def quadratic(a, b, c):

    if a==0:

        print('分母不能为零')

    elif b*b-4*a*c < 0:

        print('无解')

    else:

        d = math.sqrt(b*b-4*a*c)

        x1 = (-b+d)/(2*a)

        x2 = (-b-d)/(2*a)

        return x1,x2