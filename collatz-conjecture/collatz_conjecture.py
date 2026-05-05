def steps(number, count=0):
    if number<=0:
        raise ValueError("Only positive integers are allowed")
    elif number == 1: 
        return count
    else:
        if number%2==0: 
            number//=2 
            count+=1
        else:
            number = number*3+1
            count+=1
        return steps(number, count)
