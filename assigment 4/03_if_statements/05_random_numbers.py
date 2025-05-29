import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    #You should write your code here. Make sure to delete 
    # the 'pass' line before starting to write your own code.

    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    print(random_numbers)

if __name__ == '__main__':
    main()