def is_paired(input_string):
    stack = []
    pair = {'{':'}', '(': ')', '[':']'}
    for c in input_string:
        if c in pair.keys():
            stack.append(c)
        elif c in pair.values():
            if len(stack) > 0 and c == pair[stack[-1]]:
                stack = stack[:-1]
            else:
                return False
    return True if len(stack) == 0 else False
