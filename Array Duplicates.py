# 2 3 1 2 3
# n = int(input("-->: "))
# l = list()
# for i in range(n):
#     l.append(int(input()))
# print(l)
# s = set()
# for item in l:
#     c = l.count(item)
#     if c > 1:
#         s.add(item)
# if len(s) == 0:
#     print(-1)
# else:
#     print(s)


from typing import List

def duplicates(n : int, arr : List[int]) -> List[int]:
    # code here
    s = set()
    for i in range(len(arr)):
        c = arr.count(arr[i])
        if c > 1:
            s.add(arr[i])
    if len(s) == 0:
        return(-1)
    else:
        return(s)
print(duplicates(n = 5, arr = [2,3,1,2,3]))
    