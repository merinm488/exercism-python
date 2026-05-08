def isValid(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return  a>0 and b>0 and c>0 and a+b>=c and a+c>=b and b+c>=a
        

def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return isValid(sides) and a==b and b==c and a==c
       


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return isValid(sides) and (a==b or b==c or a==c)


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return isValid(sides) and a!=b and b!=c and a!=c
