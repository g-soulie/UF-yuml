class Attribut:
	def __init__(self):
		self.name = None
		self.type = None
		self.defaultValue = None
		self.visi = None

	def fromUML(self,umlString):
		if umlString[0] == "+":
			self.visi = "public"
		if umlString[0] == "-":
			self.visi = "private"
		umlString = umlString.lstrip("+ ").lstrip(" -")
		umlString = umlString.split(":")
		self.name = umlString[0]
		if len(umlString) > 1:
			self.type = umlString[1].lstrip(" ")
		
		

	def toString(self):
		s="\t"
		if not self.visi == None:
			s += self.visi + " "
		if not self.type == None:
			s += self.type + " "
		s += self.name
		if not self.defaultValue == None:
			s += " = " + defaultValue
		s += ";\n"
		return s



