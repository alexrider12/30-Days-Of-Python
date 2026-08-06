my_tuple = ()
sisters = ("Julia", "Maria")
brothers = ('John','Leon')
siblings = sisters + brothers
print("sinlings:",len(siblings))

print(type(siblings))
siblings = list(siblings)
siblings.extend(["Bob", "Maria"])

family_members = list(siblings)
family_members = tuple(family_members)
print(family_members)

print("---Level2---")

item1, item2, item3, *rest = family_members
print(item1)

fruits = ("Apple","Banana")
vegtables = ("Tomato","Potato")
animalProducts = ("egg", "milk")

food_stuff_tp = fruits + vegtables + animalProducts
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
del food_stuff_tp

nordic_countries = ('Dänemark', 'Finnland', 'Island', 'Norwegen', 'Schweden')
print('Island' in nordic_countries)

# print(food_stuff_tp)