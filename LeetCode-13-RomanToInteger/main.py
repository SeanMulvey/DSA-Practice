# DSA practice using LeetCode problem 13: Roman to Integer (Easy)
##################################################################
#Problem:
    #Roman numerals are represented by seven different symbols: 
    # I, V, X, L, C, D and M.

    # Symbol       Value
    # I             1
    # V             5
    # X             10
    # L             50
    # C             100
    # D             500
    # M             1000
    # For example, 2 is written as II in Roman numeral, just two
    #  ones added together. 12 is written as XII, which is simply X + II.
    #  The number 27 is written as XXVII, which is XX + V + II.

    # Roman numerals are usually written largest to smallest from 
    # left to right. However, the numeral for four is not IIII. Instead, 
    # the number four is written as IV. Because the one is before the five we 
    # subtract it making four. The same principle applies to the number nine, 
    # which is written as IX. There are six instances where subtraction is used:

    # I can be placed before V (5) and X (10) to make 4 and 9. 
    # X can be placed before L (50) and C (100) to make 40 and 90. 
    # C can be placed before D (500) and M (1000) to make 400 and 900.
    # Given a roman numeral, convert it to an integer
##################################################################
# Initial Thoughts:
    # This could probably be brute forced by iterating through the chars of the string
    # and checking for the largest possible numeral and then checking if the preceding numeral
    # is smaller. If it is smaller, then based on the symbal read, I could subtract it from the total.
    # A better approach would be to match each roman numeral with a corresponding value in a dictionary
    # and iterate through the string from left to right, keeping a running total, unless the first numeral is smaller
################################################################
#Steps:
    # 1. Create a dictionary containing the roman numerals and their corresponding values.
    # 2. have a variable to keep track of the running total.
    # 3. Iterate through the string from left to right.
    # 4. If the current numeral is the last one in the string, add its value to the total.
    # 5. If the current numeral is smaller than the next one, subtract its value from the total.
    # 6. If the current numeral is larger than the next one, add its value to the total.
    # 7. Return the final total.
######################################################################
# Psuedocode:
    # converter = {numeral key: integer equiv value}
    # total = 0
    # for i = 0 until length of string:
        # if i + 1 < length of string:
            # if converter[string[i]] >= converter[string[i+1]]:
                # total += converter[string[i]]
            # else:
                # total -= converter[string[i]]
        # else:
            # total += converter[string[i]]

    # return total

#Python Code:

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    converter = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0

    for i in range(len(s)):
        if i + 1 < len(s):
            if converter[s[i]] >= converter[s[i+1]]:
                total += converter[s[i]]
            else:
                total -= converter[s[i]]
        else:
            total += converter[s[i]]
    return total
    
# Test the function
print(romanToInt('III'))  # Output: 3
print(romanToInt('IV'))  # Output: 4
print(romanToInt('IX'))  # Output: 9
print(romanToInt('LVIII'))  # Output: 58
print(romanToInt('MCMXCIV'))  # Output: 1994
print(romanToInt('MCMXC'))  # Output: 1990


# Time Complexity: O(n)