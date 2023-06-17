
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        list_nodes = []
        if not self.head:
            return list_nodes
        while self.head.next:
            list_nodes.append(self.head)
            self.head = self.head.next
        list_nodes.append(self.head)
        return str(list_nodes)

    def get_index(self, data):
        if not self.head:
            return "Linked list is empty"
        index = 0
        while self.head.next:
            if self.head == data:
                return index
            self.head = self.head.next
            index += 1
        return f"Node {data} not found in linked list"

    def add_tail(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def add_head(self, data):
        node = Node(data)
        if self.head:
            self.head = node
            self.tail = node
        self.head.prev = node
        node.next = self.head
        self.head = node

    def insert(self, index, data):  # Пока пропущу. Нужно сделать проверку на длину. Или если индекс больше, ставвл в конец
        pass

    def is_empty(self):
        if not self.head:
            return True
        return False

    def search(self, data):
        if not self.head:
            return None
        self.head

    def pop(self, index=None):  # по умолчанию (None) возвращаем и удаляем self.tail со сменой ссылок
        pass


