
# Data Structures and Algorithms - Coding Exercises

This repository contains Python code for solving three coding exercises related to data structures and algorithms. The exercises cover topics like stacks, sequences (lists/tuples), and dictionaries. Below, you will find a description of each exercise and how to use the provided code.

## question One: Stacks

### is_balanced(expression)

This function checks whether a given expression containing parentheses, curly braces, and square brackets is balanced. An expression is considered balanced if each opening bracket has a corresponding closing bracket in the correct order.

#### Usage:

python
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False


## question Two: Sequences (Lists/Tuples)

### remove_duplicates(sequence)

This function takes a sequence (list or tuple) as input and returns a new sequence with duplicate elements removed while maintaining the original order of elements.

#### Usage:

python
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]


## question Three: Dictionaries

### word_frequency(sentence)

This function takes a sentence as input and returns a dictionary containing the frequency of each word in the sentence. Punctuation is ignored, and words are considered in a case-insensitive manner.

#### Usage:

python
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)


## Running the Code

To run the code for these exercises, you need Python installed on your system. Follow these steps:

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where you saved the code files.

3. Run each exercise individually by executing the respective Python script.

4. You will see the output for each exercise in the terminal.