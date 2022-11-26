# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true = ['t', 'r', 'u', 'e']
love = ['l', 'o', 'v', 'e']
count1 = 0
count2 = 0

trueCombined = name1 + name2

for i in trueCombined.lower():
    if str(i) in true:
        count1+= 1
# for y in name2.lower():
#     if str(y) in true:
#         count1+= 1
for i in trueCombined.lower():
    if str(i) in love:
        count2+= 1
# for y in name2.lower():
#     if str(y) in love:
#         count2+= 1
total = str(count1) + str(count2)
total = int(total)
if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >=40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")