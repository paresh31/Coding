s = input("Enter the string : ")
l = s.split()
head = list()
for item in l:
    head.append(item[0].upper())
print(head)
tail = list()
for item in l:
    new_item = item[1:]
    tail.append(new_item)
print(tail)
res = ""
for i in range(len(head)):
    r = head[i] + tail[i] + " "
    print(r, end='')
print()
    







# cook your dish here
# def firCap(s):
#     l = s.split()
#     head = list()
#     for item in l:
#         head.append(item[0].upper())
#     tail = list()
#     for item in l:
#         new_item = item[1:]
#         tail.append(new_item)
#     for i in range(len(head)):
#         r = head[i] + tail[i]
#         print(r, end=' ')
#     print()
# t = int(input())
# while t > 0:
#     s = input()
#     firCap(s)
#     t -= 1


     
        


    
    
    

