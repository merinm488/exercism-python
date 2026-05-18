def is_pangram(sentence):
    letters = set(sentence.lower())
    filtered = {ch for ch in letters if ch.isalpha()} #filters non alphabets
    return len(filtered) == 26
