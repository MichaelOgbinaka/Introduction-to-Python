# Here I define a function to safely open files with error handling
def open_file_read():
    while True:
        filename = input("Filename: ")
        try:
            file = open(filename, "r")
            return file
        except FileNotFoundError:
            print("Cannot find", filename)
        except PermissionError:
            print("You do not have permission to read", filename)

# Here I process temperature data from the file
file = open_file_read()
count = 0
total = 0
max  = -100
min  = 200

# Here I read each line and calculate statistics
for line in file:
    count += 1
    date, temp = line.split()
    temp  = int(temp)
    total += temp
    if temp > max:
        max = temp
    if temp < min:
        min = temp

# Here I calculate and display the results
average = round(total/count, 2)
print("Average:\t", average)
print("Maximum:\t", max)
print("Minimum:\t", min)
