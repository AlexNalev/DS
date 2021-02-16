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
					print(element)
					counter += 1

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
			print(node.data, end = " ")
			self.inorder(node.right)

	def postorder(self, node):
		if node is None:
			return
		else:
			self.postorder(node.left)
			self.postorder(node.right)
			print(node.data, end=" ")

	def level_order(self, root):
		self.queue.append(root)

		while len(self.queue) != 0:
			node = self.queue.pop(0)
			print(node.data, end=" ")
			if node.left is not None:
				self.queue.append(node.left)
			if node.right is not None:
				self.queue.append(node.right)


bt = BinarySearchTree(8, 3, 10, 1, 6, 14, 4, 7, 13)
print("--------------------Preorder traversal-----------------")
bt.preorder(bt.root)
print("\n--------------------Inorder traversal-----------------")
bt.inorder(bt.root)
print("\n--------------------Postorder traversal-----------------")
bt.postorder(bt.root)
print("\n--------------------Level traversal-----------------")
bt.level_order(bt.root)
