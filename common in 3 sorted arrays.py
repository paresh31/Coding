arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
s1,s2,s3 = set(arr1),set(arr2),set(arr3)
u = s1.intersection(s2)
t = u.intersection(s3)
t = list(t)
t.sort()
print(t)