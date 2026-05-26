def is_valid(isbn):
    isbn = isbn.replace('-','')

    if len(isbn) != 10:
        return False
    
    if any(char.isalpha() for char in isbn[:9]):
        return False
    factor = 10
    sum = 0
    if isbn[-1].isdigit() or isbn[-1] == 'X':
        for i in isbn:
            if i == 'X':
                i = 10
            sum = sum + (int(i) * factor)
            factor-=1
        return sum % 11 == 0
    else: return False
              
