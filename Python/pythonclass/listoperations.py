'''print(Fruits)
print(Fruits[1])
for item in Fruits:
    print(item)'''



fruits = ["Kiwi","Banana","Apple","Clementine"]



#IndexB = fruits.index("Banana")
#fruits[IndexB] = "Blueberry"


def updatelist(fruits):
    for i in range(len(fruits)):
        if fruits[i] == "Apple":
            fruits[i] = "Orange"
    fruits.append("Raspberry")
    print(fruits)
#updatelist(fruits)

colors = ["red","green","blue","sky blue", "black"]

def slicingoperation(colors):
    #slice index 1 to 4
    print(colors[1:4])
    #slice from last index
    print(colors[::-1])
    #just slice with end range

slicingoperation(colors)