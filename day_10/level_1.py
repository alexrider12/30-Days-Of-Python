
for number in range(0, 11):
    print(number)

print("---1.5---")
number = 0
while number <= 10:
    print(number)
    number += 1

print("---2---")
for number in range(10, -1, -1):
    print(number)
    
print("---3---")
hashtag = '#'
for _ in range(1, 9):
    print(_*hashtag)
    
print("---4---")
for row in range(1, 9):
    output = ""
    for _ in range(1, 9):
        output += hashtag
    print(output)

print("---5---")
for number in range(0, 11):
    print(f"{number} x {number} = {number**2}")
    
print("---6---")
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in languages:
    print(language)
    
print("---7---")
for number in range(0, 101):
    if number % 2 == 0:
        print(number)