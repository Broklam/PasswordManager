import random
import string
def generatepass(n):
    pass

print("Hello.\nWelcome to my little password manager.\nGlad to see you.")
input("Press Enter to continue")
print("What would you like to do?\n1.Generate a Password\n2.Manage my passports")
while True:
    try:
        choice = int(input("Please enter your choice: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
    else:
        break
while True:
    try:
        choice2 = int(input("Please enter your choice: "))
        if choice2==1:
            print("Loading Assets for Password Generator")
            break
        elif choice2==2:
            print("You choose 2")
            break
    except ValueError:
        print("Sorry, I didn't understand that.")

    else:
        print("Sorry, I didn't understand that.")
