s = "zvvo"
seen = set()
result = []
for char in s:
    if char not in seen:
        seen.add(char)
        result.append(char)
print(''.join(result))
