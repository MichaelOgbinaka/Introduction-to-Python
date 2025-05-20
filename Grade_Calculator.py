# Here I define a function that returns the letter grade for a numeric score
def grade(score):
    if score > 92:
        grade = "A"
    elif score > 89:
        grade = "A-"
    elif score > 85:
        grade = "B+"
    elif score > 82:
        grade = "B"
    elif score > 79:
        grade = "B-"
    elif score > 75:
        grade = "C+"
    elif score > 72:
        grade = "C"
    elif score > 69:
        grade = "C-"
    elif score > 65:
        grade = "D+"
    elif score > 62:
        grade = "D"
    elif score > 59:
        grade = "D-"
    else:
        grade = "F"
    return grade

# Here I define a function that returns true if the second number evenly divides the first
def evenly_divides(numerator, denominator):
    remainder = numerator % denominator
    return remainder == 0

# Here I define a function to get the first and last name from the user
def get_full_name():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    return first_name, last_name

# Here I test the grade function
score = int(input("Please enter a score: "))
print("Score:\t", score, "\t" , grade(score))

# Here I test the evenly_divides function
number_1 = int(input("First Number: "))
number_2 = int(input("Second number: "))

if evenly_divides(number_1, number_2):
    print(number_2, "evenly divides", number_1)
else:
    print(number_2, "does not evenly divide", number_1)

# Here I test the get_full_name function
fname, lname = get_full_name()
print("Hello", fname, lname)
