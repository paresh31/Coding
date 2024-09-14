s  = input("Enter the wining string: ")
alice, bob = 0, 0
s = list(s)
print(s)
if s[0] == 'A':
        alice += 1
for i in range(len(s)-1): 
    if s[i] == 'A' and s[i+1] == 'A':
        alice += 1
    if s[i] == 'B' and s[i+1] == 'B':
        bob += 1
print (alice, bob)
            
            