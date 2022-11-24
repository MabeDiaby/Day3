# if else statements:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

# Nested if statements
# if elif statements
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print(f"Please pay ${bill}.")
    elif age <= 18:
        bill = 7
        print(f"Please pay ${bill}.")
    else:
        bill = 12
        print(f"Please pay ${bill}.")
    photo = input("do you whant a photo? y or n.")
    if photo == "y":
        bill += 3
    print(f"Your Final bill is ${bill}")
else:
    print("Too short to ride")


