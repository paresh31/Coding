x = int(input())
s = input()
l = len(s)
chef, carl, = 0, 0
if l == 14:
    for i in range(l):
        if s[i] == 'C':
            carl = carl + 2
        elif s[i] == 'N':
            chef = chef + 2
        elif s[i] == 'D':
            carl = carl + 1
            chef = chef + 1
        else:
            break
    if carl > chef:
        print(x * 60)
    elif carl < chef:
        print(x * 40)
    else:
        print(x * 55)
else:
    print("enter score of 14 matches")


        
            