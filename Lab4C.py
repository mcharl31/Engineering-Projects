# Class: CSE 1321L
# Section: BJF
# Term: Fall 2024
# Instructor: Nisha Bagdwal
# Name: Micah Charles
# Lab:4C
t = 1000
print(f"Welcome!\nYou have ${t} in your account.")


q = True

while q != False:
    m = int(input("Menu\n0 – Make a deposit\n1 – Make a withdraw\n2 – Display account value\n\n Please make a selection: "))

    if m == 0:
        d = float(input("How much would you like to deposit?: "))
        t += d
        answer = input(f"Your total balance is ${t}\nWould you like to return to main menu (Y/N)?: ")
        if  answer == "N":
            q = False


    if m == 1:
        d = float(input("How much would you like to withdraw?: "))
        if d > t:
            print(f"Not enough balanced. Withdrawal cancelled\nYour current balance is ${t}\nWould you like to return to main menu (Y/N)?: ")
            if answer == "N":
                q = False
        else:
            t -= d
            answer = input(f"Your current balance is ${t}\nWould you like to return to main menu (Y/N)?: ")
            if  answer == "N":
                q = False


    elif m == 2:
        print(f"Your current balance is ${t}")
        answer = input(f"Your current balance is ${t}\nWould you like to return to main menu (Y/N)?: ")
        if answer == "N":
           q = False

    else:
        print("Invalid entry, please try again.")
        answer = input("Would you like to return to main menu (Y/N)?: ")
        if answer == "N":
            q = False

    if q == False:
        print("Thank you for banking with us!")
