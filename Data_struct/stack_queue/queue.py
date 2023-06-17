''' data strucrure FIFO (first in, first out) 
A queue emplemented through a list works slowly due to the peculiarities of the list
It will be more efficient to implement it through a linked list, but not in this example '''


class Queue:
    def __init__(self):
        self.queue = []

    def add(self, value):
        self.queue.append(value)

    def get(self):
        if not self.queue:
            return "queue is empty"
        self.queue.pop(0)

    def is_empty(self):
        if not self.queue:
            return True
        return False

    def get_len(self):
        return len(self.queue)


