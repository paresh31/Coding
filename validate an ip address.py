str = "255..255.255"
l = str.split(".")
if len(l) != 4:
    print(False)
for i in l:
    if not i.isdigit() or not 0 <= int(i) <= 255:
        print(False)
    if len(i) > 1 and i[0] == "0":
        print(False)
print(True)
        