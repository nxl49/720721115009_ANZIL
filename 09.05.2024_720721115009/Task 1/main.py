def is_valid(s):
    """
    Determines if the input string is valid.

    Args:
        s: The input string.

    Returns:
        True if the string is valid, False otherwise.
    """

    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top = stack.pop() if stack else "#"
            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return len(stack) == 0

# Example usage
s = "()"
print(is_valid(s))  # Output: True

s = "()[]{}"
print(is_valid(s))  # Output: True

s = "(]"
print(is_valid(s))  # Output: False