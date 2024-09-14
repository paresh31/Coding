# 00 is replaced with A
# 01 is replaced with T
# 10 is replaced with C
# 11 is replaced with G

n = int(input("--->"))
s = input()
print(s)
l = []
for i in range(0, n, 2):
    l.append(s[i]+s[i+1])
print(l)
nl = []
for i in range(n//2):
    if l[i] == "00":
        nl.append("A")
    elif l[i] == "01":
        nl.append("T") 
    elif l[i] == "10":
        nl.append("C") 
    elif l[i] == "11":
        nl.append("G")
    else:
        continue
print(nl)
fs = ""
for item in nl:
    fs = fs + item
print(fs)