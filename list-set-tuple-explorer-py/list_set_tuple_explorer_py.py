# ==========================
#   COLLECTION OPERATIONS
#   LIST - SET - TUPLE
# ==========================

# ------------------------
# LIST METHODS
# ------------------------

def list_operations():
    print("\nLIST OPERATIONS")
    print("=================")
    # List: Ordered, mutable, allows duplicates
    fruits = ["Apple", "Banana", "Coconut", "Banana"]

    # Add item to the end
    fruits.append("Orange")  # ['Apple', 'Banana', 'Coconut', 'Banana', 'Orange']

    # Insert item at index 1
    fruits.insert(1, "Grape")  # ['Apple', 'Grape', 'Banana', 'Coconut', 'Banana', 'Orange']

    # Remove first occurrence of an item (if exists)
    if "Banana" in fruits:
        fruits.remove("Banana")  # ['Apple', 'Grape', 'Coconut', 'Banana', 'Orange']

    # Count how many times 'Banana' appears
    banana_count = fruits.count("Banana")
    print("Banana count:", banana_count)

    # Sort the list in ascending alphabetical order
    fruits.sort()

    # Reverse the order of the list
    fruits.reverse()

    # Check if "Apple" is in the list
    is_apple_present = "Apple" in fruits
    print("Is Apple in list?", is_apple_present)

    # Find the index of "Coconut"
    if "Coconut" in fruits:
        coconut_index = fruits.index("Coconut")
        print("Index of Coconut:", coconut_index)

    # Print list length
    print("List length:", len(fruits))

    # Print final list
    print("Final list:", fruits)

    # Clear the list
    fruits.clear()
    print("List after clearing:", fruits)


# ------------------------
# SET METHODS
# ------------------------

def set_operations():
    print("\nSET OPERATIONS")
    print("================")
    # Set: Unordered, mutable, no duplicates
    fruit_set = {"Apple", "Banana", "Coconut"}

    # Add a new item to the set
    fruit_set.add("Orange")
    fruit_set.add("Apple")  # Duplicate, ignored

    # Remove an item safely (no error if not found)
    fruit_set.discard("Banana")

    # Another set for demonstration
    tropical_fruits = {"Mango", "Pineapple", "Apple"}

    # Union: Combine both sets (no duplicates)
    union_set = fruit_set.union(tropical_fruits)

    # Intersection: Common elements
    intersection_set = fruit_set.intersection(tropical_fruits)

    # Difference: Elements in fruit_set but not in tropical_fruits
    difference_set = fruit_set.difference(tropical_fruits)

    # Membership test
    is_coconut_present = "Coconut" in fruit_set
    print("Is Coconut in set?", is_coconut_present)

    # Print all results
    print("Fruit set:", fruit_set)
    print("Union with tropical fruits:", union_set)
    print("Intersection with tropical fruits:", intersection_set)
    print("Difference from tropical fruits:", difference_set)


# ------------------------
# TUPLE METHODS
# ------------------------

def tuple_operations():
    print("\nTUPLE OPERATIONS")
    print("=================")
    # Tuple: Ordered, immutable, allows duplicates
    fruit_tuple = ("Apple", "Banana", "Coconut", "Banana")

    # Access an item using index
    print("First fruit:", fruit_tuple[0])

    # Count occurrences of an item
    banana_count = fruit_tuple.count("Banana")
    print("Banana count:", banana_count)

    # Get index of an item
    coconut_index = fruit_tuple.index("Coconut")
    print("Index of Coconut:", coconut_index)

    # Get length of tuple
    print("Length of tuple:", len(fruit_tuple))

    # Check membership
    print("Is Apple in tuple?", "Apple" in fruit_tuple)

    # Tuple slicing (first 2 items)
    print("First two fruits:", fruit_tuple[:2])


# ------------------------
# MAIN EXECUTION
# ------------------------

def main():
    list_operations()
    set_operations()
    tuple_operations()

if __name__ == "__main__":
    main()
