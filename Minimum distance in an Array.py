arr = [1,2,3,2]
x = 1
y = 2
if ((x not in arr) or (y not in arr)):
    print(-1)
ix = arr.index(x) 
iy = arr.index(y)
r = abs(ix-iy)
print(r)
