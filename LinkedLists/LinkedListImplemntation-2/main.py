# Building on to the what we learned with LinkedListImplementation-1
# We will do a more complex practical example where we set up functions for a linked list, rather than hard coding one
######################################################################################################################

# We need to create the constructor for the linked list
# This class is used to create a new node for a linked list
######################################################################################################################
class linkedListNode:
    def __init__(self, value, next = None):
        # We set the value of our new node to the value passed through the parameter
        self.value = value
        # We set the pointer (next) to point to the next node and if next isn't passed through the parameters, we set next to None
        self.next = next


# This is the class that takes the individual nodes and connects them together to form a linked list
######################################################################################################################
class linkedList:
    def __init__(self, head = None):
        # We set the head(the start) of our linked list to the node passed through the parameter or None if no node is passed through the parameters
        # We do this to initialize an empty linked list
        self.head = head

    # This function adds a new node to the end of the linked list
    ##################################################################################################################
    def insert(self,value):
        # We create a new node with the given value
        node = linkedListNode(value)
        # We check to see if our linked list is empty
        # We can do this by checking if our head is None
        if self.head is None:
            # If our linked list is empty, we set our head to the new node with the given value
            self.head = node
            return
        # If our linked list isn't empty, we move to the end of the list by traversing through each node
        current_node = self.head
        # We keep moving to the next node until we reach the end of the list
        while True:
            # We check if the next node is None, which means we've reached the end of the list
            if current_node.next is None:
                # If current_node.next is None, we set it to the new node with the given value
                current_node.next = node
                return
            # If current_node.next isn't None, we move to the next node of the linked list
            current_node = current_node.next
    
    # Now we'll create a function to print out the values of the linked list
    ##################################################################################################################
    def print_list(self):
        # We initialize a variable current_node to the head of our linked list
        current_node = self.head
        # We loop through the linked list until we reach the end
        while current_node is not None:
            # For each node, we print the value and move to the next node
            print (current_node.value + "->")
            current_node = current_node.next


# Lets create a linked list and insert some values
my_list = linkedList()
print("Initial List:")
my_list.print_list()
print("\nAfter Insertion:")
my_list.insert("a")
my_list.print_list()
print("\nAfter Insertion:")
my_list.insert("b")
my_list.print_list()
print("\nAfter Insertion:")
my_list.insert("c")
my_list.print_list()

# Print the values of the linked list
        