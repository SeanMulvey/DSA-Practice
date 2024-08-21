# DSA practice using LeetCode problem 20: Valid Parentheses (Easy)
################################################################################################
# Problem:
    # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine 
    # if the input string is valid. An input string is valid if:
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.
    # Every close bracket has a corresponding open bracket of the same type.
################################################################################################
# Thoughts:
    # I could use a stack data structure to keep track of the open brackets.
    # As I iterate through the string, I would push any open bracket onto the stack.
    # If I encounter a close bracket, I would pop the top open bracket from the stack.
    # If the stack is empty or the top open bracket does not match the current close bracket, then the string is not valid.
    # If I reach the end of the string and the stack is empty, then the string is valid.
#################################################################################################
# Steps:
    # Create an empty stack
    # Create a dictionary that links each closing symbol with its correlated opening symbol]
    # Iterate through the string
    # If the current character is an opening symbol, push it to the stack
    # If the current character is a closing symbol, Peek the top of the stack, if its the correlating open symbol, then pop and go to the next element
    # If the top is not the correlating open bracket, return False
    # After iterating through the lsit, check if the stack is empty
    # If its empty, return True
    # If the stack is not empty, return False
################################################################################################
# Psuedocode: 
    # stack = []
    # closing_brackets = {")":"(", "]":"[", "}":"{"}
    # for each char in string:
        # if stack and string[i] in closing_brackets:
            # if closing_brackets[string[i]] == stack.pop()
                # continue
            # else:
                # return False
        # else:
            # stack.push(string[i])
    # if stack:
        # return False
    # return True
################################################################################################
# Python Code:

def isValid(s):
    stack = []
    closing_brackets = {")":"(", "]":"[", "}":"{"}
    for char in s:
        if stack and char in closing_brackets:
            if closing_brackets[char] == stack.pop():
                continue
            else:
                return False
        else:
            stack.append(char)
    if stack:
        return False
    return True

# Test Cases:
print(isValid("()"))  # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))  # False
print(isValid("([)]"))  # False
print(isValid("{[]}"))  # True
print(isValid("([)]"))  # False
