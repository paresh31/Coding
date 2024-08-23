n = int(input("Enter a number: "))
if n % 2 == 0 and n % 7 == 0:
    print("Alice")
elif n % 2 != 0 and n % 9 == 0:
    print("Bob")
else:
    print("Charlie")