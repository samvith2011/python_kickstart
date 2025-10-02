'''Problem statement- Design a program that can tell the letter grade based on score.
reqirements:
90 and above- A
80-89-B
70-79-C
60-69-D
Below 60-F'''
#Creating function
def grader():
    grade = int(input("What is your grade as a #?\n"))
    if grade >=90 and grade <=100:
        print("This is your grade:")
        print("A")
        print("Amazing Work!")
    elif grade <=89 and grade >=80:
        print("This is your grade:")
        print("B")
        print("Good Job!")
    elif grade <= 79 and grade >= 70:
        print("This is your grade:")
        print("C")
        print("You barely passed!")
    elif grade <= 69 and grade >= 60:
        print("This is your grade:")
        print("D")
        print("Do better")
    elif grade <=59 and grade >= 0:
        print("This is your grade:")
        print("F")
        print("You failed")
    else:
        print("Enter an actual score")
#Code to call function

grader()


