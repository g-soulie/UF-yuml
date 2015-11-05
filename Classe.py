from Attribut import *
from Interface import *
from Method import *

class Classe:
	def __init__(self,name):
		self.methods = []
		self.attributs = []
		self.interfaces = []
		self.meres = []
		self.name = name


	def fromUML(self,json):
		for uml_attribut in json["attributs"]:
			if len(uml_attribut)>0:
				attribut = Attribut()
				attribut.fromUML(uml_attribut)
				self.attributs.append(attribut)
		for uml_method in json["methods"]:
			method = Method()
			method.fromUML(uml_method)
			self.methods.append(method)


	def addMethod(self,m):
		self.methods.append(m)

	def addInterface(self,i):
		self.interfaces.append(i)

	def addAttribut(self,a):
		self.attributs.append(a)

	def addClasseMere(self,c):
		self.meres.append(c)

	def toString(self):
		s = "public class " + self.name
		s += self.meres2String() + ""
		s += self.interfaces2String()+ " {\n"
		s += self.attributs2String()+"\n"
		s += self.methods2String()
		s += "}"
		return s

	def meres2String(self):
		s = ""
		if len(self.meres) > 0:
			s += " extends "
			for i in range(len(self.meres)-1):
				s += self.meres[i].name + ","
			s += self.meres[len(self.meres)-1].name + " "
		return s
	
	def interfaces2String(self):
		s = ""
		if len(self.interfaces) > 0:
			s += " implements "
			for i in range(len(self.interfaces)-1):
				s += self.interfaces[i].name + ","
			s += self.interfaces[len(self.interfaces)-1].name
		return s

	def attributs2String(self):
		s=""
		if len(self.attributs) > 0:
			for i in range(len(self.attributs)):
				s += self.attributs[i].toString()
		return s

	def methods2String(self):
		s=""
		if len(self.methods) > 0:
			for i in range(len(self.methods)):
				s += self.methods[i].toString() + "\n"
		return s





