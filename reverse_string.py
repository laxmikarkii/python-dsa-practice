"""
Problem: Reverse a String

Description: Given a string, return the string in reverse order.

Example:

Approach:

Time complexity: 
Space complexity:
"""

def reverse_string(s: str) -> str:
    """
    Reverse a string using the two-pointer technique.
    """

    chars = list(s)

    left = 0
    right = len(chars) - 1

    while left < right:
        temp = chars[left]
        chars[left] = chars[right]
        chars[right] = temp

        left += 1
        right -= 1

    return "".join(chars)


# Test cases
if __name__ == "__main__":

    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("a") == "a"
    assert reverse_string("") == ""

    print("All test cases passed!")