'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # create a max array to store each max value
    # create current_i = 0
    # iterate through the array
        # create window variable -- nums[current_i:k]
        # find max value in the window
        # append max value to max array
        # increment current index
        # increment k
    # return max array

    max_arr = []
    current_i = 0
    while k <= len(nums):
        window = nums[current_i:k]
        max_value = max(window)
        max_arr.append(max_value)
        current_i += 1
        k += 1
    return max_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
