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

C = A.union(B)
D = B.union(A)
print("A U B" , C)
print("B U A", D)

print("Symetrische Differenz:",A^B)

print("A",A)
print("B",B)

#del A
#del B

# --- Level 3 ---
set_age = set(age)
print(f"Lengths: A:{len(A)} B:{len(B)} age:{len(set_age)}")

print("""Ein String ist ein Text, eine Liste ist eine Aufzählung 
      von mehreren Texten und Zahlen und ist veränderbar.
      Ein Tuple ist wie eine Liste, ist aber unveränderbar.
      Ein Set bildet eine Menge ab (ähnlich zur Liste), erlaubt aber
      keine Duplikate. 
      """)

#singleWords = set()
singleWords = set("I am a teacher and I love to inspire and teach people.".split(" "))
print(singleWords)
print("Anzahl einzelner Wörter:", len(singleWords))