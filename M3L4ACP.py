try:
    age = int(input("Enter your age: "))
    
    if age <= 0 or age > 120:
        print("Age entered is incorrect")
    else:
        print("Age entered is correct")
        
        if age % 2 == 0:
            print("Age is even")
        else:
            print("Age is odd")

except ValueError:
    print("Invalid input") 