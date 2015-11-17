# -*- coding: utf-8 -*-
import commands
from Classe import *
from Interface import *


classes = {}
interfaces = {}

def get_liaisons(folder):
    #recuperation des fichiers de liaisons = ceux commencant par liaisons
    commands.getoutput("rm ./"+folder+".liaisons.txt")
    commands.getoutput("ls ./"+folder +">> ./"+folder+".liaisons.txt")
    liaison = open("./"+folder+".liaisons.txt",'r')
    fichiers=[]
    for fichier in liaison:
        fichiers.append(fichier.rstrip('\n'))

    liaisons=[]
    for fichier in fichiers:
        if fichier[0:7]=="liaison":
            liaisons.append(fichier)
    return liaisons


def setupLiaisons(folder):
    liaisons = get_liaisons(folder)
    for i in range(len(liaisons)):
        f=open("./"+folder+liaisons[i],'r')
        for line in f:
        	line = line.rstrip('\n').split(',')
        	if '^-.-' in line[1]:
        		real_name = line[0].split(">>")[1].lstrip(" ").lstrip("\n")
        		classes[line[2]].addInterface(interfaces[real_name])
    		elif '-.-^' in line[1]:
        		real_name = line[2].split(">>")[1].lstrip(" ").lstrip("\n")
        		classes[line[0]].addInterface(interfaces[real_name])
        	elif '^-' in line[1]:
        		classes[line[2]].addClasseMere(classes[line[0]])
        	elif '-^' in line[1]:
 				classes[line[0]].addClasseMere(classes[line[2]])

	
def createClasse(json):
	classe = Classe(json["name"])
	classe.fromUML(json)
	classes[json["name"]] = classe

def createInterface(json):
	real_name = json["name"].split(">>")[1].lstrip(" ").lstrip("\n")
	interface = Interface(real_name)
	interface.fromUML(json)
	interfaces[real_name] = interface

def write(javaObject,folder):
	f = open("./"+folder+"java/"+javaObject.name+".java",'w')
	f.write(javaObject.toString())
	f.close()


def gen(folder,jsons,getter):
    commands.getoutput("mkdir ./"+folder+"/java/")
    commands.getoutput("rm ./"+folder+"/java/*")

	#Création des classes et des interfaces:
    for json in jsons:
        if json["name"][0] == "<":
            createInterface(json)
        else:
            createClasse(json)

	#Générations des liaisons
    setupLiaisons(folder)

	#Ecriture des fichiers générés
    for classe in classes:
        write(classes[classe],folder)
    for interface in interfaces:
        write(interfaces[interface],folder)