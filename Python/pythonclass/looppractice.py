#1(For Loop)
'''or i in range(1, 6):
    print(i)'''
#2(For Loop)
'''colors =["red","green","blue"]
for color in colors:
    print(color)'''
#3
'''users = ["Alice","Bob","Charlie"]
for  users in users:
    print("Send email to",{users})'''
#1 (While loop)
'''count = 1
while count <=5:
    print(count)
    count += 1'''
#2(While loop)
'''user_input = input("What is your password")
password = "python123"

while user_input != password:
    print("Enter the password")
print("Access granted")
#3(While Loop)'''
#2(Edited)
user_input = input("What is your password")
password = "python123"

while user_input != password:
    user_input = input("What is your password")

print("Access granted")
#1(Examples)
'''for i in range(10):
    if i ==5:
        break
    print(i)'''
#2(Example)
'''for i in range(1,6):
    if i % 2 ==0:
        continue
    print(i)
#3(Example)
for i in range(5):
    if i ==3:
        pass#to be implemented later
    else:
        print(i)'''
