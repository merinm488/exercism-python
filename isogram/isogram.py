def is_isogram(string):
    string = ''.join([char for char in string if char.isalpha()]) #keep only alphbets
    letters = list(string.lower())
    unique_letters = set(letters)
    return len(letters) == len(unique_letters)
