# Here I created lists to demonstrate various list operations in Python
days = ["Sunday", "Monday", "Tuesday", "Wednesday"]
days += ["Thursday", "Friday", "Saturday"]
# Here I use the tab function "\t" to create a tab before the variable
print("days:\t\t", days)
weekdays = days[1:6]
print("weekdays:\t", weekdays)
daynames = days[:]
print("daynames:\t", daynames)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("digits:\t\t", digits)
even_digits = digits[1:2]
print("even_digits:\t", even_digits)
print()

# Here I demonstrate checking if items are in the list
print("1 in digits:\t", 1 in digits)
print("'foo' in digits:", 'foo' in digits)
print()

# Here I create a numbers list and demonstrate various list methods
numbers = [1, 2, 3, 4, 5]
print("numbers:\t", numbers)
numbers.append(6)
print("numbers:\t", numbers)
print("numbers.index(6):", numbers.index(6))
numbers.insert(0, 0)
print("numbers:\t", numbers)
numbers.remove(0)
print("numbers:\t", numbers)
numbers.reverse()
print("numbers:\t", numbers)
numbers.sort()
print("numbers:\t", numbers)
del numbers[5]
print("numbers:\t", numbers)
# Here I use built-in functions to find min and max values
print("min(numbers):", min(numbers))
print("max(numbers):", max(numbers))