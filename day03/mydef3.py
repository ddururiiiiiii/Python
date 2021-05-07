def addmin(a, b):
    return a+b, a-b

sum, min = addmin(5, 6)
print(sum, min)
print(min)

min =  addmin(5, 6)[1]
print(min)

