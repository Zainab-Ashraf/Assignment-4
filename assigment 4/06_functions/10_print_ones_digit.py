def print_ones_digit(num):
    # Extract and print the ones digit using modulo operator
    print("The ones digit is", num % 10)

def main():
    # Get user input and convert it to an integer
    num = int(input("Enter a number: "))
    print_ones_digit(num)

# Call the main function to start the program
if __name__ == '__main__':
    main()