start = int(input())
end = int(input())

squares = [i**2 for i in range(start, end + 1)]

even = [x for x in squares if x % 2 == 0]
odd = [x for x in squares if x % 2 != 0]

print("Squares:", squares)
print("Even Squares:", even)
print("Odd Squares:", odd)