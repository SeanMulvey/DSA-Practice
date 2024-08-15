# DSA practice using LeetCode Problem 557: Reverse Words in a String III (Easy)
################################################################################
#Problem:
    #Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
# Example 1:
    # Input: s = "Let's take LeetCode contest"
    # Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:
    # Input: s = "Mr Ding"
    # Output: "rM gniD"
# Constraints:
    # 1 <= s.length <= 5 * 104
    # s contains printable ASCII characters.
    # s does not contain any leading or trailing spaces.
    # There is at least one word in s.
    # All the words in s are separated by a single space.
################################################################################
# Initial Thoughts: 
    # Maybe we could iterate over the string and create substrings based on the whitespaces separating the characters
    # we would then reverse each substring
    # and concat them together in the same order
#################################################################################
# Steps:
    # Have a string builder variable that adds characters until we hit a white space
    # Once a white space is hit, we take the substring, reverse its order and add it to a new string that we will return when finished
    # We then continue iterating and doing the same process throughout the rest of the string 
##################################################################################
#Pseudocode:
    # newString = ""
    # stringBuilder = ""
    # for i = 0 until string length:
        #if string[i] != ' ':
            #stringBuilder += string[i]
        #else:
            #newString += stringBuilder.reverse() + ' '
        #stringBuilder = ""
    # return newString
#####################################################################################
# Python Code:
def reverseWords(str):

    newString = ""
    stringBuilder = ""
    for i in range(len(str)):
        
        if str[i] != ' ':
            stringBuilder += str[i]
        else:
            newString += stringBuilder[::-1] + ' '
        stringBuilder = ""
    return newString


# Test the function


print(reverseWords("Let's take LeetCode contest"))  # Output: "s'teL ekat edoCteeL tsetnoc"
