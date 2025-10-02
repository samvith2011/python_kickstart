'''
1. Ask for number
2.use series of if then coditions to find out if it is a prime numer
3.Print resluts

(It only works in between 10-100)

'''



def primefinder():
    print("IMPORTANT: ONLY USE NUMBERS BETWEEN 10-100, AS THAT IS WHAT IT WAS DESIGNED FOR!!!!")
    prime_number = int(input("What number do you want to enter\n"))

    if prime_number / prime_number ==1:
        if prime_number / 1 == prime_number:
            if prime_number % 2 ==0 or prime_number % 3 ==0 or prime_number % 4 ==0 or prime_number % 5 ==0 or prime_number % 6 ==0 or prime_number % 7 ==0 or prime_number % 8 ==0 or prime_number % 9 ==0 or prime_number % 10 ==0:
                print("it is not a prime number\n")
            elif prime_number % 2 !=0 or prime_number % 3 !=0 or prime_number % 4 !=0 or prime_number % 5 !=0 or prime_number % 6 !=0 or prime_number % 7 !=0 or prime_number % 8 !=0 or prime_number % 9 !=0 or prime_number % 10 !=0:
                print("It is a prime number\n")
            elif prime_number == 2:
                print("it is a prime number")



primefinder()
