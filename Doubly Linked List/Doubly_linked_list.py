class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if not self.head:
            return None

        temp = self.tail
        if not self.head.next:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next.prev = None
            self.tail.next = None

        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if not self.head:
            return None

        temp = self.head
        if not self.head.next:
            self.head = None
            self.tail = None

        else:
            self.head = temp.next
            temp.next = None
            self.head.prev = None

        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next

        else:
            temp = self.tail
            for _ in range(self.length - index - 1):
                temp = temp.prev

        return temp

    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True

        return False

    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        before = self.get(index - 1)
        if before:
            new_node = Node(value)
            after = before.next
            before.next = new_node
            new_node.prev = before
            after.prev = new_node
            new_node.next = after

            self.length += 1
            return True

        return False

    def remove(self, index):
        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        node_to_be_removed = self.get(index)

        if node_to_be_removed:
            node_to_be_removed.prev.next = node_to_be_removed.next
            node_to_be_removed.next.prev = node_to_be_removed.prev
            node_to_be_removed.next = None
            node_to_be_removed.prev = None
            self.length -= 1

        return node_to_be_removed

