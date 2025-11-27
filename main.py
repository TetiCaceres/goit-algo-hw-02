def check_string(str_to_check):
    # Stack stores only opening brackets while scanning the string
    stack = []

    open = ["(", "[", "{"]
    close = [")", "]", "}"]

    for ch in str_to_check:
        if ch in open:
            stack.append(ch)  # push opening bracket
        elif ch in close and stack:
            # If closing bracket does not match the last opening one → exit early
            if close.index(ch) != open.index(stack[-1]):
                break
            stack.pop()  # pop matched opening bracket

    # If stack is empty → all brackets matched
    return "Symmetric" if not stack else "Not symmetric"


# Test expressions to validate bracket symmetry
test_expressions = [
    "( ) { [ ] ( ) ( ) { } } }",
    "( 23 ( 2 - 3);",
    "( 11 }",
    "([{}])",
    "((()))",
    "(()",
    ")(",
    "{[()]}",
    "[()]{}"
]

# Run tests
for exp in test_expressions:
    print(check_string(exp))
