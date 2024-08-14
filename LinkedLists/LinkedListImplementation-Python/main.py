# Example of how to create a linked list in Python
################################################################################################
# A linked list is composed of nodes, where each node contains data and a reference to the next node.
# We need to define a Node class to represent each node in the list.
# Each node will have two attributes: data (to store the value) and next (to store the reference to the next node).
################################################################################################

# In python we have to define the Node class before creating the LinkedList class because a linked list is not a built-in data structure in Python.

# Define the node class that will contain the constructor for each node
class linkedListNode:

    # Constructor for the Node class
    ################################################################################################
    # def __init__(): is the built in Python method that we use to initialize an object of the class.
    # self refers to the current object being created.
    # value: the data to be stored in the node
    # next: a reference to the next node in the list
    def __init__ (self, value, next = None):
        # We assign the value of our object to the value passed through the constructor as a parameter
        self.value = value
        # We assign the next node to the next passed through the constructor as a parameter, or None if no next node is provided
        self.next = next


# Now that we have the boiler plate set up to construct a linked list, lets create a Linked List
# Lets make a linked list with 3 nodes: a -> b -> c
#####################################################################################################
# We start by creating the isolated nodes a, b, and c
# As of right now, these nodes are completely separate from each other and not connected to each other.
node1 = linkedListNode("a")
node2 = linkedListNode("b")
node3 = linkedListNode("c")


# Now, we connect the nodes together.
##################################################################################################
# Because the next attribute of each node is a reference to the next node, we set the next attribute of node1 to node2
# Now node1 knows that the next node is node2.
node1.next = node2
# Next, we do the same for node2 and node3
node2.next = node3
# Now our nodes are connected in a linear order: a -> b -> c
#################################################################################################
# Lets test our linked list to make sure it works as expected

# We will start at the first node(sometimes called the head node) (node1) and print each node's value until we reach the end of the list (None)
currentNode = node1

while True:
    # Becuase the end of our linked list doesn't point to a next value, it will point to None
    # So we check if the current node is pointing to None, if it is, we print "None" and break the loop
    if currentNode is None:
        print("None")
        break
    print(currentNode.value)
    # After printing the current node's value, we move to the next node in the list
    # Because currentNode starts at the head(node1), if we update currentNode to currentNode.next, we will move to the next node in the list
    # And the next node's next node, and so on...
    currentNode = currentNode.next

# Output:
    # a
    # b
    # c
    # None


