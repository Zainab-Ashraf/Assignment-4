# Ask the user to enter a number
curr_value = int(input("Enter a number: "))

# Double the number until the value is 100 or greater
while curr_value < 100:
    curr_value = curr_value * 2
    print(curr_value)