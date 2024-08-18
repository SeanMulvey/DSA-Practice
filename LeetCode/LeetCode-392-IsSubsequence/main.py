# DSA practice using LeetCode Problem 392: Is Sequence (Easy)
########################################################################################################
# Problem:
    # Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
    # A subsequence of a string is a new string that is formed from the original string by deleting 
    # some (can be none) of the characters without disturbing the relative positions of the remaining 
    # characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
########################################################################################################
# Initial Thoughts:
    # Maybe I could take s and search for the first character and if theres a match in t, continue from that 
    # point for the second character of s in t, then from that point for the third character in t, etc.
    # Once I reach the end of t, I can check to see if all of the characters in s were matched. If they were
    # I would return true, if not I would return false.
########################################################################################################
# Steps:
    # 1. Create a variable to store the matched characters of s
    # 2. Iterate through each character in s
    # 3. If the current character in s matches the current character in t, add it to the matched characters
    # 4. Save the current index of t where we found the matched characters
    # 5. Continue to iterate through t for the next character in s
    # 6. After reaching the end of t, check to see if all characters in s were matched
    # 7. If they were, return true, if not return false 
########################################################################################################
# Pseudocode:
    # matched_chars = ""
    # i = 0
    # foreach character in s:
    #     if i is less than length of t:
    #         if current_character_of_s equals t[i]:
    #           add t[i] to matched_chars
                # if matched_chars equals s:
                    # return True
    #         i += 1
    # return False
##########################################################################################################
# Python Code:

def is_subsequence(s,t):
    matched_chars = ""
    start = 0
    for i in range(len(s)):
        if s[i] not in t:
            return False
        for j in range(start,len(t)):
            if s[i] == t[j]:
                matched_chars += t[j]
                start = j + 1
                break
    if matched_chars == s:
            return True


# Test the function
print(is_subsequence("", "ahbgdc"))  # Output: True
print(is_subsequence("axc", "ahbgdc"))  # Output: false
print(is_subsequence("axc", "ahbgdcx"))  # Output: False
print(is_subsequence("axc", "ahbgdcxa"))  # Output: True
print(is_subsequence("axc", "ahbgdcxaxc"))  # Output: True
print(is_subsequence("axc", "ahbgdcxaxca"))  # Output: False