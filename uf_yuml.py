# -*- coding: utf-8 -*-
import commands
import sys
import javagen

#python uf_yuml.py exemple/ methoffds png plain


params={"-p":"","-f":"png","-s":"plain","-j":"False","-g":"False","-m":"False"}
i=1
while i <len(sys.argv):
    if sys.argv[i] in params:
        params[sys.argv[i]]=sys.argv[i+1]
        i+=1
    i+=1

folder = params["-p"]

def fichier_to_JSON(i,classes):#transforme un fichier de classe en un JSON ad hoc
    #format du JSON : {"name":"","attributs":[],"methods":[]} 
    f=open("./"+folder+"class/"+classes[i],'r')
    json={"name":"","attributs":[],"methods":[],"asc":""}
    etat=-1
    for line in f:
        if etat == -1:
            json["name"]=line.rstrip('\n')  
            etat += 1
        elif len(line)==1:
            etat += 1
        elif etat == 1:
            json["attributs"].append(line.rstrip('\n'))
        elif etat == 2:
            json["methods"].append(line.rstrip('\n'))
    return json

def JSON_to_string(json):#transforme un JSON en une string yuml ad hoc
    stri = ""
    stri += '[' + json["name"]
    if len(json["attributs"]) > 0:
        stri += '|'
        for i in range(len(json['attributs'])-1):
            stri += json['attributs'][i]+';'
        stri += json['attributs'][len(json['attributs'])-1]

    if len(json["methods"]) > 0:
        stri += '|'
        for i in range(len(json['methods'])-1):
            stri += json['methods'][i]+';'
        stri += json['methods'][len(json['methods'])-1]
    stri += ']'
    i = 0
    while i < len(stri):
        if stri[i] == '<' or stri[i] == '>':
            stri = stri[:i]+'\\'+stri[i:]
            i += 1
        elif stri[i] == ',':
            stri = stri[:i]+'&#1548;'+stri[i+1:]
            i += 6
        i += 1
    return stri


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
    commands.getoutput("rm ./"+folder+".liaisons.txt")
    return liaisons


def ajouter_laisons(string_yuml):#Ajoute les liaisons a la string yuml
    liaisons = get_liaisons(folder)

    string_yuml+=","
    #Ajout liaisons:
    for i in range(len(liaisons)):
        f=open("./"+folder+liaisons[i],'r')
        for line in f:
            i=0
            while i < (len(line))-1:
                if line[i:i+2]=='<<' or line[i:i+2]=='>>':
                    line = line[:i]+'\\'+line[i+1]+'\\'+line[i+1:]
                    i+=3
                i+=1    
            line = line.split(",")
            line[2]=line[2].rstrip('\n')
            string_yuml+='['+line[0]+']'+line[1]+'['+line[2]+'],'
    string_yuml=string_yuml.rstrip(',')
    return string_yuml
def retirer_methods(string_yuml):#Retire les methods d'une string yuml
    pos = 0
    new_string=""
    for i in range(len(string_yuml)):
        if string_yuml[i] == '|':
            pos += 1
            if pos == 1:
                new_string += '|'
        else:
            if string_yuml[i] == ']':
                pos = 0
                new_string += ']'
            else:
                if pos < 2:
                    new_string += string_yuml[i]
    string_yuml=new_string
    return string_yuml

def ecriture_classe():#ecris les classes de la stringyuml
    #réupération du nombre de classes, dans le dossier ./folder/class/
    commands.getoutput("rm ./"+folder+".class.txt")
    commands.getoutput("ls ./"+folder+"class/ >> ./"+folder+".class.txt")
    classe = open("./"+folder+".class.txt",'r')
    classes=[]
    for fichier in classe:
        classes.append(fichier.rstrip('\n'))
    #on cree la string de presntation des classes
    string_yuml = "echo \""

    for i in range(len(classes)-1):
        string_yuml+=JSON_to_string(fichier_to_JSON(i,classes))+','
    string_yuml+=JSON_to_string(fichier_to_JSON(len(classes)-1,classes))

    #Generation java :
    jsons=[]
    for i in range(len(classes)):
        jsons.append(fichier_to_JSON(i,classes))
    if (params["-j"]=="True"):
        javagen.gen(folder,jsons,"True"==params["-g"])
    commands.getoutput("rm ./"+folder+".class.txt")
    return string_yuml


#-----------On ecris les classes (ac attributs et methodes--------
string_output = ecriture_classe()

#-------------------On enleve les methods si besoin---------------
if "False"==(params["-m"]):
    string_output = retirer_methods(string_output)

#---------------------On rajoute les liaisons---------------------
string_output = ajouter_laisons(string_output)

#-----On termine, on exporte pour le souvenir et en execute yuml ---
string_output += "\"| ./yuml -s "+params["-s"]+" -f "+params["-f"]+" -o "+folder+"uml."+params["-f"]+" -v"


commands.getoutput("rm ./"+folder+"string_yuml.txt")
f = open("./"+folder+"string_yuml.txt","w")
f.write(string_output)



print("seems good :-)")



commands.getoutput(string_output)

