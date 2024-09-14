# 3 2 1 

# t = input()
# l = []
# for i in range(t):
#     n = int(input())
#     l.append(n)


t = int(input())
for j in range(t):
    s = input()
    l = s.split(" ")
    for i in range(len(l)):
        l[i] = int(l[i])
        
    if l[0] > l[1] and l[0] > l[2]:
        if l[1] > l[2]:
            print(l[1])
        else:
            print(l[2])
            
    if l[1] > l[0] and l[1] > l[2]:
        if l[0] > l[2]:
            print(l[0])
        else:
            print(l[2])
            
    if l[2] > l[0] and l[2] > l[1]:
        if l[0] > l[1]:
            print(l[0])
        else:
            print(l[1]) 
    

    
    
    