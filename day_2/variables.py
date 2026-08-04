# Day 2: 30 Days of python programming
first_name = "JAkob"
last_name = "ROlle"
full_name = first_name + " " + last_name
print(3%2)
#exit()
print('b'.upper() in 'BER')
#exit()
country = "Panama"
city = "Hometown"
age = 10
year = 2000
is_married = False
is_true = False
is_light_on = True
a, b, c = 1, 2, 3

variables = [first_name, last_name, full_name, country, city, age]
for _ in variables:
    print(_, type(_))

print('First Name:', first_name)
print('Length:', len(first_name))
print('Age:', age)
print(a, b, c)
print('Lengths: ', len(first_name), len(last_name))

num_one = 5
num_two = 4

diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainer = num_two % num_one
exp = num_one**num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = radius**2 * 3,14
circumference_of_circle = radius * 2 * 3,14
print(circumference_of_circle)
userRadius = input("Enter radius:\n")
#userArea_of_circle = userRadius**2 * 3,14
#print(userArea_of_circle)
print(help('keywords'))

informations = {
    'first name': input("First Name: \n"),
    'last_name': input("Last Name: \n")

}

for _ in informations:
    print(_,':',informations[_])

print(True)
print(False)

