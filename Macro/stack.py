import networkx

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def insert_sons(self,G,item_father):
        list_sons=list(G.successors(int(item_father)))
        for i in list_sons:
           self.push(i)

    def print_stack_order(self):
        print("Stack Order:")
        for item in self.stack:
            print(item)
# Example usage
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
#
# print(stack.pop())  # Output: 3
# print(stack.peek())  # Output: 2
# print(stack.pop())  # Output: 2
# print(stack.pop())  # Output: 1
# print(stack.pop())  # Output: Stack is empty
