# DSA practice using LeetCode problem 217: Contains Duplicates (Easy)
################################################################
# Problem:
    # Given an integer array nums, return true if any value appears at 
    # least twice in the array, and return false if every element is distinct.
################################################################
# Initial thoughts:
    # We can solve this quickly using a hash map (dictionary)
################################################################
# Pseudocode:
    # seen = {}
    # for num in nums:
        # seen[num] = 0
    # if len(seen) != len(nums):
        # return true
    # else:
        # return false
################################################################
# Python Code:

def containsDuplicate(nums):
    seen = {}
    for num in nums:
        seen[num] = 0
    if len(seen)!= len(nums):
        return True
    
    return False



# Test Cases:
print(containsDuplicate([1,2,3,1]))  # Output: True
print(containsDuplicate([1,2,3,4]))  # Output: False
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # Output: True
print(containsDuplicate([1,2,3,4,5]))  # Output: False
print(containsDuplicate([0,1,2,3,4,5,6,7,8,9,10]))  # Output: False
print(containsDuplicate([1,1,1,1,1,1,1,1,1,1]))  # Output: True