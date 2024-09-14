# chalk = [3,4,1,2]
# k = 25
# tc = sum(chalk)
# k = k % tc
# c = 0
# for i in range(len(chalk)):
#     k -= chalk[i]
#     if k < 0:
#         break
#     c += 1
# print(c)


# arr = [3, 1, 3, 3, 2]
# a = set(arr)
# for i in a:
#     if arr.count(i) > len(arr)//2:
#         print(i)


# n = 47
# arr = list(map(int, "13 33 43 16 25 19 23 31 29 35 10 2 32 11 47 15 34 46 30 26 41 18 5 17 37 39 6 4 20 27 9 3 8 40 24 44 14 36 7 38 12 1 42 12 28 22 45".split()))
# print(arr)
# d, m = 0, 0
# for i in range(1, n+1):
#     if arr.count(i) == 2:
#         d = i
#     if arr.count(i) == 0:
#         m = i
# print(d, m)

# s = "leetcode"
# k = 2
# l = ''
# for item in s:
#     l = l + str(ord(item) - 96)
# for j in range(k):
#     a = 0
#     for i in l:
#         a += int(i)
#     l = str(a)
# print(l)


# nums = [1,3,5,6]
# target = 7
# if  target in nums:
#     print(nums.index(target))
# for i in range(len(nums)):
#     if nums[i] > target:
#         print(nums.index(nums[i]))
#     else:
#         print(len(nums))


# pattern = "abba"
# s = "dog cat cat fish"
# pattern = list(pattern)
# s = s.split()
# if len(pattern) != len(s):
#     print(False)
# if len(set(s)) != len(set(pattern)):
#     print(False)
# print(pattern, s)
# dict = {}
# for i in range(len(s)):
#     dict.update({pattern[i]: s[i]})
# print(dict)
# r = True
# for i in range(len(s)):
#     if s[i] != dict.get(pattern[i]):
#         print(False)
#     else:
#         print(True)


# k = 4
# n = 4
# arr = list(map(int, "1 3 6 7".split()))
# print(arr)
# l = []
# for item in arr:
#     l.append(abs(k- item))
# print(l)
# a = l.index(min(l))
# b = l.count(a)
# if b == 1:
#     print(arr[a])
# else:


# arr = [1,2,3,4,5]
# s = ""
# for i in arr:
#     s += str(i)
# a = ' '.join(s)
# print(a)

# s = "deeee"
# r = list(s)
# t = r.copy()
# t.reverse()
# print(r,t)
# if  r == t:
#     print(True)
# else:
#     for i in range(len(r)-1):
#         if t[i] != r[i]:
#             t.pop(i)
#             r.pop(-1-i)
#             break
#     print(r,t)
#     if r == t:
#         print(True)
#     else:
#         print(False)

# 1122 2605  2965
# arr1 = [2,3,1,3,2,4,6,7,9,2,19]
# arr2 = [2,1,4,3,9,6]
# el = []
# for i in range(len(arr2)):
#     a = arr1.count(arr2[i])
#     for j in range(a):
#         el.append(arr2[i])
# print(el)
# el2 = []
# for i in range(len(arr1)):
#     if arr1[i] not in arr2:
#         el2.append(arr1[i])
# el2.sort()
# print(el + el2)


# s = "fvevzh"
# k = 10
# if  k > len(s):
#     k = k % len(s)
# r = s[k:]
# r += s[:k]
# print(r)

# b = 4
# l = 2
# s = 1
# bb = 0
# ll = 0
# while s <  b and s < l:
#     if s > bb:
#         print("b")
#     elif s > ll:
#         print("l")
#     ll += s
#     bb += s+1
#     s += 2


# for i in range(t):
#     c = 0
#     co = 0
#     s1 = input()
#     s2 = input()
#     for i in range(len(s1)):
#         if s1[i] != "?" and s2[i] != "?":
#             if s1[i] != s2[i]:
#                 c = c + 1

#         if s1[i] != "?" and s2[i] != "?":
#             if s1[i] == s2[i]:
#                 co = co + 1

#     print(c, end=" ")
#     print(len(s1) - co)
# print()


# nums1 = [4,1,3]
# nums2 = [5,7]
# l = list()
# for item in nums1:
#     if item in nums2:
#         l.append(item)
# if l: 
#     print(min(l))
# n1 = min(nums1)
# n2 = min(nums2)
# print((min(n1,n2)*10) + max(n1,n2))



# grid = [[9,1,7],[8,9,2],[3,4,6]]
# l = []
# n = len(grid[0])
# for i in range(n):
#     for j in range(n):
#         l.append(grid[i][j])
# r,m = 0,0
# for i in range(0, len(l)):
#     if i+1 not in l:
#         m = i+1
#     if l.count(l[i]) == 2:
#         r = l[i]
# print(r,m)



# start = 3
# goal = 4
# less = min(start, goal)
# more = max(start, goal)
# bs = bin(start)[2:]
# bg = bin(goal)[2:]
# ma = max(len(bs), len(bg))
# mi = min(len(bs), len(bg))
# bm = bin(more)[2:]
# bl = bin(less)[2:]
# rl = bl[::-1]
# for i in range(ma-mi):
#     rl += "0"
# rl = rl[::-1]
# c = 0
# for i in range(len(bm)):
#     if bm[i] != rl[i]:
#         c += 1
# print(c)


# arr = [4, 2, 7, 6, 9]
# l = []
# while len(arr) != 1:
#     m1 = min(arr)
#     arr.remove(m1)
#     m2 = min(arr)
#     arr.remove(m2)
#     arr.append(m1+m2)
#     l.append(m1+m2)
# print(sum(l))

# allowed = "ab"
# words = ["ad","bd","aaab","baa","badab"]
# la = list(allowed)
# na = []
# print(la)
# for i in range(len(words)):
#     for j in range(len(words[i])):
#         if words[i][j] not in la:
#             na.append(words[i])
# print(na)
# print(len(words) - len(na))

            
# allowed = "ab"
# words = ["ad","bd","aaab","baa","badab"]
# a_set = set(allowed)
# c = 0
# for word in words:
#     if all(char in a_set for char in word):
#         c += 1 
# print(c)


# arr = [1, 2, 13, 4]
# c = 0
# l = []
# for i in range(len(arr)):
#     if "1" in str(arr[i]) or "2" in str(arr[i]) or "3" in str(arr[i]):
#         c += 1
#         l.append(c)
# print(l)


# s = "015"
# n = int(s)
# r = n % 10
# if r > 5:
#     res =  n + (10 - r)
# else:
#     res =  n - r 
# ress = str(res)
# for i in range(len(ress)):
#     if ress[i] != "0":
#         break
#     else:
#         ress = "0" + ress   
# print(ress)

# n = 654
# a,b = n*2,n*3
# x = str(n)+str(a)+str(b)
# print(int(x))

# arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
# p,n,a = [],[],[]
# for i in arr:
#     if i >= 0:
#         p.append(i)
#     else:
#         n.append(i)
# m = min(len(p), len(n))
# for i in range(m):
#     a.append(p[i])
#     a.append(n[i])
# if len(p) > len(n):
#     a.extend(p[m:])
# else:
#     a.extend(n[m:])
# print(a)


# n,m = map(int, input().split())
# n,m = 1,10
# l = []
# for i in range(n,m+1):
#     c = 0
#     for j in range(1,i):
#         if i % j == 0:
#             c+=1 
#     if c == 1:
#         l.append(i)
# print(l)

