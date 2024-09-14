s = "123456789"
lt = len(s)
s_reverse = s[::-1]
print(s_reverse)
if  lt % 2 == 0:
    lt = lt // 2
else:
    lt = (lt + 1) // 2
s1=""
s1 = s[:lt]
s2 = s_reverse[lt:]
print(s1)
print(s2)
print(s1+s2)
