list1 = [10,25,50,40,50]

def find2nd(list1):
    max = list1[0]
    for item in list1:
        if item > max:
            max = item


    c = list1.count(max)
    for i in range(c):
        list1.remove(max)





    max = list1[0]
    for item in list1:
        if item > max:
            max = item

    print(max)


find2nd(list1)