int_myAge = 15
int_userAge = int(input("Please enter your age:\n"))
if int_userAge >= 18:
    print("You can drive")
else:
    print(f"You can't drive. You have to wait {18-int_userAge} years")
if int_userAge == int_myAge:
    print("Your age is equal to the creator of this script")
elif int_userAge > int_myAge:
    print("Your age is greater to the creator of this script")
else:
    print("Your age is less to the creator of this script")
    
int_a = int(input("Please enter a number: \n"))
int_b = int(input("Please enter another number: \n"))

if int_a > int_b:
    print("A is greater than B") 
elif int_a == int_b:
    print("A is equal to B")
else:
    print("A is less than B")
    
