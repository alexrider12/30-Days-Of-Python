score = int(input("Please enter your score:\n"))

if score <= 100 and score >= 90:
    print("Grade: A") 
elif score <= 89 and score >= 80:
    print("Grade: B")  
elif score <= 79 and score >= 70:
    print("Grade: C")   
elif score <= 69 and score >= 60:
    print("Grade: D")   
elif score <= 59 and score >= 0:
    print("Grade: F")   
else:
    print("Please enter a score between 100 and 0")
    
userMonth = input("Please enter a month:\n")
trysMonths = 0
months = {
    "Spring": ["March","April","May"],
    "Summer": ["June","July","August"],
    "Autumm": ["September","October","November"],
    "Winter": ["December","January","February"]
}
for aSeason in months.keys():
    if userMonth in months[aSeason]:
        print(f"{userMonth} is in the {aSeason}")
        break
    else:
        trysMonths += 1
        if trysMonths >= 4:
            print("Your month doesnt exists or is typed wrog")
            break


# if userMonth in months["Spring"]:
#     print(f"{userMonth} is in the Spring")
# elif userMonth in months["Summer"]:
#     print(f"{userMonth} is in the Summer")
# elif userMonth in months["Autumm"]:
#     print(f"{userMonth} is in the Autumm")
# elif userMonth in months["Winter"]:
#     print(f"{userMonth} is in the Winter")
# else:
#     print("Your month doesnt exists or is typed wrog")
    
# print("spring") if userMonth in months["spring"] else print("Nothing")
fruits = ['banana', 'orange', 'mango', 'lemon']
userFruit = input("Please enter your fruit:\n")

if userFruit.lower() not in fruits:
    fruits.append(userFruit)
    print(fruits)
else:
    print("That fruit already exist in the list")