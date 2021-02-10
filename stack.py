class Node:
	def __init__(self, data, next = None, prev = None):
		self.data = data
		self.next = next
		self.prev = prev

class Stack:
	def __init__(self):
		self.top = None

	def isEmpty(self):
		if self.top is None:
			return True

		return False

	def push(self, data):
		if self.isEmpty():
			self.top = Node(data)

		else:
			self.auxiliary = self.top
			self.top = Node(data, self.auxiliary)
			self.auxiliary.prev = self.top

	def pop(self):
		if self.isEmpty():
			return "Stack underflow"

		else:
			if self.top.next is None:
				auxiliary2 = self.top.data
				self.top = None

			else:
				self.auxiliary = self.top
				self.top = self.top.next
				self.top.prev = None
				auxiliary2 = self.auxiliary.data
				self.auxiliary = None
			
			return auxiliary2

	def peek(self):
		if self.isEmpty():
			return "There aren't elements on the list."

		else:
			return self.top.data

	def show_elements(self):
		if self.isEmpty():
			print("No elements to show.")

		else:
			self.traversal = self.top

			while self.traversal is not None:
				print(self.traversal.data)
				self.traversal = self.traversal.next


plates = Stack()
print(plates.pop())
plates.push(1)
print(plates.pop())
print()
plates.push(1)
plates.push(2)
plates.push(3)
plates.push(4)
print()
plates.show_elements()
print()
print(plates.peek())
print()
plates.pop()
plates.pop()
plates.pop()
plates.pop()
plates.show_elements()
