def remove_duplicates(sequence):
    result = []  # Initialize an empty list to store unique elements
    # Iterate through the elements in the input sequence
    [result.append(x) for x in sequence if x not in result]
    return result  # Return the list with duplicates removed

# Test case
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]