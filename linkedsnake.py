from string import digits


class SnakeNode:
	def __init__(self, value:str) -> None:
		self.value = value 
		self.next = None
		self.last = None
		self.upper = self.value.isupper() if value not in digits else False
		self.space = True if self.value == " " else False
	
	def isUpper(self):
		return self.upper
	
	def isLower(self):
		return not self.upper
	
	def isSpace(self):
		return self.space
	

class LinkedSnake:

	def __init__(self, string: str) -> None:
		self.return_string = ""
		self.string = string
		self.stringlist = [x for x in string]
		self.nodes: list[SnakeNode] = [SnakeNode("HEAD"), ]
		self.current_node = None
		self.last_node = None
		self.next_node = None
		self.started = False

		self.start(self.stringlist.pop(0))
		for value in [x for x in self.string]:
			self.addNode(value)
		self.stringlist = [x for x in string]
		self.nodes.append(SnakeNode("TAIL"))
	
	def start(self, value:str):
		if not self.started:
			node = SnakeNode(value)
			self.nodes.append(node)
			self.next_node = node
		
	def addNode(self, value:str):
		
		new_node = SnakeNode(value)

		if self.current_node is None:
			self.last_node = SnakeNode("")
			self.current_node = SnakeNode("")	
		
		if self.current_node.value == "HEAD" or self.current_node.value == None:
			self.current_node.value = ""
			self.current_node.last = ""
			self.next_node = new_node
			self.current_node.next = self.next_node.value
			self.last_node = SnakeNode("")
			self.last_node.next = self.current_node.value
			self.last_node.last = self.current_node.value
			self.last_node = self.current_node
			self.current_node = self.last_node
			return

		elif new_node.value == "TAIL" or self.current_node.value == None:
			self.next_node = SnakeNode("")
			self.next_node.next = ""
			self.next_node.last = ""
			self.current_node.next = self.next_node.value
			self.current_node = self.next_node
			return
		
		if self.next_node != None and self.current_node == None:
			self.current_node = self.next_node
			self.next_node = new_node
			self.current_node.next = self.next_node.value
			self.next_node.last = self.current_node.value
			self.nodes.append(new_node)
			return 
		
		elif self.current_node != None and self.last_node == None:
			self.last_node = self.current_node
			self.current_node = self.next_node
			self.next_node = new_node
			self.current_node.next = self.next_node.value
			self.next_node.last = self.current_node.value
			self.nodes.append(new_node)
			return
		
		elif self.current_node != None and self.last_node != None:
			# adjust next node values 
			self.next_node.next = new_node.value
			self.next_node.last = self.current_node.value
			# adjust new node values 
			new_node.last = self.next_node.value
			# adjust current node values
			self.current_node.next = self.next_node.value
			self.current_node.last = self.last_node.value
			#adjust last node values
			self.last_node.next = self.current_node.value
			# adjust node index
			self.last_node = self.current_node
			self.current_node = self.next_node
			self.next_node = new_node
			self.nodes.append(self.next_node)
			return

	def snakecase(self):
		import gc
		gc.disable()
		self.retv = ""
		self.current_node = None
		self.next_node = self.nodes[0]
		self.last_node = None
		
    for node in self.nodes[2:]:
			self.last_node = self.current_node
			self.current_node = self.next_node
			self.next_node = node
			if self.current_node.value == "HEAD":
				continue
			if self.last_node.value == "HEAD":
				if self.next_node.isLower():
					self.retv+=self.current_node.value.lower()
					continue
				if self.next_node.isUpper():
					if self.current_node.isLower():
						self.retv+=self.current_node.value
						self.retv+="_"
						continue
					elif self.current_node.isUpper():
						self.retv+=self.current_node.value 
						continue
			if self.next_node.value == "TAIL":
				self.next_node.value = ""
				# if the current node is uppercase
				if self.current_node.isUpper():
					if self.last_node.isUpper() and self.next_node.isUpper():
						self.retv+=self.current_node.value
						self.retv+=self.next_node.value
						break
					elif self.last_node.isUpper() and self.next_node.isLower():
						self.retv+=self.current_node.value
						self.retv+="_"
						self.retv+=self.next_node.value
						break
					elif self.last_node.isLower() and self.next_node.isUpper():
						self.retv+="_"
						self.retv+=self.current_node.value
						self.retv+=self.next_node.value
						break
					elif self.last_node.isLower() and self.next_node.isLower():
						self.retv+=self.current_node.value.lower()
						self.retv+self.next_node.value.lower()
						break
				elif self.current_node.isLower():
					if self.last_node.isUpper() and self.next_node.isUpper():
						self.retv+=self.current_node.value
						self.retv+="_"
						self.retv+=self.next_node.value.lower()
						break
					elif self.last_node.isUpper() and self.next_node.isLower():
						self.retv+=self.current_node.value
						self.retv+=self.next_node.value
						break
					elif self.last_node.isLower() and self.next_node.isUpper():
						self.retv+=self.current_node.value
						self.retv+="_"
						self.retv+=self.next_node.value.lower()
						break
					elif self.last_node.isLower() and self.next_node.isLower():
						self.retv+=self.current_node.value
						self.retv+=self.next_node.value
						break
					break
			if self.current_node.isUpper():
				if self.last_node.isUpper() and self.next_node.isUpper():
					if self.last_node.value == "HEAD" and self.next_node.isUpper():
						self.retv+=self.current_node.value
						continue
					elif self.last_node.value == "HEAD" and self.next_node.isLower():
						self.retv+=self.current_node.value.lower()
						continue
					self.retv+=self.current_node.value
					continue
				elif self.last_node.isUpper() and self.next_node.isLower():
					self.retv+=self.current_node.value
					self.retv+="_"
					continue
				elif self.last_node.isLower() and self.next_node.isUpper():
					self.retv+="_"
					self.retv+=self.current_node.value
					continue
				elif self.last_node.isLower() and self.next_node.isLower():
					if self.retv[-1] != "_":
						self.retv+="_"
					self.retv+=self.current_node.value.lower()
					continue
				continue
			elif self.current_node.isLower():
				if self.last_node.isUpper() and self.next_node.isUpper():
					self.retv+=self.current_node.value
					self.retv+="_"
					continue
				elif self.last_node.isUpper() and self.next_node.isLower():
					self.retv+=self.current_node.value
					continue
				elif self.last_node.isLower() and self.next_node.isUpper():
					self.retv+=self.current_node.value
					continue
				elif self.last_node.isLower() and self.next_node.isLower():
					self.retv+=self.current_node.value.lower()
					continue
				continue
		gc.enable()
		return self.retv.strip("_").replace("__", "_")
