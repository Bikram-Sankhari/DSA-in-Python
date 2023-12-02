class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self):
        temp = self.top

        if temp:
            self.top = self.top.next
            temp.next = None
            self.height -= 1

        return temp

