age = 15
print("Type age:", type(age))
height = 170.0
print("Type height: ", type(height))
complex = (1 - 1j)
print("Type complex: ", type(complex))

base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = base * height * 0.5
print('The area of the triangle is:', area)
print("--")

a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))

perimeter2 = a + b + c
print("The Perimeter of the triangle is", perimeter2)
print("--")
print("Rectangle")

length = int(input("Enter length: "))
width = int(input("Enter width: "))
area51 = length * width
print('Area51:', area51)

perimeter51 = 2*(length + width)
print('Perimeter51:', perimeter51)

radius = float(input("Enter the radius of the circle: "))
circleArea = radius * radius * 3.14
print("area of the circle:", circleArea)

circumference = 2 * 3.14 * radius
print("circumference:", circumference)
# Nr. 8, 9, 10, 11 übersprungen
# Nr.12

#Nr.13
print('on' in 'python' and 'on' in 'dragon')
# Nr.14
print("Jargon",'jargon' in 'I hope this course is not full of jargon')
# Nr.15
print("on not in jargon or dragon", 'on' not in 'jargon' and 'on' not in 'python')
# Nr.16
print("str, float, len of python", str(float(len('python'))))
# Nr.17 Teilbarkeit
print("Teilbarkeit:", 4 %2==0)
# Nr.18
print("ganzahldivision: ", 7//3 == int(2.7))
print(int(2.7))
# Nr.19
print("Typenvergleich:", type(10) == type('10'))
# Nr.20
print("is 9.8 equal to 10:",float('9.8') is float(10))
#Gehaltsrechner Nr.21
hours = int(input("Hours worked: "))
moneyperHour = int(input("Money per hour: "))
weeklyPay = hours * moneyperHour
print("weekly pay:", weeklyPay)
# Nr.22 Gelebte Sekunden
livedYears = int(input("How old are you: "))
livedSeconds = (livedYears * 365,24 * 24 * 60 * 60)
print("Lived seconds:", livedSeconds)


for _ in range(1, 6):
    print(_, 1 ,_,_**2,_**3)