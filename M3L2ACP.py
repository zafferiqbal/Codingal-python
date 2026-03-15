def shutdown():
    answer = input("Do you want to shut down the system? (yes/no): ")

    if answer == "yes":
        print("Shutting down...")
    elif answer == "no":
        print("Shutdown aborted.")
    else:
        print("Invalid input")

shutdown()