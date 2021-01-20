import math

'''
Input: a List of integers
Returns: a List of integers
'''

def product_of_all_other_numbers(arr):
    current_i = 0
    all_products = []
    product = 1

    for num in arr:
        for i in range(len(arr)):
            if current_i == i:
                pass
            else:
                product *= arr[i]
        all_products.append(product)
        current_i += 1
        product = 1
    return all_products


    # create empty array for single numbers
    # create empty array for products of numbers
    # iterate through array to get x
        # iterate through array again to get y
            # if x is equal to y
                # ignore
             # else
                # append numbers to array
        # find product of numbers in array and store in product variable
        # empty out nums array
        # append product variable to array

    # nums = []
    # products = []
    # for x in arr:
    #     for y in arr:
    #         if x == y:
    #             continue
    #         else:
    #             nums.append(y) 
    #     product = math.prod(nums)
    #     nums = []
    #     products.append(product)
    # return products
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
