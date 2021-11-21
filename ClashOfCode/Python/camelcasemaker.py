variable_name = input()
var = ""
nextone = False

for x in variable_name:

    if nextone == True and x != "_":
        var = var + str.upper(x)
        nextone = False

    elif x == "_" and nextone != True:
        nextone = True

    elif x != "_":
        var = var + str(x)
        nextone = False

    else:
        nextone = True

print(var)