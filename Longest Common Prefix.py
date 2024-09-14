
def longestCommonPrefix(v: list[str]) -> str:
    ans=""
    v=sorted(v)
    first=v[0]
    last=v[-1]
    for i in range(min(len(first),len(last))):
        if(first[i] == last[i]):
            ans = ans + first[i]
        else:
            break
    if ans:
        return ans
    return -1
v = ["geeksforgeeks", "geeks", "geek", "geezer"]
print(longestCommonPrefix(v))
 