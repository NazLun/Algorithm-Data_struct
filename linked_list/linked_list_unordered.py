class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        print_list = []
        current = self.head
        while current:
            print_list.append(current.get_data())
            current = current.get_next()
        return str(print_list)

    def is_empty(self):
        return self.head==None

    def add(self, item):
        node = Node(item)
        node.set_next(self.head)  # Самый легкий доступ к 1 элементу, поэтому добавление идет в начало неупорядоч списка
        self.head = node

    def size(self):      # size, search, remove основаны на обходе списка, поэтому работают за O(N)
        count = 0                       # поочередное посещение каждого узла
        current = self.head
        while current != None:
            current = current.get_next()
            count += 1
        return count

    def search(self, item):
        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def get(self, index):
        current = self.head
        while self.index(current.get_data()) < index:
            current = current.get_next()
        return current.get_data()

    def remove(self, item):
        current = self.head
        prev = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                prev = current
                current = current.get_next()

            if prev == None:
                self.head = current.get_next()
            else:
                prev.set_next(current.get_next())
        return f'element {item} was deleted'

    def append(self, item):     # добавление в конец св списка
        current = self.head
        if not current:
            self.head = Node(item)
            return item
        while current.get_next():
            current = current.get_next()
        current.set_next(Node(item))

    def index(self, item):
        current = self.head
        index = 0
        while current:
            if current.get_data() == item:
                return index
            index += 1
            current = current.get_next()
        return index

    def insert(self, pos, item):
        node = Node(item)
        if pos == 0:
            node.set_next(self.head)
            self.head = node
        else:
            current = self.head
            prev = None
            while self.index(current.get_data()) != pos:
                prev = current
                current = current.get_next()
                if current is None:
                    break
            node.set_next(current)    # порядок этой и след строки не важен, т.к. current не теряется из памяти,
            prev.set_next(node)

    def pop(self, index=None):
        if index is None:
            index = self.size() - 1
        if index < 0:
            index = self.size() - abs(index)
        if index < 0 or (index >= self.size()):
            raise IndexError
        current = self.head
        previous = None
        while self.index(current.get_data()) != index:
            previous = current
            current = current.get_next()
        item = current.get_data()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return item


