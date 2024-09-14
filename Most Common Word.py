import re
paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
cleaned_paragraph = re.sub(r'[^A-Za-z0-9\s]', ' ', paragraph)
p = cleaned_paragraph.lower()
l = p.split()
print(l)
print(banned)
l = [word for word in l if word not in banned]
print(l)
c = 0
for item in l:
    if l.count(item) > c:
        c = l.count(item)
        s = item
print(s)

