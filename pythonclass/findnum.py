list1 = [1,2,3,4,5]
check_for = 7

def findnum(list1,check_for):
    for num in list1:
        if check_for == num:
            print("Found")
            break
    if check_for != num:
        print("Not Found")

findnum(list1,check_for)