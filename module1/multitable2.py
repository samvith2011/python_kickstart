'''
Algorithm:
Create a loop with each of the numbers fom 1-5
Create loops inside the big loop for each digit
Print it
'''
def multitable2():
    for num in range(1,6):
        for i in range(1,11):
            temp = i * num
            print(f"{i} x {num} = {temp}")

multitable2()