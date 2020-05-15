from random import randint
MAX_NUM = 100


def merge_sort(items):
    """
    Sorts the items in the list
    :param items: The list to sort
    """
    """ Base case"""
    if len(items) == None:
        return
    """ Split into two halfs """
    half = len(items) // 2
    """first half """
    first_half = items[:half]
    """ Second half """
    second_half = items[half:]
    
    """Recursive part"""
    merge_sort(first_half)
    merge_sort(second_half)
    
    
    """Straight from instructors code"""
    
     # Merge the two sorted parts
    i = 0 # iterator for part 1
    j = 0 # iterator for part 2
    k = 0 # iterator for complete list
    
    while i < len(first_half) and j < len(second_half):
        # Get the smaller item from whichever part its in
        if first_half[i] < second_half[j]:
            items[k] = first_half[i]
            i += 1
            k += 1
        else: # part2 <= part1
            items[k] = second_half[j]
            j += 1
            k += 1

    # At this point, one or the other size is done

    # Copy any remaining items from part1
    while i < len(first_half):
        items[k] = first_half[i]
        i += 1
        k += 1

    # Copy any remaining items from part2
    while j < len(second_half):
        items[k] = second_half[j]
        j += 1
        k += 1

    # The list is now sorted!
    
    

def generate_list(size):
    """
    Generates a list of random numbers.
    """
    items = [randint(0, MAX_NUM) for i in range(size)]
    return items


def display_list(items):
    """
    Displays a list
    """
    for item in items:
        print(item)


def main():
    """
    Tests the merge sort
    """
    size = int(input("Enter size: "))

    items = generate_list(size)
    merge_sort(items)

    print("\nThe Sorted list is:")
    display_list(items)


if __name__ == "__main__":
    main()