import math

print("Print your card number")
card = input()
digit_sum = 0

for i, digit in enumerate(reversed(card)):
    n = int(digit)
    if i % 2 == 0:
        digit_sum += n
    else:
        num = n * 2
        if num > 9:
            digit1 = num % 10
            num = math.floor(num / 10)
            digit2 = num % 10
            digit_sum = digit_sum + digit1 + digit2
        else:
            digit_sum += num
print(digit_sum)
if digit_sum % 10 == 0:
    print("Card is valid!")
else:
    print("Card is invalid!")