# fib =  0, 1, 1, 2, 3, 5, 8, 13, 21, 34
n = int(input("->"))
a = 0
b = 1
fib = [0]
for i in range(0, n+1):
    c = a + b % 1000000007
    b = a
    a = c
print(b)
