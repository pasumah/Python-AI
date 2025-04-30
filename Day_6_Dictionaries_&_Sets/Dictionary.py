# Create a dictionary
person = {
    "name": "Mahesh",
    "age": 30,
    "city": "Madras"
}
print(person)

# Accessing values from the dictionary
print(person["name"])
print(person["age"])
print(person.get("age"))

# Adding and updating values
person["email"] = "mahesh@gmail.com"
person["age"] = 35

print(person)

# Removing a key-pair value
del person["city"]
print(person)

# looping through key-value pair or dictionary

for key, value in person.items():
    print(f"{key}: {value}")
