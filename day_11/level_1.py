print("---1.1---")
def add_two_numbers(num_1, num_2):
    result = num_1 + num_2
    return result

print(add_two_numbers(1, 2))

print("---1.2---")
def area_of_circle(radius):
    area = radius ** 2 * 3.14
    return area
print(area_of_circle(3))

print("---1.3---")
def add_all_nums(*args):
    result = 0
    for num in args:
        if type(args[1]) == int:
            result += num
        else: 
            return "Enter numbers only"
    return result
    
print(add_all_nums(1, 2, 3))

print("----1.4---")
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit
print(convert_celsius_to_fahrenheit(100)) 

print("----1.5---")
def check_season(month):
    # Autumn, Winter, Spring or Summer
    spring = ["march", "april", "may"]
    summer = ["june", "july", "august"]
    autumn = ["september", "october", "november"]
    winter = ["december", "january", "february"]
    if month.lower() in spring:
        return "Spring"
    elif month.lower() in summer:
        return "Summer"
    elif month.lower() in autumn:
        return "Autumm"
    elif month.lower() in winter:
        return "Winter"
    else:
        return "Not a valid month"
print(check_season("september"))

print("----1.6---")
def calculate_slope(x1, y1, x2, y2):
    slope = ((y2 - y1) / (x2 - x1))
    return slope
print(calculate_slope(1, 1, 3, 4))

# 1.7 übersprungen
# 1.7 not solved

print("----1.8---")
def print_list(list):
    for item in list:
        print(item)
numbers = [1, 2, 3, 4]
print_list(numbers)

print("----1.9---")
def reverse_list(list):
    newList = []
    for i in range(len(list), 0, -1):
        newList.append(list[i-1])
    return newList 
print(reverse_list(numbers))

print("----1.10---")
def capitalize_list_items(list):
    newList = []
    for i in range(len(list)):
        
        newList.append(str(list[i]).upper())
    return newList
aList = ["afdsA", "dfs1", "sdf", 1]
print(capitalize_list_items(aList))

print("----1.11---")
def add_item(list, *args):
    for a in args:
        list.append(a)
    return list   

print("---1.12---")
def remove_item(list, item):
    if item in list:
        list.remove(item)
        return list
    else:
        return "Item not found"
print(remove_item(aList, 1))

print("---1.13---")
def sum_of_numbers(last_number):
    result = 0
    for i in range(1, last_number+1):
        result += i
    return result
print(sum_of_numbers(100))

print("---1.14---")
def sum_of_odds(last_number):
    result = 0
    for i in range(last_number+1):
        if i % 2 != 0:
            result += i
        else:
            continue
    return result
print(sum_of_odds(4))

print("---1.15---")
def sum_of_even(last_number):
    result = 0
    for i in range(last_number+1):
        if i % 2 == 0:
            result += i
        else:
            continue
    return result
print(sum_of_even(4))