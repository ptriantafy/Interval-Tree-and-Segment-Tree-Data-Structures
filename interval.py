import random

class Interval:
	def __init__(self, minLow, maxLow, minSize, maxSize):
		self.low = random.randint(minLow, maxLow)
		self.high =self.low +  random.randint(minSize, maxSize)

	def __str__(self):
		return "[" + str(self.low) + "," + str(self.high) + "]"

