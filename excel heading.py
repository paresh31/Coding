n = int(input("Enter the number: "))
if 1 <= n <= 2147483647:
    result = []
    temp_number = n
    while temp_number > 0:
        temp_number -= 1
        result.append(chr(temp_number % 26 + ord('A')))
        temp_number //= 26
    cn = ''.join(result[::-1])
    print(cn)