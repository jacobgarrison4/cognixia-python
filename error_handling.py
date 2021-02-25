try:
    user_int = int(input("Please enter an integer: \n"))
    print("Sick number dude")
except ValueError:
    print("You did not enter a value that can be cast as an integer!")
except Exception:
    print("General exception")
finally:
    pass

print("End of program")


n =2 
if n < 5:
    raise Exception
print("End of program")



















