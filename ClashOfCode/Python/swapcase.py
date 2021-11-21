s = input()
n = ""

for x in s:
    if x.isupper() == True:
        n = n + str.lower(x)
    else:
        n = n + str.upper(x)

print(n)

# I have found out that this code can be massively simplified
# All you have to do is use swapcase().
# print(s.swapcase()) Does the exact same as the for loop above.