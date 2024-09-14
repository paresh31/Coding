str1 = "ababab"
str2 = "abab"
s1, s2 = list(str1), list(str2)
s = ""
for i in range(min(len(s1), len(s2))):
    if s1[i] == s2[i]:
        s = s + s1[i]
x = max(len(s1), len(s2)) / min(len(s1), len(s2))
if x < 2:
    a = max(len(s1), len(s2)) - min(len(s1), len(s2))
    s = s[:a]
b = max(len(s1), len(s2)) // min(len(s1), len(s2))
c = s*b
print(str1)
print(c)
if str1 == c or c == s:
    print(s)
print("")

        