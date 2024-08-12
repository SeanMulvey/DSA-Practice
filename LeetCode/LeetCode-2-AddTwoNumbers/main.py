# !!!NOTE: THIS IS NOT COMPLETE, STILL WORKING OUT SOLUTION!!!

# DSA practice using leetCode problem 2: Add Two Numbers (Medium)
##################################################################
# Problem:
    #You are given two non-empty linked lists representing two 
    # non-negative integers. The digits are stored in reverse order, 
    # and each of their nodes contains a single digit. Add the two 
    # numbers and return the sum as a linked list. You may assume 
    # the two numbers do not contain any leading zero, except the 
    # number 0 itself.
##################################################################
# Initial Thoughts:
    # Since we are adding the two linked lists together as one number,
    #  we can achieve this by adding the digits in each decimal place 
    # and if its greater than 10, we carry the 1 to the next decimal place. 
    # Because the linked lists are stoerd in reverse order, we can do this. 
    # If they were stored in the correct order, I think we would need a 
    # doubly-linked list to solve it in this manner.
# Things to consider:
    # 1. The numbers each list represent are always positive, so we don't
    #  need to handle negative numbers.
    # 2. The numbers do not contain leading 0's unless the number is 0.
    # 3. The linked lists can be of different lengths.
# Steps:
    # 1. Check if either list ends in 0. If so that would mean the number would
        # have leading 0's, meaning the number would have to 0 based on problem
        # parameters. In that case we could just return the value of the other list.
    # 2. Create a new list to store the sum of each digit.
    # 3. Check length of each linked list.
        # If lengths are different, we want to get the smaller one since
        # thats the one we will iterate over.
        # We want to iterate on the smaller linked list because once direct 
        # addition is complete, we only need to carry over 1's if the next
        # digit in the larger list is greater than 10.
    # 4. foreach node in the shorter list, add it to the corresponding node in
        # the longer list.
    # 5. If the sum from step 3 is greater than 9, subtract 10 from the sum and add
        # 1 to the next node in the longer list.
    # 6. Add the sum (subtracted sum if greater than 9) to a separate list
        # to store the result.
    # 7. Return the result list.
########################################################################


# Python Code:

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next





def add_two_numbers(l1, l2):
    # if len(l1) != len(l2):
    #     if len(l1) < len(l2):
    #         l3 = l1
    #         other = l2
    #     else:
    #         l3 = l2
    #         other = l1
    # else:
    #     l3 = l1

 
    new_list = ListNode(0)
    carry = 0
    while l1:
        l1.val += carry
            
        l1.val += l2.val
        if l1.val >= 10:
            new_list.val = l1.val - 10
            l1 = l1.next 
            l2 = l2.next
            carry = 1
        else:
            new_list.val = l1.val
            l1 = l1.next
            l2 = l2.next
            carry = 0
    return new_list

# Test the function
node1 = ListNode(2)
node1.next = ListNode(4)
node1.next.next = ListNode(3)

node2 = ListNode(5)
node2.next = ListNode(6)


print(add_two_numbers(node1, node2))



        
