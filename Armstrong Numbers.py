n = 153
temp = n
s = 0
while n > 0:
    rem = n % 10
    s = s + (rem**3)
    n = n // 10
if s == temp:
    print(True)
else:
    print(False)