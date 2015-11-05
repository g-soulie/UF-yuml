from Argument import *

class Method:
	def __init__(self):
		self.rtype = None
		self.visi = None
		self.stat = None
		self.args = []

	def fromUML(self,umlString):
		if umlString[0] == "+":
			self.visi = "public"
		if umlString[0] == "-":
			self.visi = "private"
		umlString = umlString.lstrip("+ ").lstrip("- ")
		umlString = umlString.split(":")
		if len(umlString) > 1:
			self.rtype = umlString[1].lstrip(" ")
		umlString = umlString[0]
		umlString = umlString.split("(")
		self.name = umlString[0]
		if len(umlString) > 1:
			arguments = umlString[1].split(")")[0].split(",")
			if len(arguments[0])>0:
				for uml_argument in arguments:
					argument = Argument()
					argument.fromUML(uml_argument.lstrip(" "))
					self.args.append(argument)

	def toString(self):
		s="\t"
		if not self.visi == None:
			s += self.visi + " "
		if not self.stat == None:
			s += self.stat + " "
		if not self.rtype == None:
			s += self.rtype + " "
		s += self.name + "("
		if len(self.args) > 0:
			for i in range(len(self.args)-1):
				s += self.args[i].toString()+", "
			s += self.args[len(self.args)-1].toString()
		s+="){\n"
		if not self.rtype == None:
			if self.rtype == "int" or self.rtype == "float" or self.rtype == "long" \
			or self.rtype == "double":
				s += "\t\treturn 0;\n"
			elif self.rtype == "boolean":
				s += "\t\treturn false;\n"
			elif not self.rtype == "void":
				s += "\t\treturn null;\n"
		return s + "\t}\n"