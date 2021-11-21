unastring = ""

count = int(input())
for unary in input().split():
    if unary == "1":
        unastring = unastring + unary
        pass
    elif unary != "1":
        unastring = unastring + unary

print(unastring)