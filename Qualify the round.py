for i in range(int(input())):
    x,a,b = map(int, input().split())
    print("Qualify" if ((a*1)+(b*2)) >= x else "NotQualify")