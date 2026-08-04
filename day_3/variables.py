age = 15
height = 170.0
complex = (1 - 1j)

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

print(int(9.8) is 10)
print('on' in 'python' and 'on' in 'dragon')