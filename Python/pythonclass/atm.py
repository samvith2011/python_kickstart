'''
Algorithm:
1.create a pin code and make it a variable, and, to log in, ame it ask for a pin code
2.Create a variable, account_balance, which shows your account balance
3. Make it easy to add and withdraw money

'''


def atm():
    atm_pin = 12345
    user_pin = int(input("Enter PIN\n"))
    while user_pin != atm_pin:
        user_pin = int(input("Wrong password, try again:\n"))
    if user_pin == atm_pin:
        print("Password Correct")
        atm_balance()

#print(atm())
def atm_balance():
    user_balance = 0
    print("Balance")
    print(user_balance)
    while True:

        add_money = "add"
        sub_money = "subtract"
        dda = "No"

        money_interact = input("would ypu like to add or subtract money\n")
        if money_interact == add_money:
            money_addnumber = int(input("How much money would you like to add?\n"))
            print("New Balance:")
            user_balance = user_balance + money_addnumber
            print(user_balance)
        if money_interact == sub_money:
            money_subnumber = int(input("How much money would you like to subtract?\n"))
            print("New Balance:")
            user_balance = user_balance - money_subnumber
            print(user_balance)
        if money_interact == dda:
            print("Balance")
            print(user_balance)
        user_exit = "Yes"
        atm_exit = input("Do you want to exit\n")
        if user_exit != atm_exit:
            continue
        if user_exit == atm_exit:
            break


#atm()
'''
Algorithm:
1. Create a pin
2. Make the user enter the pin
3. If they match up, continue the ocde
4. If they dont, stop the code
5. When continuing, make a screen asking them what they want to do
6.Create 4 commands, one for checking your balance, one for depositing money, one for withdrawing money, one for exiting
7. For deopsiting and withdrawing, ask for ther amount of money to be deposited and withdrawn

'''

#ATM simulation


