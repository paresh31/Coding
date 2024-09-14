num = 14
x = num ** .5
print(x)
x = str(x)
l = x.split(".")
print(l)
if l[1] == "0":
    print(True)
else:
    print(False)