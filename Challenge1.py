# """
# The goal was to output the True or False if the value of two numbers is equal to K.
# """

# # function to take in the values and return true
# def sum_of_two_numbers(list, k):
#     n = len(list)
#     for i in range(n):
#         for j in range(i+1, n):
#             if((list[i] + list[j]) == k):
#                 return list[i], list[j]
#     return None
        
# list = [10, 15, 3, 7]
# k=17
# print(sum_of_two_numbers(list, k))

def sum_of_two_numbers(lst):
    """
    Finds any two numbers in the list that add up to the same number.

    Args:
        lst (list): The list of numbers to search.

    Returns:
        tuple: A tuple containing the sum of the pair of numbers and a list of all pairs that add up to the same number,
        or None if no such pair is found.
    """
    pairs = []  # List to store pairs of numbers
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            current_sum = lst[i] + lst[j]  # Calculate the sum of the current pair
            existing_pair = next((pair for pair in pairs if pair[0] == current_sum), None)
            # Check if a pair with the same sum already exists in the pairs list
            if existing_pair is None:
                # If no pair exists, add the current pair to the pairs list
                pairs.append((current_sum, lst[i], lst[j]))
            else:
                existing_pair_numbers = (existing_pair[1], existing_pair[2])
                current_pair_numbers = (lst[i], lst[j])
                # Check if the current pair contains different numbers than the existing pair
                if current_pair_numbers != existing_pair_numbers:
                    # If different numbers, return the sum and both pairs
                    return current_sum, [existing_pair_numbers, current_pair_numbers]
    return None

numbers = [10, 15, 3, 2, 7]

result = sum_of_two_numbers(numbers)
if result:
    print(f"The number that the pairs add up to is: {result[0]}")
    for pair in result[1]:
        print(f"Pair: {pair[0]} and {pair[1]}")
else:
    print("No pair of numbers found that add up to the same number.")

