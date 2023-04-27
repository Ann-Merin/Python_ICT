
def swapi(x):
    stri = ""
    for i in x:
        if i.isupper():
            stri += i.lower()
        else:
            stri += i.upper()

    return stri


name = input("Enter string ")
result = swapi(name)
print(result)
