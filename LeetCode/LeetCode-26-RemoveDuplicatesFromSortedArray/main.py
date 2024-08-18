# DSA practice using LeetCode problem 26: Remove duplicates from sorted array (Easy)
######################################################################################
# Problem:
    # Given an integer array nums sorted in non-decreasing order, remove the 
    # duplicates in-place such that each unique element appears only once. 
    # The relative order of the elements should be kept the same. Then return 
    # the number of unique elements in nums. Consider the number of unique 
    # elements of nums to be k, to get accepted, you need to do the following 
    # things:
    # Change the array nums such that the first k elements of nums contain 
    # the unique elements in the order they were present in nums initially. 
    # The remaining elements of nums are not important as well as the size of nums.
    # Return k.
######################################################################################
# Initial Thoughts:
    # I need to iterate through the array and remove the duplicates
    # Because I have to do this in-place, we can't create a new array
    # We have to shift the values of the array to override the duplicates
    # What do I need to know to do this?:
        # I need a way to check if its a duplicate
            # Because the array is ordered, I can check if the value is duplicate by checking the value before it
        # I have to know where to shift the next unique value
            # I can do this by having a pointer variable that saves the location of the last shifted index so we know there's an "open" spot there
        # I need to know the count of unique elements
            # This can be tracked with the pointer variable
######################################################################################
# Pseudocode:
    # p = 1
    # for i = 1 until end of nums:
        # if nums[i] != nums[i - 1]
            #nums[p] == nums[i]
            # p += 1
    # return p

def removeDuplicates(nums):
        # p is used as a pointer to the last shifted index that we will move the next unique value to
        p = 1
        # Iterate through the list starting at 1 since we will never be changing nums[0]
        for i in range(1,len(nums)):
            # If the current value is not equal to the previous value, move the current value to the next unique index and increment p
            if nums[i] != nums[i - 1]:
                nums[p] = nums[i]
                p += 1
        return p


# Test the function
nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print(removeDuplicates(nums))  # Expected output: 5

