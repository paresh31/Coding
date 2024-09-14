s = "A man, a plan, a canal: Panama"
s = ''.join(cha.lower() for cha in s if cha.isalnum())
print(s)
t = s[::-1]
print(t)