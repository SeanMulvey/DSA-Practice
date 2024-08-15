# DSA practice using LeetCode problem 344: Reverse String (Easy)
##################################################################
# Problem:
    # Write a function that reverses a string. The input string is given as an array of characters s.

    # You must do this by modifying the input array in-place with O(1) extra memory.
##################################################################
#Steps:
    # iterate through the string from the start to the middle
    # swap the characters at the start and end indices
    
# Psuedocode:
    # for i from 0 to half of the length of the string:
    # swap s[i] and s[length -  i - 1]
##################################################################
#Python Code:
def reverseString(s):
    # iterate through the string from the start to the middle (half of the length)
    # We use len(s) // 2 instead of len(s) / 2 to round down to the nearest integer instead of getting a float
    for i in range(len(s) // 2):
        # swap the characters at the start and end indices
        # Python's tuple unpacking feature allows us to swap values in a single line of code
        # This is more efficient than using a temporary variable to store the value at the start index before swapping it with the value at the end index
        # The comma after s[i] ensures that the assignment operation is performed on the left side of the assignment operator (the start index)
        # The comma after s[len(s) - i - 1] ensures that the assignment operation is performed on the right side of the assignment operator (the end index)
        # The assignment operation is performed on the tuple s[i], s[len(s) - i - 1] simultaneously, effectively swapping the values at the start and end indices in one line of code
        # The result of the assignment operation is not stored in any variable, so it is not needed to assign it to a new variable
        ##############################################################################################
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
        #NOTE: A really cool feature of Python is we can get the mirrored element of a list in one line of code using negative indices
        # Instead of s[i], s[len(s) - i - 1] = s[-i - 1], s[i]
        # We could do s[i], s[~i] = s[~i], s[i] to do the same thing
        # The ~ operator in Python gives the negative index of the given index, so it effectively reverses the list
        # For example, if i = 0 and s[i] = s[0], then s[~i] = s[-1] which is the same as s[len(s) - 1]



# Test the function
s = ['h', 'e', 'l', 'l', 'o']
reverseString(s)
print(s)  # Output: ['o', 'l', 'l', 'e', 'h']

s = ['A', 'B', 'C', 'D', 'E']
reverseString(s)
print(s)  # Output: ['E', 'D', 'C', 'B', 'A']