# Write a Python program that asks for a number and tells if it’s positive, negative, or zero.#
# Example Output:
# Enter a number: -5
# The number is negative.

score = int(input("Enter your score: "))

if score >= 10:
    print("The number is Positive.")
elif score < 0:
    print("The number is Negative.")
elif score == 0:
    print("The number is Zero.")
else:
    print("The number is not a number.")
