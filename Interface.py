from Method import *

class Interface:
	def __init__(self,name):
		self.methods = []
		self.interfaces = []
		self.name = name

	def fromUML(self,json):
		for uml_method in json["methods"]:
			method = Method()
			method.fromUML(uml_method)
			self.methods.append(method)

	def addMethod(m):
		self.methods.append(m)

	def addInterface(i):
		self.interfaces.append(i)

	def toString(self):
		s = "public interface " + self.name
		s += self.interfaces2String()+ " {\n"
		s += self.methods2String()+"\n"
		s += "}"
		return s

	def interfaces2String(self):
		s = ""
		if len(self.interfaces) > 0:
			s += " implements "
			for i in range(len(self.interfaces)-1):
				s += self.interfaces[i].name + ","
			s += self.interfaces[len(self.interfaces)-1].name
		return s

	def methods2String(self):
		s=""
		if len(self.methods) > 0:
			for i in range(len(self.methods)):
				s += self.methods[i].toString() + "\n"
		return s