import math
def score(x, y):
    dist = math.sqrt(x*x + y*y)
    if dist<=1:
        point = 10
    elif dist<=5:
        point = 5
    elif dist<=10:
        point = 1
    else: point = 0

    return point
