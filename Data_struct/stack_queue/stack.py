''' data structure LIFO (last in, first out) '''


class Stack:
    def __init__(self):
        self.stack = []

    def get(self):
        if not self.stack:
            return "stack is empty"
        self.stack.pop()

    def add(self, value):
        self.stack.append(value)

    def is_empty(self):
        if not self.stack:
            return True
        return False

    def check_len(self):
        return len(self.stack)


