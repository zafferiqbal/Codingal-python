n = int(input())

even = [i for i in range(n) if i % 2 == 0]
odd = [i for i in range(n) if i % 2 != 0]

print(even)
print(odd)

fruits = ["apple", "banana", "mango", "orange"]

capital_fruits = [f.capitalize() for f in fruits]

print(capital_fruits)