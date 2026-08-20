person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:          # Man soll in person keys suchen, passt das dann so (es funktioniert!)
    print(f"Skills: {person['skills'][len(person['skills'])//2]}")
    if "React" in person['skills'] and "Node" in person['skills'] and "MongoDB" in person['skills']: #in der nächsten if-abfrage
        print('He is a fullstack developer')                                                         #besser gelöst (kürzer)
    elif "Node" and "Python" and "MongoDB" in person['skills']:
        print('He is a backend developer')
    elif "JavaScript" and "React" in person['skills']:
        print('He is a front end developer')
    else:
        print('unknown title')

if person['is_married'] and person['country'] == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")