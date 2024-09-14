# n = int(input())
# a = input()
# a = a.split(" ")
# l, u = 0, 0
# for i in range(n):
#     if int(a[i]) % 2 == 0:
#         l += 1
#     else:
#         u += 1

# if l > u:
#     print("READY FOR BATTLE")
# else:
#     print("NOT READY")

t = int(input())
for i in range(t):
    a,b,c = map(int, input().split())
print(a,b,c)