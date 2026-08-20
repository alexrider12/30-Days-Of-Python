dog = {}
dog["Name"] = "Lulu"
dog["Alter"] = 10
dog["Rasse"] = "Pudel"
dog["Beine"] = 4
dog["Farbe"] = "gefleckt"
print(dog)

student = {
    "Vorname": "Jakob",
    "Nachname": "Rolle",
    "Alter": 15,
    "skills":["Python", "Tech"]
}
print("Length:",len(student))
print("Datentyp: ",type(student["skills"]))

student["skills"].append("Git")
student["skills"].append("Arduino")
print(student)

print("Keys: ",student.keys())          # Alternativ eine Variable mit dem Wert student.keys() deklarieren
print("Values: ", student.values())     # -""-

list_of_tuples = student.items()
print(list_of_tuples)

student.pop("Nachname")
print(student)

del dog
try:
    print(dog)
    
except NameError:
    print(" \"dog\" is not defined")