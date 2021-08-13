my_stack = []

def pop():
    if(len(my_stack)):
        return -1
    my_stack.pop()

def push(item):
    my_stack.append(item)

def peek():
    return my_stack[-1]

def show_stack():
    for i in my_stack[::-1]:
        print(i)

