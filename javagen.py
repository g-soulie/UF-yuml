import commands

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

def genClassJava(folder,json):
	String = "public class "+json["name"]+json["asc"]+" {\n"
	commands.getoutput("rm ./"+folder+"java/"+json["name"]+".java")
	commands.getoutput("mkdir ./"+folder+"/java/")
	f=open("./"+folder+"java/"+json["name"]+".java",'w')
	f.write(String+"\t")

	for i in range(len(json['attributs'])):
		if json['attributs'][i][0]=='+':
			a=json['attributs'][i][1:]
			a=a.split(':')
			if len(a)>1:
				json['attributs'][i]="public"+ str(a[1]) +" "+str(a[0])
			else:
				json['attributs'][i]="public "+ str(a)
		if json['attributs'][i][0]=='-':
			a=json['attributs'][i][1:]
			a=a.split(':')
			if len(a)>1:
				json['attributs'][i]="private"+ str(a[1]) +" "+str(a[0])
			else:
				json['attributs'][i]="private"+ str(a)
		f.write(json['attributs'][i]+"\n\t")
	

	for i in range(len(json['methods'])):
		f.write('\n\t')
		nom=json['methods'][i]
		if nom[0]=='+':
			nom=json['methods'][i][1:]
			nom="public "+ nom
		if nom[0]=='-':
			nom=json['methods'][i][1:]
			nom="private "+ nom
		f.write(nom+"{\n\t}\n")

			
	f.write("}")

def set_implements(jsons,classe,interface):
	interface_methods=[]
	new_jsons = jsons
	for i in range(len(new_jsons)):
		if new_jsons[i]['name']==interface:
			for method in new_jsons[i]['methods']:
				interface_methods.append(method)
	for i in range(len(new_jsons)):
		if new_jsons[i]["name"]==classe:
			new_jsons[i]["asc"] =" implements "+interface
			for method in interface_methods:
				new_jsons[i]['methods'].append(method)
	return new_jsons

def set_extends(jsons,fille,mere):
	new_jsons = jsons
	for i in range(len(new_jsons)):
		if new_jsons[i]["name"]==fille:
			new_jsons[i]["asc"] =" extends "+mere
	return new_jsons



def setupLiaisons(folder,jsons):
    liaisons = get_liaisons(folder)
    new_jsons=jsons
    for i in range(len(liaisons)):
        f=open("./"+folder+liaisons[i],'r')
        for line in f:
        	line = line.split(',')
        	if '^-.-' in line[1]:
        		new_jsons=set_implements(new_jsons,line[2].rstrip('\n'),line[0])
    		elif '-.-^' in line[1]:
        		new_jsons=set_implements(new_jsons,line[0],line[2].rstrip('\n'))
        	elif '^-' in line[1]:
        		new_jsons=set_extends(new_jsons,line[2].rstrip('\n'),line[0])
        	elif '-^' in line[1]:
        		new_jsons=set_extends(new_jsons,line[2].rstrip('\n'),line[0])
    return new_jsons


def gen(folder,jsons):
	new_jsons = setupLiaisons(folder,jsons)
	for json in new_jsons:
		print json['name']
		genClassJava(folder,json)
