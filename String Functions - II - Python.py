# S = "gFgabcdEGfG"
# b = S.lower()
# print(b)
# print(b[:3])
# print(b[-1:-4:-1])
# if(b[:3] == "gfg" and b[-1:-4:-1] == "gfg"):  
#     print ("Yes")
# else:
#     print ("No")


N = 7 
sum = 8 
arr = [1, 2, 3, 3, 5, 5, 5] 
for i in range(N-1):
    for j in range(i+1, N):
        if arr[i] + arr[j] == sum:
            print(True)
        break