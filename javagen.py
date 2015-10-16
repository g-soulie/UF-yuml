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
	if json['name'][0:2]=='<<':
		typ = "interface"
		name = json['name'].lstrip('<<').rstrip('>>')
	else:
		typ="class"
		name = json['name']

	String = "public "+typ+" "+name+json["asc"]+" {\n"
	commands.getoutput("rm ./"+folder+"java/"+json["name"]+".java")
	commands.getoutput("mkdir ./"+folder+"/java/")
	f=open("./"+folder+"java/"+json["name"]+".java",'w')
	f.write(String+"\t")

	for i in range(len(json['attributs'])):
		if json['attributs'][i][0]=='+':
			a=json['attributs'][i][1:]
			a=a.split(':')
			if len(a)>1:
				json['attributs'][i]="public"+ str(a[1]) +""+str(a[0])
			else:
				json['attributs'][i]="public "+ str(a)
		if json['attributs'][i][0]=='-':
			a=json['attributs'][i][1:]
			a=a.split(':')
			if len(a)>1:
				json['attributs'][i]="private"+ str(a[1]) +""+str(a[0])
			else:
				json['attributs'][i]="private"+ str(a)
		f.write(json['attributs'][i]+"\n\t")
	
	f.write('')
	for i in range(len(json['methods'])):
		f.write('\n\t')
		c=""
		if json['methods'][i][0]=='+':
			a=json['methods'][i][1:]
			a=a.split(':')
			if len(a)>1:
				b = a[0].lstrip(' ').split('(')
				if b[0]==json['name']:
					json['methods'][i]="public"+ str(a[0])
				else:
					json['methods'][i]="public"+ str(a[1]) +""+str(a[0])
				getSet = a[0].lstrip('-').lstrip('+').lstrip(' ')
				json['methods'][i]+='{'
				if 'get_' in getSet:
					tt=a[0].split('(')[0].split('_')
					t=""
					for k in range(len(tt)-2):
						t=t+tt[k+1]+"_"
					t+=tt[len(tt)-1]
					c+="\n\t\treturn "+t+";"
				elif 'set_' in getSet:
					tt=a[0].split('(')[0].split('_')
					t=""
					for k in range(len(tt)-2):
						t+=tt[k+1]+"_"
					t+=tt[len(tt)-1]
					c="\n\t\tthis."+t
					c+="="+t+";"
				json['methods'][i]+=c

			else:
				json['methods'][i]="public "+ str(a)
		if json['methods'][i][0]=='-':
			a=json['methods'][i][1:]
			a=a.split(':')
			if len(a)>1:
				json['methods'][i]="private"+ str(a[1]) +""+str(a[0])
			else:
				json['methods'][i]="private"+ str(a)
		f.write(str(json['methods'][i])+"\n\t}\n")

			
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
			new_jsons[i]["asc"]=" implements "+interface.rstrip('>>').lstrip('<<')
			for method in interface_methods:
				new_jsons[i]['methods'].append(method)
	return new_jsons

def set_extends(jsons,fille,mere):
	new_jsons = jsons
	mere_attributs=[]
	for i in range(len(new_jsons)):
		if new_jsons[i]['name']==mere:
			for method in new_jsons[i]['attributs']:
				mere_attributs.append(method)
	for i in range(len(new_jsons)):
		if new_jsons[i]["name"]==fille:
			new_jsons[i]["asc"] =" extends "+mere
			for attributs in mere_attributs:
				new_jsons[i]['attributs'].append(attributs)
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

def set_get(jsons):
	new_jsons=[]
	for json in jsons:
		new_json=json
		for i in range(len(json['attributs'])):
			if json['attributs'][i][0]=='+':
				a=json['attributs'][i]
				a=a.split(':')
				if (len(a)>1):
					string = "+ get_"+a[0].lstrip('-').lstrip('+').lstrip(' ').rstrip(' ')+"(): "+a[1]
					new_json['methods'].append(string)
					string = "+ set_"+a[0].lstrip('-').lstrip('+').lstrip(' ').rstrip(' ')+"("+a[1].lstrip(' ')
					string+=" "+a[0].lstrip('-').lstrip('+').lstrip(' ').rstrip(' ')+"): "+a[1]
					new_json['methods'].append(string)
					new_jsons.append(new_json)
	return new_jsons
	

def gen(folder,jsons,getter):
	commands.getoutput("rm ./"+folder+"/java/*")
	new_jsons = setupLiaisons(folder,jsons)
	print new_jsons
	print getter
	if getter:
		new_jsons=set_get(new_jsons)
	print new_jsons
	for json in new_jsons:
		genClassJava(folder,json)