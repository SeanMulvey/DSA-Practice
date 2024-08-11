# This is an example of a Selection Sort Algorithm
################################################################
# Selection Sort Algorithm:
    # 1. Search through a collection for the smallest element
    # 2. Swap the smallest element with the first element
    # 3. Repeat the process for the remaining unsorted elements
# Time Complexity: O(n^2)
################################################################

def selection_sort(collection):
    # Iterate thorugh collection to get smallest number
    for i in range(len(collection)):
        # Compare collection[i] to each other element in collection
        for j in range(i + 1, len(collection)):
            #Check if collection[j] is smaller than collection[i]
            if collection[j] < collection[i]:
                # If collection[j] is smaller that collection[i], swap places
                collection[i], collection[j] = collection[j], collection[i]
    return collection

# Test the function
case = [64, 25, 12, 22, 11]
print("Original Collection:", case)
print("Selection Sort Algorithm:", selection_sort(case))
