class Argument:
	def __init__(self):
		self.type = None
		self.name = None

	def fromUML(self,umlString):
		umlString = umlString.split(" ")
		self.name = umlString[len(umlString)-1]
		if len(umlString)>1:
			self.type = umlString[0]


	def toString(self):
		return self.type + " "+ self.name