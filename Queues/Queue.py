class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)

        if self.last:
            self.last.next = new_node
        else:
            self.first = new_node

        self.last = new_node
        self.length += 1

    def dequeue(self):
        if not self.first:
            return None

        temp = self.first
        self.first = self.first.next

        if self.first:
            temp.next = None
        else:
            self.last = None

        self.length -= 1
        return temp
