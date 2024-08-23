# 549843954323494990404

n = input()
c = 1
a = list(n)
for i in range(len(a)-1, -1, -1):
    if c == 1:
        if a[i] == "9":
            a[i] = "0"
        else:
            a[i] = str(int(a[i]) + 1)
            c = 0
if c == 1:
    a.insert(0, "1")
print(''.join(a))
    
            
        
