def primefinder2():
    number_input = int(input("What number do you want to enter\n"))

    n = 2
    prime = False
    while True:
        if number_input % n != 0:
            prime = True
        else:
            prime = False
            break
        n += 1
        if number_input / 2 <= n:
            break
    print (number_input,"is prime is : ", prime)


primefinder2()