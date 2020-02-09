import math

def q(a, b, c):

    if a==0:

        x1=x2=-(c/b)

    elif b*b-4*a*c < 0:

        x1=x2='wujie'

    else:

        d = math.sqrt(b*b-4*a*c)

        x1 = (-b+d)/(2*a)

        x2 = (-b-d)/(2*a)

	return x1,x2
