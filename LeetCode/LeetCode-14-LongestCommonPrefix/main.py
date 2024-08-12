# DSA Practice using LeetCode problem 14: Longest Common Prefix (Easy)
##################################################################
# Problem:
    # Write a function to find the longest common prefix string amongst an array of strings.
    # If there is no common prefix, return an empty string "".
##################################################################
# Initial Thoughts:
    # We need to find an effecient way to check each character in a string until we find a difference in one string.
    # A quick solution would be to iterate through a single string and compare it to the charactars in the other strings.
    # I'm not sure if this will be the most effecient solution because the time complexity would be O(n*m), where n is 
    # the length of the longest string and m is the number of strings in the array.
    # Lets go ahead and implement this and see if we can find optimizations later.
##################################################################
# Steps:
    # 1. Create a variable where we will add characters that are part of the common prefix.
    # 2. Get the first char of the first string 
    # 3. Compare it with the first char of all other strings.
    # 4. If they are the same, add it to the common prefix and move on to the next character.
    # 5. If they are not the same, return the common prefix.

# Python Code:

def longestCommonPrefix(collection):
    if collection == []:
        return ""
    prefix = ""
    str = collection[0]

    for i in range(len(str)):
        for word in collection[1:]:
            if i >= len(word) or str[i]!= word[i]:
                return prefix
        prefix += str[i]
    return prefix

    return prefix

# Test the function
print(longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog","racecar","car"]))  # Output: ""
print(longestCommonPrefix(["dog","dogdog","dogdogdog"]))  # Output: "dog"
print(longestCommonPrefix(["apple","banana","cherry"]))  # Output: ""
print(longestCommonPrefix(["flower","flow","flight","flying"]))  # Output: "fl"
print(longestCommonPrefix(["flower","flow","flight","flying","fly"]))  # Output: "fl"
print(longestCommonPrefix(["flower","flower","flower"]))  # Output: "flower"
    
            



