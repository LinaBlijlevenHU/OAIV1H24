def is_sorted(maybesorted):
    """ Check if a list is sorted """
    # Start by secretly comparing the first element to itself
    prev = maybesorted[0]

    for el in maybesorted:
        # Check if bigger than previous element
        if el >= prev:
            # Store the current element for the next comparison
            prev = el
        else:
            # If we get here it's not sorted
            return False

    # If we haven't found two unsorted elements by now we're all sorted
    return True

import random

def bogosort(elements):
    tries = 0

    while not is_sorted(elements):
        print(f"Oh no the list is not sorted! {elements}")
        random.shuffle(elements)
        tries += 1

    return elements, tries

# Sample lists
actuallysorted = [1, 2, 3, 4, 5]
notsorted = [2, 4, 6, 5]

sortlist, tries = bogosort(actuallysorted)
print(f"List sorted in {tries} tries.\n{sortlist}")
sortlist, tries = bogosort(notsorted)
print(f"List sorted in {tries} tries.\n{sortlist}")
