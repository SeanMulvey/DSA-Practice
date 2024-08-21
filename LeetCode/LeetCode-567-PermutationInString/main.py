# DSA practice using LeetCode problem 567: Permutation in string (Medium)
################################################################################################
# Problem:
    # Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
    # In other words, return true if one of s1's permutations is the substring of s2.
################################################################################################
# Initial Thoughts:
    # To solve this problem, I can sort s1 and then iterate through sections of s2 with a size of n
    # where n is the length of s1. If the sorted s1 matches the sorted section of s2 that we are looking at, return true.
    # If we reach the end of s2 without finding a match, we return false
################################################################################################
# Pseudocode:
    # s1 = sort(s1)
    # pointer = 0
    # end = len(s1)
    # while end <= length of s2:
        # builder = [pointer:end]
        # sorted_builder = sort(builder)
        # if sorted_builder == s1:
            # return true
        # pointer += 1
        # end += 1
    # return false
################################################################################################
# Python Code:

def checkInclusion(s1: str, s2: str) -> bool:
    s1 = ''.join(sorted(s1))
    pointer = 0
    end = len(s1)
    while end <= len(s2):
        builder = s2[pointer:end]
        sorted_builder = ''.join(sorted(builder))
        if sorted_builder == s1:
            return True
        pointer += 1
        end += 1
    return False

# Test Cases:
print(checkInclusion("ab", "eidbaooo"))  # Output: True
print(checkInclusion("ab", "eidboaoo"))  # Output: False
print(checkInclusion("hello", "ooolleh"))  # Output: True
print(checkInclusion("adc", "dcda"))  # Output: True
print(checkInclusion("a", "aa"))  # Output: True
print(checkInclusion("ab", "eidboaoo"))  # Output: False
                 