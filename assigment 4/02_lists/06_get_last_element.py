def get_last_element(lst):
    if lst:
        return lst[-1]
    else:
        return None

# Example usage
my_list = [1, 2, 3, 4, 5]
last_element = get_last_element(my_list)
print("The last element is:", last_element)