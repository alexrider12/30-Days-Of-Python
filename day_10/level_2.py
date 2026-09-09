print("---1---")
result = 0
for number in range(1, 101):
    result += number
print(result)

print("---2---")
uneven = 0
even = 0
for number in range(1, 101):
    if number % 2 == 0:
        even += number
    elif number % 2 != 0:
        uneven += number
print(f"Even: {even}")
print(f"Uneven: {uneven}")