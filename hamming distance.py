# def ham(x, y):
#     bin_x = bin(x)[2:]
#     bin_y = bin(y)[2:]
#     max_xy = max(bin_x, bin_y)
#     min_xy = min(bin_x, bin_y)
#     l = len(max_xy)
#     for i in range(l-1):
#         min_xy = "0" + min_xy
#     c = 0
#     for a, b in zip(min_xy, max_xy):
#         if a != b:
#             c += 1
#     return c
       
# x = 93
# y = 73
# print(ham(x, y))


 
x = 3
y = 5
bin_x = bin(x)[2:]
bin_y = bin(y)[2:]
print(bin_x)
print(bin_y)
max_xy = str(max(int(bin_x), int(bin_y)))
min_xy = str(min(int(bin_x), int(bin_y)))
print("max --> ",max_xy)
print("min --> ",min_xy)
l = len(max_xy)
if len(min_xy) != len(max_xy):
    for i in range(l-len(min_xy)):
        min_xy = "0" + min_xy
c = 0
print(min_xy)
for a, b in zip(min_xy, max_xy):
    if a != b:
        c += 1
print(c)
      