# created a while loop
number = 0
print("Entering while loop")
while number < 4:
    print("number:", number)
    number = number + 1
print("Left while loop")
print("number:", number)

print()

# created a while loop for the sum of all the numbers from 1-100
total = 0
num = 1
while num <= 100:
    total = total + num
    num = num + 1
print('The sum of all the numbers from 1 to 100 is', total)

print()

# created an infinite while loop that ends only if the user inputs "yes"
reply = ''
while reply != 'yes' :
    reply = input('Are we there yet? ')
print('Yeah!')

print()

# created a while loop and that figure outs error and askes the user to change his input
value = int(input("Please enter an integer greater than 0: "))
while value <= 0:
    print(value, "is not greather than 0")
    value = int(input("Please enter an integer greater than 0: "))
print(value)
