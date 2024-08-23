for i in range(int(input())):
    a,b = map(int, input().split())
    aa = int(a/10)*100
    bb = int(b/20)*100
    if aa == bb:
        print("Any")
    elif aa > bb:
        print("First")
    else:
        print("Second")