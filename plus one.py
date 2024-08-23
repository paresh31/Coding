'''Input: digits = [4,3,2,1]
   Output: [4,3,2,2]
   Explanation: The array represents the integer 4321.
   Incrementing by one gives 4321 + 1 = 4322.
   Thus, the result should be [4,3,2,2].'''

digits = [4,3,2,9]
# Increment the last digit by 1
digits[-1] += 1
print(digits)
# If the last digit is greater than 9, carry the excess to the previous digit
for i in range(len(digits)-1, 0, -1):
    if digits[i] > 9:
        digits[i] = 0
        digits[i-1] += 1
        print(digits)  # Output: [4, 3, 2, 2]
        
