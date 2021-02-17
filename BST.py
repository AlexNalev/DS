class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.ask_elements()

    @classmethod
    def insert(cls, root, data):
        """
        This method is a class method to create a tree that is not gonna have more
        elements once it's built.
        If we want to allow the insertion of new elements, we take out the class 
        references and make this function a function of the instances of the
        Binary Search Tree class.
        In the main it will be called as:
        bt.insert(bt.root, data)
        """
        if root is None:
            return Node(data)

        else:
            if data < root.data:
                node = cls.insert(root.left, data)
                root.left = node

            elif data > root.data:
                node = cls.insert(root.right, data)
                root.right = node

            else:
                pass

            return root

    def ask_elements(self):
        number_elements = int(input("Number of elements in the tree (root included): "))

        for i in range(number_elements):
            data = int(input(f"Element {i + 1}: "))
            self.root = self.insert(self.root, data)

    def preorder(self, node):
        if node is None:
            return
        else:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return

        else:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        else:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def level_order(self, root):
        queue = []
        queue.append(root)

        while len(queue) != 0:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


bt = BinarySearchTree()
print("--------------------Preorder traversal-----------------")
bt.preorder(bt.root)
print("\n--------------------Inorder traversal-----------------")
bt.inorder(bt.root)
print("\n--------------------Postorder traversal-----------------")
bt.postorder(bt.root)
print("\n--------------------Level traversal-----------------")
bt.level_order(bt.root)

