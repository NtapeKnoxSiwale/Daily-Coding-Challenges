"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is
the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

# function
def product_array_except_self_method1(array):
    # count the numberss in the given array
    n = len(array)
    # init an n array for the result
    result_array = [0] * n
    # compute the product of the array
    total_product = 1

    for num in array:
        total_product *= num

    for i in range(n):
        # product except the i
        result_array[i] = total_product // array[i]

    return result_array

# # test arrays
# array = [1, 2, 3, 4, 5]
# #array = [3, 2, 1]

# # print
# result = product_array_except_self_method1(array)
# print(f"The array: {array}")
# print(f"The result: {result}")

"""
Follow-up: what if you can't use division?
"""

# different method
def product_array_except_self_method2(array):
    n = len(array)
    result_array = [1] * n

    left_product = 1
    for i in range(n):
        result_array[i] *= left_product
        left_product *= array[i]

    right_product = 1
    for i in range(n-1, -1, -1):
        result_array[i] *= right_product
        right_product *= array[i]

    return result_array

# test arrays
array = [1, 2, 3, 4, 5]
#array = [3, 2, 1]

# print
result = product_array_except_self_method2(array)
print(f"The array: {array}")
print(f"The result: {result}")