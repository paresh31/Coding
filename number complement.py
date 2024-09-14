n = 5
bin_n = bin(n)[2:]
print(bin_n)
s = ""
for i in range(len(bin_n)):
    print(bin_n[i])
    if int(bin_n[i]) == 1:
        s = s + "0"
    else:
        s = s + "1"
print(s)
print(int(s, 2))
