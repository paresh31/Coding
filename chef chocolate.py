t = int(input())

while t > 0:
    x, y, z = map(int, input().split())
    tot_cho = (x*5 + y*10)//z
    print(tot_cho)





    t -= 1