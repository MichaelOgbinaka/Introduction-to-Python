# Here I demonstrate how lists are referenced in Python
numbers = [1, 2, 3, 4, 5]
print("numbers:\t", numbers)
numbers_2 = numbers
print("numbers_2:\t", numbers_2)
numbers.append(6)
print("numbers:\t", numbers)
print("numbers_2:\t", numbers_2)
numbers_2.append(7)
print("numbers:\t", numbers)
print("numbers_2:\t", numbers_2)
print()

# Here I define a function that reads integers from a file into a list
def read_integers_into_list(filename):
    file = open(filename, "r")
    new_list = []
    for line in file:
        number = int(line)
        new_list.append(number)
    file.close()
    return new_list

# Here I define a function that returns the average of a list of numbers
def average_list(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    return total / len(list)

# Here I define a function that counts entries above a certain value
def entries_above(list, value):
    number_above = 0
    for i in range(len(list)):
        if list[i] > value:
            number_above += 1
    return number_above

# Here I use the functions to analyze temperature data
temps = read_integers_into_list("temperatures.txt")
print("Temperature list:", temps)
average = average_list(temps)
print("Average:\t", average)
print("Days above average:", entries_above(temps, average))
