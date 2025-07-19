'''print("samvith person".islower())
name = "Samvith"
print(name.lower())
print(len(name))
print("th" in name)
name = 'Samvith is cool'
print(name[7:])
done = "beau"

print(type(done) == bool)

if done:
    print("Yes")
else:
    print("No")

book_1_read = True
book_2_read = True

read_any_book = all([book_1_read,book_2_read])
print(read_any_book)


num1 = 2 +3j
num2 = complex(2,3)
print(num2.real,num2.imag)

print(round(5.49,))

from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(len(State))


age = input("What is your age ")
print("Your age is "+age)

condition = False
name = "Syd"

if condition == True:
    print("The condition")
    print("was true")

elif name == "Roger":
    print("Your name is roger")
elif name == "Syd":
    print("Your name is syd")

else:
    print("The cindition")
    print("Was false")

dogs = ["Roger",1,"Syd",True,"Quicny",7]

dogs[2] = "beau"
dogs.remove("Quicny")
print(dogs.pop())
print(dogs)
items = ["Roger","bob","Beau","Quincy"]

print(sorted(items,key=str.lower))
print(items)

#Tuples

names = ("Roger","Syd","Adam")
names[-1]
len(names)

print("Roger" in names)
names[0:2]
print(sorted(names))
newTuple = names + ""

#Dictionares

dog = {"name": "Roger","age": 8,"color":"green"}
dog["favorite food"] = "meat"

del dog['color']

dogcopy = dog.copy
print(dog)

set1 = {"Roger","Syd","Roger"}
set2 = {"Roger"}


print(list(set1))
#Functions


def test():
    age = 8
    print(age)

print(age)
test()

#Nested functions
def talk(phrase):
    def say(word):
        print(word)
    words = phrase.split(' ')
    for word in words:
        say(word)

talk('I am going to buy the milk')
def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()

count()'''
def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment

increment = counter()
print(increment())
print(increment())
print(increment())



