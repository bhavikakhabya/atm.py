
# Step 1: Create data for 3 users
card_no1 = 1234
pin1 = 6767
bal1 = 5000

card_no2 = 6234
pin2 = 1234
bal2 = 10000

card_no3 = 8891
pin3 = 3636
bal3 = 15000

# Step 2: Take input from user
card_no = int(input("Enter your card number: "))

# Step 3: Check which user it is
if card_no == card_no1:
    pin = int(input("Enter your PIN: "))
    if pin == pin1:
        print("Login Successful 1234")
        print("1: Check Balance")
        print("2: Withdraw")
        print("3: Deposit")
        choice = int(input("Enter your choice: "))

        # Option 1: Show balance
        if choice == 1:
            print("Your balance is:", bal1)

        # Option 2: Withdraw money
        elif choice == 2:
            amt = int(input("Enter amount to withdraw: "))
            if amt <= bal1:
                bal1 = bal1 - amt
                print("Withdraw Successful! New balance:", bal1)
            else:
                print("Insufficient Balance!")

        # Option 3: Deposit money
        elif choice == 3:
            amt = int(input("Enter amount to deposit: "))
            bal1 = bal1 + amt
            print("Deposit Successful! New balance:", bal1)
        else:
            print("Invalid Option!")

    else:
        print("Wrong PIN ")

elif card_no == card_no2:
    pin = int(input("Enter your PIN: "))
    if pin == pin2:
        print("Login Successful ")
        print("1: Check Balance")
        print("2: Withdraw")
        print("3: Deposit")
        choice = int(input("Enter your choice: "))

        # Option 1: Show balance
        if choice == 1:
            print("Your balance is:", bal2)

        # Option 2: Withdraw money
        elif choice == 2:
            amt = int(input("Enter amount to withdraw: "))
            if amt <= bal2:
                bal2 = bal2 - amt
                print("Withdraw Successful! New balance:", bal2)
            else:
                print("Insufficient Balance!")

        # Option 3: Deposit money
        elif choice == 3:
            amt = int(input("Enter amount to deposit: "))
            bal2 = bal2 + amt
            print("Deposit Successful! New balance:", bal2)
        else:
            print("Invalid Option!")

    else:
        print("Wrong PIN ")

elif card_no == card_no3:
    pin = int(input("Enter your PIN: "))
    if pin == pin3:
        print("Login Successful ")
        print("1: Check Balance")
        print("2: Withdraw")
        print("3: Deposit")
        choice = int(input("Enter your choice: "))

        # Option 1: Show balance
        if choice == 1:
            print("Your balance is:", bal3)

        # Option 2: Withdraw money
        elif choice == 2:
            amt = int(input("Enter amount to withdraw: "))
            if amt <= bal3:
                bal3 = bal3 - amt
                print("Withdraw Successful! New balance:", bal3)
            else:
                print("Insufficient Balance!")

        # Option 3: Deposit money
        elif choice == 3:
            amt = int(input("Enter amount to deposit: "))
            bal3 = bal3 + amt
            print("Deposit Successful! New balance:", bal3)
        else:
            print("Invalid Option!")

    else:
        print("Wrong PIN ")
else:
    print("Card not found ")