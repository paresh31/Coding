arr = [1,2,3,5]
r = "false"
s = sum(arr)
half = int(s/2)
h = s/2
if h - half != 0:
    print(r)
else:
    c = 0
    for i in range(len(arr)):
        c = c + arr[i]
        if c == half:
            r = "true"
            break
        else:
            continue
    print(r)

