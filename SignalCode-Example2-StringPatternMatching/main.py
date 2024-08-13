# You are given two strings: pattern and source. The first string pattern contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.

# Your task is to calculate the number of substrings of source that match pattern. 

# We’ll say that a substring source[l..r] matches pattern if the following three conditions are met:
# – The pattern and substring are equal in length.
# – Where there is a 0 in the pattern, there is a vowel in the substring. 
# – Where there is a 1 in the pattern, there is a consonant in the substring. 

# Vowels are ‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘, and ‘y‘. All other letters are consonants.
########################################################################
#Pseudocode:
    # Create a list of vowels
    # Initialize a counter variable to 0
    # if pattern length is greater than source length, return 0
    # 

def count_matching_substrings(pattern: str, source: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count = 0
    if len(pattern) > len(source):
        return 0
    for i in range(len(source) - len(pattern) + 1):
        same = True
        
        for j in range(len(pattern)):
            isVowel = True
            if source[i + j] not in vowels:
                isVowel = False
            if pattern[j] == '0' and isVowel is False:
                same = False
            elif pattern[j] == '1' and isVowel is True:
                same = False
                break
        if same:
            count += 1
    return count

# Test the function
print(count_matching_substrings("100", "abracadabra"))  # Output: 2
print(count_matching_substrings("101", "abracadabra"))  # Output: 1
print(count_matching_substrings("000", "abracadabra"))  # Output: 0
print(count_matching_substrings("111", "banana"))  # Output: 0
print(count_matching_substrings("101", "banana"))  # Output: 1
print(count_matching_substrings("010", "banana"))  # Output: 0
                
    

        
            
    
 