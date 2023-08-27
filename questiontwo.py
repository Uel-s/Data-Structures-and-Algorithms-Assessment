def remove_duplicates(sequence):
    seen = set()  # Initialize an empty set to store unique elements
    result = []   # Initialize an empty list to store the result

    # Iterate through the elements in the input sequence
    for item in sequence:
        if item not in seen:  # Check if the item is not already seen
            seen.add(item)    # Add the item to the set to mark it as seen
            result.append(item)  # Append it to the result list

    return result

# Test case
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]