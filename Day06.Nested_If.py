# Day 06 - Nested if statement

print("==== student Admission Checker ====")
age = int(input("Enter your  age:"))
marks = int(input("Enter your marks:"))

if age >= 18:
    if marks >= 60:
        print("Congratulations! You are eligible for admission.")
    else:
        print("Sorry! You marks are too low.")
else:
    print("Sorry! You are underage.")