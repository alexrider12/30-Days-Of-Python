print('jA'.capitalize()) # Ja
liste = ['Thirty', 'Days', 'Of', 'Python']
new = ''
print(new.join(liste))
cfa = ['Coding', 'For', 'All']
newcfa = ''
print(newcfa.join(cfa))

company = "Coding For All"
print(company)

print(len(company))

print(company.upper())
print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())
# Nr.9
print(company.replace("Coding ",''))
# Nr.10
print(company.find("Coding"))
# Nr.11
print(company.replace("Coding ","Python"))
# Nr.12
word = "Python for everyone"
word = word.replace("everyone","all")
print(word)
# Nr.13
newList = company.split(' ')
print(newList)
# Nr.14
secoundList = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(',')
print(secoundList)
# Nr.15
print(company[0])
# Nr.16
print(company[-1])
# Nr.17
print(company[10])
# Nr.18
name = word.split(' ')
print(f"{name[0][0]}{name[1][1].upper()}{name[2][2].upper()}")
# Nr.19
print(f"{company.split(' ')[0][0]}{company.split(' ')[1][1].upper()}{company.split(' ')[2][2].upper()}")
#NR.20
print(company.index('C'))
# Nr.21
print(company.index('F'))
# Nr.22
print(company.rfind('l'))
# Nr.23
print("Nr.23", 'You cannot end a sentence with because because because is a conjunction'.index('because'))
# Nr.24
print("Nr.24", 'You cannot end a sentence with because because because is a conjunction'.rfind('because'))
# Nr.25
print("Nr.25", 'You cannot end a sentence with because because because is a conjunction'.replace('because',''))
# Nr.26
print("Nr.26", company.startswith("Coding"))
# Nr.27
print("Nr.27", company.endswith('coding'))
# Nr.28
print("Nr.28", ' Coding For All '.strip())
# Nr.29
print("Nr.29", '30DaysOfPython'.isidentifier(), 'thirty_days_of_python'.isidentifier)
# Nr.30
programmingLanguages = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
string = '# '.join(programmingLanguages)
print("Nr.30", string)
# Nr.31
print("Nr.31 \n Hello")
# Nr.32
print("Nr.32")
print("Name\tAlter\tLand\tStadt")
print("Jakob\t15\tDE\tEntenhausen")
# Nr.33
print(f"Radius: 10m\nFläche:{10**2*3.14}")
# Nr.34
print(f"8-6={8-6}\n8+4={8+4}\n8**6={8**6}")
