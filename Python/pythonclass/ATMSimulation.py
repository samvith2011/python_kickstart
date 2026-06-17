def atmsimulation():
    atm_pin = 1234
    user_pin = int(input("What is your PIN\n"))
    if atm_pin != user_pin:
        print("That is not correct")

    else:
        user_balance = 10000.00
        while True:


            user_input = input("What do you want to do? Please enter option 1,2,3,4 as a number. \n Option 1: Check Balance \n Option 2: Deposit Money  \n Option 3: Withdraw Money \n Option 4: Exit \n")
            if user_input == "1":
                print("Your Balance is",user_balance)
            elif user_input ==  "2":
                depositmoney = float(input("Please enter money to be deposited\n"))
                user_balance = user_balance + depositmoney
                print("Your  new balance is", user_balance)
            elif user_input == "3":
                withdrawnmoney = float(input("Please enter money to be withdrawn\n"))
                if user_balance - withdrawnmoney < 0:
                    print("You cannot make this withdrawal, you do not have sufficient funds")
                    continue
                user_balance = user_balance - withdrawnmoney
                print("Please collect",withdrawnmoney,".","\n","Your new balance is",user_balance)
            else:
                print("Thank you")
                break

atmsimulation()