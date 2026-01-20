# Task 4: Loops & Iterations
# Python Developer Internship

print("1. For loop: Print numbers from 1 to 100")
for i in range(1, 101):
    print(i, end=" ")
print("\n")

print("2. While loop: Countdown Timer")
count = 10
while count > 0:
    print("Countdown:", count)
    count -= 1
print("Time's up!\n")

print("3. Break and Continue Example")
for i in range(1, 11):
    if i == 5:
        print("Breaking the loop at", i)
        break
    if i == 3:
        print("Skipping", i)
        continue
    print("Number:", i)
print()

print("4. Iterating over a string")
name = "Python"
for ch in name:
    print(ch)
print()

print("5. Multiplication Table of 5")
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()

print("6. Range with steps (Even numbers from 2 to 20)")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")

print("7. Loop with condition (Find numbers > 50)")
for i in range(40, 61):
    if i > 50:
        print(i)
print()

print("8. Real-world Example: Checking attendance")
students = ["Ravi", "Anu", "Kiran", "Sita"]
for student in students:
    print(student, "is present")