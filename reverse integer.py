# reverse integer
# y = 1534236469
# z = (2**31)-1
x = 1534236469

# print(z)
# print(y)

a = str(x)

if a[0] != "-":
    b = ""
    for i in range (len(a)-1, -1, -1):
        b = b + a[i]
    b = int(b)
    if b >= (2**31)-1:
        print("0")
    else:
        print(b)    
else:
    b = "-"
    for i in range (len(a)-1, 0, -1):
        b = b + a[i]
        if b <= -(2**31):
            print("0")
        else:
            print(b)


    


