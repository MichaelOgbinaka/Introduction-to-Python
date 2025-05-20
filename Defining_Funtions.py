# Here I define a function to safely open files for reading
def open_file_read(filename):
    try:
        file = open(filename, "r")
        return file
    except:
        print("Cannot open " + filename)

# Here I create a function to read integers from a file into a list
def int_list_from_file(file):
    list = []
    for line in file:
        number = int(line)
        list.append(number)
    return list

# Here I calculate the average of numbers in a list
def list_average(list):
    total = 0
    for num in list:
        total += num
    return round(total / len(list), 2)

# Here I use the functions to read numbers and calculate their average
file = open_file_read("numbs.txt")
numbs = int_list_from_file(file)
print(list_average(numbs))
