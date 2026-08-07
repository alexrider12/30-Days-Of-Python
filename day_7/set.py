it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Nr.1 Length:",len(it_companies))

it_companies.add("Twitter")
print(it_companies)

it_companies.update(["X.com","Vector"])

it_companies.discard("Facebook")
print("Discard vs. Pop->\nBei pop kommt eine Fehlermeldung wenn das Element nicht exestiert") 

# Level 2

AB = A.union(B)
#AB.union(A, B)
print(AB)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))


