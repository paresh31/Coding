n = 6
start = [1, 3, 0, 5, 8, 5]
end   = [2, 4, 6, 7, 9, 9]
# n = 3
# start = [10, 12, 20]
# end   = [20, 25, 30]
m = [(start[i], end[i]) for i in range(n)]
print(m)
m.sort(key=lambda x: x[1])
c = 1
lt = m[0][1]
for i in range(1, n):
    if m[i][0] > lt:
        c += 1
        lt = m[i][1]
print(c)