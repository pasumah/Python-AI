# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Accessing a list
print(fruits[0])
print(fruits[-1])

# Modifying a list
fruits[1] = "blueberry"
print(fruits)

# list operations
fruits.append("Orange")
fruits.remove("apple")
print(len(fruits))

# looping through a list
for fruit in fruits:
    print(fruit)
