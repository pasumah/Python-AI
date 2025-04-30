# Create a list of 5 numbers.
numbers = [1, 2, 3, 4, 5]
# Add a number to the list.
numbers.append(6)
# Replace the 2nd number with something else.
numbers[1] = 7

print(numbers)
# Loop through the list and print only even numbers.
for number in numbers:
    if number % 2 == 0:
        print(number)

# Bonus: Create a tuple of your 3 favorite colors and print each one.
colors = ("red", "blue", "white")
print(colors[0])
print(colors[1])
print(colors[2])
