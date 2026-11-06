print("---2.1---")
def evensAndOdds(endNumber):
    evens = 0
    odds = 0
    for i in range(0, endNumber+1):
        if i % 2 == 0:
            evens += i
        elif i % 2 != 0:
            odds += i
    return evens, odds
print(evensAndOdds(50))