def is_balanced(expression):
    # Define the mapping of opening and closing brackets
    brackets = {')': '(', '}': '{', ']': '['}
    stack = []  # Initialize an empty stack to track brackets

    for char in expression:
        # If the character is an opening bracket, push it onto the stack
        if char in brackets.values():
            stack.append(char)
        # If the character is a closing bracket
        elif char in brackets.keys():
            # If the stack is not empty and the top of the stack matches the corresponding opening bracket
            if stack and stack[-1] == brackets[char]:
                stack.pop()  # Pop the opening bracket from the stack
            else:
                return False  # Return False if brackets are not balanced

    return not stack  # If the stack is empty, brackets are balanced


# Test cases
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
