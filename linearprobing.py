class HashTable:
	def __init__(self):
		self.size = 10
		self.keys = [None]*self.size 
		self.values = [None]*self.size

	def put(self, key, data):
		index = self.hashFunction(key)

		#deals with the possibility fo a collision

		while self.keys[index] is not None:
			if self.keys[index] == key: #update
				self.values[index] = data
				return
			index = (index + 1)%self.size

		self.keys[index] = key 
		self.values[index] = data 

	def get(self, key):
		index = self.hashFunction(key)

		while self.keys[index] is not None:
			if self.keys[index] == key:
				return self.values[index]

			index = (index + 1)%self.size

		return None #key not present in associative array



	def hashFunction(self, key):
		sum = 0
		for pos in range(len(key)):
			sum = sum + ord(key[pos])

		return sum%self.size





if __name__ == "__main__":
	table = HashTable()
	table.put("apple", 10)
	table.put("orange", 20)
	table.put("car", 30)
	table.put("table", 40)

	print table.get("orang")