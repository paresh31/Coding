# a = [1,2,3,5]
n = int(input("Enter the list length: "))
l = list()
for i in range(n-1):
    l.append(int(input()))
# print(l)
# for i in range(n-1):
#     if l[i] != i+1:
#         print(i+1)

s = int((n*(n+1))/2)
c = 0
for i in l:
    c = c + i
print(s-c)