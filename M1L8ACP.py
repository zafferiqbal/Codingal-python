num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

sparenumber = num1   
num1 = num3       
num3 = num2       
num2 = sparenumber   

print("After swapping:")
print("Number 1 is now:", num1)
print("Number 2 is now:", num2)
print("Number 3 is now:", num3)