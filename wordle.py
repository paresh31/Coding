s = input()
t = input()
m = ""
for i in range(5):
    if s[i] == t[i]:
        m = m + "G"
    else:
        m = m + "B"
print(m)