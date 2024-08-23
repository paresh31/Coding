# arr = [1,2,34,3,4,5,7,23,12]
# l = len(arr)
# r = False
# for i in range(l-2):
#     if (arr[i] % 2!= 0) and (arr[i+1] %2 != 0) and  (arr[i+2] != 0):
#         t = True
# print(t)

# s = ["h","e","l","l","o"]
# l = list()
# for i in range(len(s)-1,-1,-1):
#     print(s[i])
#     l.append(s[i])
# s = l.copy()
# print(s)

n = 5
s = (bin(n)[2:])
print(s)
e = s[::-1]
print(e)
d = int(e, 2)
print(d)
