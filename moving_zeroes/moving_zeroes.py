'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # create a left and right pointer - use index numbers
    # iterate through array as long as left is equal to right (we don't want our pointers to cross)
        # if left pointer is at 0 and the right pointer is not at 0
            # swap pointers
            # move left pointer up by one
            # move right pointer down by one
        # else
            # if number at left pointer is not 0
                # move left pointer up by 1
            # if number at right pointer is at 0
                # move right pointer down by 1
       # return array

    left = arr[0]
    right = len(arr) - 1

    while left <= right:
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        else:
            if arr[left] != 0:
                left += 1
            if arr[right] == 0:
                right -= 1
    return arr

    # This solution doesn't work -->
    # for i in range(len(arr)):
    #     if arr[i] == 0:
    #         # arr[i], arr[-1] = arr[-1], arr[i]
    #         removed = arr.pop(arr[i])
    #         arr.append(removed)
    # return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    # arr = [0, 3, 1, 0, -2]
    arr = [1, 2, 3, 0, 4, 0, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")