# Write a program that asks the user to enter 3 names, and then displays the
# names sorted in ascending order. For example, if thee user entered "Charlie", 
# "Leslie" and "Andy", the program would display: Andy, Charlie, Leslie

# variables
name_one = input("Please enter name one.\n").lower()

name_two = input("Please enter name two.\n").lower()

name_three = input("Please enter name three.\n").lower()

# opening message
print("Thank you! Here are the names in alphabetical order.")

# sort the names if name_one is first
if (name_one < name_two and name_one < name_three):
    print(name_one)
    if (name_two < name_three):
        print(name_two)
        print(name_three)
    else:
        print(name_three)
        print(name_two)

if (name_two < name_one and name_two < name_three):
    print(name_two)
    if (name_one < name_three):
        print(name_one)
        print(name_three)
    else:
        print(name_three)
        print(name_one)

if (name_three < name_one and name_three < name_two):
    print(name_three)
    if (name_one < name_two):
        print(name_one)
        print(name_two)
    else:
        print(name_two)
        print(name_one)








