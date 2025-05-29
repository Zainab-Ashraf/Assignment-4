def in_range(n, low, high):
    #Returns True if n is between low and high, inclusive.
    return low <= n <= high

def main():
    # Example usage
    num = 5
    print(in_range(num, 1, 10))  # Expected output: True
    print(in_range(num, 6, 10))  # Expected output: False

if __name__ == '__main__':
    main()