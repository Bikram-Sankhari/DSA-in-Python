from node_of_binary_tree import NodeOfBinaryTree


class BinaryTree:
    def __init__(self):
        #                           50
        #                    _______ | ________
        #                   |                  |
        #                   25                 90
        #               ____ | ____        ____ | ____
        #              |           |      |           |
        #             20           30                130
        #                                        ____ | _____
        #                                       |            |
        #                                      100           150
        self.root = NodeOfBinaryTree(50)
        self.root.left = NodeOfBinaryTree(25)
        self.root.left.left = NodeOfBinaryTree(20)
        self.root.left.right = NodeOfBinaryTree(30)
        self.root.right = NodeOfBinaryTree(90)
        self.root.right.right = NodeOfBinaryTree(130)
        self.root.right.right.left = NodeOfBinaryTree(100)
        self.root.right.right.right = NodeOfBinaryTree(150)
