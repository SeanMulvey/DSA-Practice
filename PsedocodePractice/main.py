# Practice turnining psuedocode into actual code
########################################################################
# Problem:
    #Find largest number in a collection

#Psuedocode:
    # a = [list of numbers]
    # biggest_num = a[0]
    # for num in a
        # if num > biggest_num
            # biggest_num = num
    # return biggest_num
########################################################################

# Python Code:

def get_biggest_num(collection):
    biggest_num = collection[0]
    for num in collection:
        if num > biggest_num:
            biggest_num = num
    return biggest_num
    
    
print(get_biggest_num([64, 25, 12, 22, 11, 126]))
    
