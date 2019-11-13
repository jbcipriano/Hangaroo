import string
alph = string.ascii_lowercase
def getAvailableletters(lettersGuessed):
    remain=[]
    for i in alph:
        if i not in lettersGuessed:
            remain.append(i)
    return ''.join(remain)