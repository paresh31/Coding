t = int(input())
while t > 0:
    n = int(input())
    l = list(map(int, input().split()))
    if len(l) == n:
        print(max(l))
        
        
    t -= 1