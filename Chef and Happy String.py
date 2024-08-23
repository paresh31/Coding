s = input()
l = ['a', 'e', 'i', 'o', 'u']
c = 0
for i in range(len(s)-2):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        if s[i+1] == 'a' or s[i+1] == 'e' or s[i+1] == 'i' or s[i+1] == 'o' or s[i+1] == 'u':
            if s[i+2] == 'a' or s[i+2] == 'e' or s[i+2] == 'i' or s[i+2] == 'o' or s[i+2] == 'u':
                c = c + 1
                break
            else:
                continue
        else:
            continue
    else:
        continue
print("Happy") if c == 1 else print("Sad")

            
            