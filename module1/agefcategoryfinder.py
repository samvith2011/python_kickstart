def agegroupfinder():
    age = int(input("How old are you\n"))

    #check edge case
    if age<=0:
        print("Please enter correct age")
    if age <= 12:
        print("You are a child")
    elif age <= 19 and age >= 13:
        print("You are a teen")
    elif age <= 100 and age >= 20:
        print("You are an adult")
    else:
        print("Amazing! you are more that 100 years old")


agegroupfinder()

