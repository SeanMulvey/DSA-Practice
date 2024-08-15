# DSA practice using LeetCode problem 520: Detect Capital (Easy)
##################################################################
# Problem:
    # We define the usage of capitals in a word to be right when one of the following cases holds:
    # All letters in this word are capitals, like "USA".
    # All letters in this word are not capitals, like "leetcode".
    # Only the first letter in this word is capital, like "Google".
    # Given a string word, return true if the usage of capitals in it is right.
###################################################################
# Initial Thoughts: 
    # There is a couple of different ways we can go about this problem.
    # We can have a collection of all uppercase letters and check if each character in the string is in that collection.
    # We check for a scenario where the first letter is capitalized and all other letters are not, if true we return true
    # We then check if all letters are capital, if true we return true
    # We then check if there are no capital letters, if true we return true
    # If none of these scenarios hold true, we return false
    ##################################################################
    # I think a better way to do this might be the is upper() function in Python
    # We have a variable to see if the first letter is capitalized
    # While also having a counter to keep track of the amount of capital letters we've seen
    # We iterate through each character and if there is more than one capital but capital count doesn't match length we return false
    # If capital count is 1 we check if it was the first character and if it was we return true, if not we return false
    # If capital count is 0 we return true
######################################################################
#Psuedocode:
    #capCount = 0
    # isFirst = False
    # for i = 0 to length of word:
        # if word[i] is uppercase and i == 0:
            # isFirst = True
            # capitalCount += 1
        # elif word[i] is uppercase:
            # capitalCount += 1
    # if capitalCount == 0:
        # return True
    # elif capitalCount == 1 and isFirst:
        # return True
    # elif capitalCount == len(word):
        # return True
    # else:
        # return False
    # return True
######################################################################

def detectCapitalUse(word):
    capCount = 0
    isFirst = False
    for i in range(len(word)):
        if word[i].isupper() and i == 0:
            isFirst = True
            capCount += 1
        elif word[i].isupper():
            capCount += 1
    if capCount == 0:
        return True
    elif capCount == 1 and isFirst:
        return True
    elif capCount == len(word):
        return True
    else: 
        return False
    return True

# Test the function
print(detectCapitalUse("USA"))  # Output: True
print(detectCapitalUse("FlaG"))  # Output: False
print(detectCapitalUse("leetcode"))  # Output: True
print(detectCapitalUse("Google"))  # Output: True
print(detectCapitalUse("LEETcode"))  # Output: False
print(detectCapitalUse("I"))  # Output: True


#NOTE: After looking at solutions, I learned that Python has a built in capitalize() function that capitalizes the first letter of the string.
# Using this we could simplify the function to:
#if word.upper() == word:
    # return True
# if word.lower() == word:
    # return True
# if word.capitalize() == word:
    # return True
#return false

# With my current understanding of time complexity, I believe this solution is less efficient because if I'm understanding the processes correctly, the built-in capitalize(), upper(), and lower() will each iterate through the entire string while my current solution iterates through the string only once.

