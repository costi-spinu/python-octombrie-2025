def esteMajor(varsta):
    if varsta>=18:
        return "Major"
    else:
        return "Minor"

a=esteMajor(26)
b=esteMajor(13)
print (a)
print (b)
print (esteMajor (8))