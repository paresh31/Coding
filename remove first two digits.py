t = int(input())
while t > 0:
    n = input()
    s = ""
    ft = n[0] + n[1]
    fti = int(ft)
    if fti == 10:    
        for i in range(2, len(n)):
            s = s + n[i]
        s = int(s)
        if s > 2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    t -= 1