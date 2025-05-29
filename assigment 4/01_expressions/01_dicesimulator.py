import random  # ✅ Required for random number generation

NUM_SIDES = 6  # ✅ Number of sides on a standard die

def roll_dice():
    """Function to roll two dice and display their results."""
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {total}")

def main():
    """Main function to roll dice multiple times."""
    die1 = 10  # ✅ This variable is separate from roll_dice()
    print(f"die1 in main() starts as {die1}")

    for _ in range(3):  # ✅ Rolls the dice three times
        roll_dice()
    
    print(f"die1 in main() is still {die1}")  # ✅ Shows die1 remains unchanged

if __name__ == "__main__":
    main()  # ✅ Calls the main function to run the simulator
