class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


class BinarySearchTree:
	def __init__(self, *args):
		self.root = None
		self.aux = None
		self.elements = []
		self.elements.extend([*args])
		self.root = Node(self.elements[0])
		self.order_tree()

	def order_tree(self):
		if self.root is not None:
			self.aux = self.root
			counter = 1

			while counter != (len(self.elements)):
				element = self.elements[counter]

				if element < self.aux.data:
					if self.aux.left is None:
						self.aux.left = Node(element)
						counter += 1
						self.aux = self.root
					else:
						self.aux = self.aux.left
				elif element > self.aux.data:
					if self.aux.right is None:
						self.aux.right = Node(element)
						counter += 1
						self.aux = self.root
					else:
						self.aux = self.aux.right
				else:
					counter += 1

	def preorder(self, node):
		if node is None:
			return
		else:
			print(node.data)
			self.preorder(node.left)
			self.preorder(node.right)


bt = BinarySearchTree(8, 3, 3, 10, 1, 6, 14, 4, 7, 13)
bt.preorder(bt.root)
