def longestCommonPrefix(s):
    empt_str = ""
    s = sorted(s)
    f = s[0]
    l = s[-1]
    m = min(len(f), len(l))
    for i in range(m):
        if f[i] == l[i]:
            empt_str += f[i]
        else:
            return empt_str
    return empt_str


print(longestCommonPrefix(["flower", "flight", "flow"]))