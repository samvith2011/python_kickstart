
def driveage():
    userage = int(input("What is your age"))
    if userage < 18:
        print("You cannot drive")
    elif userage >= 18:
        print("You can drive")

driveage()