# DSA practice using Leet Code problem 27: Remove Element (Easy)
################################################################
# Problem:
    # Given an integer array nums and an integer val, remove all occurrences 
    # of val in nums in-place. The order of the elements may be changed. Then 
    # return the number of elements in nums which are not equal to val.
    # Consider the number of elements in nums which are not equal to val be k, 
    # to get accepted, you need to do the following things:
    # Change the array nums such that the first k elements of nums contain the 
    # elements which are not equal to val. The remaining elements of nums are not 
    # important as well as the size of nums.
    # Return k.
################################################################
# Thoughts: 
    # I initially spent a lot of time trying to solve this by checking if nums[i] = val
    # But when watching an explanation of the solution, they explained that we are checking if nums[i] is not val
    # After realizing that, I immediately went back and tried to solve the problem that way and it worked
################################################################
# Steps:
    # Create a pointer index to keep track of the current place to shift the values to
    # Iterate through the array from the start to the end
    # If the current element is not equal to val, shift it to the current position and increment the pointer index
    # Once we reach the end of the array, the pointer index will be the number of elements that are not equal to val
    # Return the pointer index

def removeElement(nums, val):
    # Create a pointer index to keep track of the current place to shift the values to
    index = 0

    # Iterate through the array from the start to the end
    for i in range(len(nums)):
        # If the current element is not equal to val, shift it to the current position and increment the pointer index
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1

    # Return the pointer index, which will be the number of elements that are not equal to val
    return index

# Test the function
nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))  # Expected output: 2
print(nums)  # Expected output: [2, 2]

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(removeElement(nums, val))  # Expected output: 5
print(nums)  # Expected output: [0, 1, 3, 0, 4]