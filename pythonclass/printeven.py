list1 = [1,4,5,6,7,8]

def printeven(list1):
    evennum = []
    for item in list1:
        if item % 2 ==0:
            evennum.append(item)
        elif item % 2 !=0:
            continue
    print(evennum)

printeven(list1)