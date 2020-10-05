# Lets implement a stack
class Stack:
    def __init__(self):
        self.container = []

    def is_empty(self):
        return self.size() == 0
    
    def push(self, new_value):
        self.container.append(new_value)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        if self.is_empty():
            raise Exception('Stack empty!')
        return self.container[-1]
    
    def size(self):
        return len(self.container)

stack_1 = Stack()
stack_1.push('1')
stack_1.push('2')
print(stack_1.peek())
print(stack_1.size())
print(stack_1.pop())
print(stack_1.size())