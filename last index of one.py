def lastIndex(s: str) -> int:
    # code here
    t = str(s)
    r = -1
    for i in range(len(t)-1,-1,-1):
        if int(s[i]) == 1:
            r = i
            break
    return(r)

a = 20001
print(lastIndex(a))