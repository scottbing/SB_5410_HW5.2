numbers = set()
evens = set()
threes = set()

for i in range(20):
    numbers.add(i)
    if i%2 == 0:
        evens.add(i)
    if i%3 == 0:
        threes.add(i)
print("All: ", numbers)
print("Evens: ", evens)
print("odds: ", numbers - evens)
print("Mult. 3: ", threes)
print(threes-evens)
print(threes - (threes-evens))
odds = numbers - evens
print(threes-odds)

odds = numbers - evens
evens.discard(0)
evens.discard(100)

print(evens.intersection(threes))  #same as &
print("do odds and evens have zero common elements?")
print(odds.isdisjoint(evens))

print("Is every element in odds found in numbers?")
print(odds.issubset(numbers))

print("Is it true that numbers containevery element in these sets?")
print(numbers.issuperset((threes & odds)))

print("Is it tur that evens and odds together are all numbers?")
print(numbers == odds.union(evens))     #false becuse of '0' removal earlier

print("What about if I include the set containing 0?")
print(numbers == odds.union(evens.union({0})))

print(len(evens))
print("Popped val: ", evens.pop())
print(len(evens))
evens.clear()
print(len(evens))