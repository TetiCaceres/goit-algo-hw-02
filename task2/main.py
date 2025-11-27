from collections import deque

def is_palindrome(entry_data: str) -> bool:
    """
    Check if the input string is a palindrome.
    It ignores case and spaces, and compares characters from both ends using deque.
    """

    # Convert to lowercase and remove spaces
    cleaned = entry_data.lower().replace(" ", "")

    # Add characters into deque
    dq = deque(cleaned)

    # Compare characters from both ends
    while len(dq) > 1:
        if dq.pop() != dq.popleft():
            return False

    return True


# Main program execution
entry_data = input("Input a string of chars: ")

if is_palindrome(entry_data):
    print("entry data is a palindrome")
else:
    print("entry data is not a palindrome")
