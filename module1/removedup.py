list1 = [2,3,2,5,3,6]
unique = []
def unique1(list1,unique):
    for item in list1:
        if item in unique:
            continue
        else:
            unique.append(item)


    print(unique)


unique1(list1, unique)