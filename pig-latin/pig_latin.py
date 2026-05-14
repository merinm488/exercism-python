def translate(text):
    latin = []
    
    words = text.split()
    for word in words: #loop through through each word
        if word[0] in 'aeiou' or word[0:2] == 'xr' or word[0:2] == 'yt': #testing rule 1
            latin.append(word + 'ay')
        else: 
            consonent = ''
            char = 0
            while char < len(word) and word[char] not in 'aeiou': 
                if char+1 < len(word) and word[char] == 'q' and word[char+1] == 'u':  #rule 3
                        consonent += 'qu'
                        char+=2 #helps in sliceing from corect character
                        break
                elif char+1 < len(word) and word[char+1] == 'y': #rule 4
                    consonent+=word[char]
                    char+=1
                    break
                else: 
                    consonent+=word[char] #rule 2
                    char+=1
            latin.append(word[char:] + consonent + 'ay') #appending is same for all rules

    return " ".join(latin)
