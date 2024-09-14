n = 4
s = 1
# if n == 0:
#     return 0
# if n == 1:
#     return 1
for i in range(2, n):
    s = s + i
    if s > n:
        print(i-1)
        break
    