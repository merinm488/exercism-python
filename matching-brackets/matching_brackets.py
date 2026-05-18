def is_paired(input_string):
    open_to_close = {'(':')', '[':']', '{':'}'}
    stack = []
    for char in input_string:
        if char in '([{':
            stack.append(open_to_close[char])
        elif char in ')]}':
            if len(stack) == 0:
                return False
            elif stack[-1] == char:
                stack.pop()
            else: return False
    
    return len(stack) == 0
