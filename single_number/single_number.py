'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    count = {}
    for num in arr:
        if num not in count:
            count[num] = 1                      # adds a key value pair if the key didn't exist in the dictionary before, or changes the value if the key does exist
        else:
            count[num] += 1
    for num, frequency in count.items():        # unpacking key value pair
        if frequency == 1:
            return num

    # for num in count:
    #     if count[num] == 1:
    #         return num

    # .count is a linear method -- takes too long
    # for num in arr:
    #     if arr.count(num) == 1:
    #         return num


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")