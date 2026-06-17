list1 = [1,2,3,4,5,6]
even = []
odd = []
def evenodd(list1):
    for item in list1:
        if item % 2 ==0:
            even.append(item)
        elif item % 2 !=0:
            odd.append(item)
    print("Even->",even,",","Odd->",odd)


evenodd(list1)