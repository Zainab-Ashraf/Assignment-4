import random

DONE_LIKELIHOOD = 0.2  # Adjust this probability as needed

def done():
    #Returns True with a probability of DONE_LIKELIHOOD
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def chaotic_counting():
    count = 1
    while count <= 10 and not done():
        print(count)
        count += 1

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()