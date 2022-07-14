if __name__ == "__main__":
    stack = [1,2,3,4,5]
    stack.append(6)
    stack.append(7)
    stack.pop() # pop the top of the stack
    print(stack[-1]) # top of the stack
    print(len(stack))
