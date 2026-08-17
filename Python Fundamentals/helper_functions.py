def delete_letter(word):
    if len(word)==1:
        return word
    
    if word[0]== word[1]:
        return delete_letter(word[1:])
    
    return word[0] + delete_letter(word[1:])


def factorial(n):
    if n==0 or n==1:
        return 1
    
    else:
        return n * factorial(n-1)
    