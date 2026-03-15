def circumference(radius):
    pi = 3.14
    c = 2 * pi * radius
    return c

r = float(input("Enter the radius of the circle: "))

result = circumference(r)

print("Circumference of the circle is:", result)