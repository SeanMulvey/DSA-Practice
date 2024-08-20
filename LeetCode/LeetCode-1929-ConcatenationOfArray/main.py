# DSA practice using LeetCode problem 1929: Concatenation of Array (Easy)
########################################################################
# Problem:
    # Given an integer array nums of length n, you want to create an array 
    # ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] 
    # for 0 <= i < n (0-indexed). Specifically, ans is the concatenation 
    # of two nums arrays. Return the array ans.
########################################################################
# Initial Thoughts:
    # This question seemed a bit too straight forward after reading the problem
    # and looking at the example output.
    # I ended up just creating an array that was a copy of nums and appended
    # each element of nums to ans.
########################################################################
# Pseudocode:
    # ans = []
    # ans = nums
    # for num in nums:
        # ans.append(num)
    # return ans

def getConcatenation(nums):
    ans = []
    ans = nums
    for i in range(len(nums)):
        ans.append(nums[i])
    return ans

# Test the function
nums = [1,2,3]
print(getConcatenation(nums))  # Expected output: [1, 2, 3, 1, 2, 3]

nums = [1]
print(getConcatenation(nums))  # Expected output: [1, 1]

# NOTE: Maybe there's a way to optimize this solution to O(1) or something, because it seems too easy (Maybe its just meant to be this easy, idk :/)