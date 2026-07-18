# Programe .01
# Print Numbers

print("==== Print Number ==== ")

for number in range(1,11):
    print(number)

# Programe .02
# Multiplication Table

print("==== Multiplication Table ====")

number = int(input("Enter a number:"))

for i in range(1,11):
    print(f"{number}x {i} = {number * i}")

# Programe .03
# Sum of Numbers

print("==== Sum of Numbers ====")
total = 0
for i in range(1,6):
    total += i

print("Total =",total)