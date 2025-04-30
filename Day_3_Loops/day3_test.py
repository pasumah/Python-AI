# Write a Python program that prints numbers from 1 to 10, but skips 5 and stops at 8.
# # Example Output:
# # 1
# # 2
# # 3
# # 4
# # 6
# # 7
# # 8

for i in range(1, 10):
    if i == 5:
        continue
    elif i == 9:
        break
    print(i)
