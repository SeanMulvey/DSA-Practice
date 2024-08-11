# DSA practice using leetCode problem 1: Two Sum (Easy)
##################################################################
#Problem:
    # Given an array of integers nums and an integer target, return 
    # indices of the two numbers such that they add up to target.
    # You may assume that each input would have exactly one solution, 
    # and you may not use the same element twice. You can return the
    #  answer in any order.
##################################################################
# Psuedocode:
    # get x and y for x + y = target
    # Compare all pairs and check if sum equals target
        # for i = 0 until length of nums:
            # for j = i + 1 until length of nums:
                # if nums[i] + nums[j] == target:
                    # return [i, j]
###################################################################

# Python Code:

def two_sums(nums,target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# Test the function
print(two_sums([2, 7, 11, 15], 9))  # Output: [0, 1]
print(two_sums([3, 2, 4], 6))  # Output: [1, 2]
print(two_sums([3, 3], 6))  # Output: [0, 1]
print(two_sums([0, 0, 3, 4], 0))  # Output: [0, 3]
print(two_sums([3, 2, 3], 6))  # Output: [0, 2]
print(two_sums([1, 2, 3, 4, 5, 6, 7, 8, 9], 15))  # Output: [4, 8]


# Note:
    # This solution has a time complexity of O(n^2) due to the nested loops.
    # We can make this O(n) by removing one of the loops.
    # How would I do this?
    ################################
    # The previous formula we used was solving for x and y by brute forcing the list
    # and checking for all pairs.
    # Instead, we can solve for just 1 variable by changing the formula:
    # Old formula: x + y = target
    # New Formula: y = target - x
    ################################
# Psuedocode for improved solution:
    # solve for y = target - x
    # create a dictionary of value as key and index as value
    # iterate through collection
    # if target - x is in dictionary, return x and value of target - x
    # if target - x is not in dictionary, add x and its index to dictionary
     # seen = {}
     # for i = 0 until length of nums:
     #     if nums[i] in seen:
     #         return [seen[target - nums[i]], i]
     #     add nums[i] to seen
    

    # Python Code for improved solution:

def better_two_sums(nums, target):
    seen = {}
    for i in range(len(nums)):
        x = target - nums[i]
        if x in seen:
            return [seen[x], i]
        else:
            seen[nums[i]] = i

# Test the function
print('Better: ',better_two_sums([2, 7, 11, 15], 9))  # Output: [0, 1]
print('Better: ',better_two_sums([3, 2, 4], 6))  # Output: [1, 2]
print('Better: ',better_two_sums([3, 3], 6))  # Output: [0, 1]
print('Better: ',better_two_sums([0, 0, 3, 4], 0))  # Output: [0, 3]
print('Better: ',better_two_sums([3, 2, 3], 6))  # Output: [0, 2]
print('Better: ',better_two_sums([1, 2, 3, 4, 5, 6, 7, 8, 9], 15))  # Output: [4, 8]