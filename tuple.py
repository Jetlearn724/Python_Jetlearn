Fruits = ("apple" , "banana","orange" )
print(Fruits)
print(Fruits[0])
for i in range(3):
    print(Fruits[i])
# unpacking 
fruit1 , fruit2 , fruit3 = Fruits 
print (fruit1,fruit2,fruit3)

# nested tuple
Food = (("Apple","banana"),("Mangojuice" , "chocolate shake"),("Burger","Pizza"))
print(Food[1][1])
print(Food[2][1])

#Slicing(Nmbers)
Pizza = (11,22,33,44,55,66,77,88)
print(Pizza[1:5])
print(Pizza[:])
print(Pizza[1:])
print(Pizza[:1])
print(Pizza[2:])
# changing the value
Pizza[3]=80
print(Pizza)