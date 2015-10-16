import commands

def genjava(folder,json):
	String = "\n public class "+json["name"]+" { \n"
	commands.getoutput("rm ./"+folder+"java/"+json["name"]+".java")
	commands.getoutput("mkdir ./"+folder+"/java/")
	f=open("./"+folder+"java/"+json["name"]+".java",'w')
	f.write(String)

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
		f.write(json['attributs'][i]+"\n")
	

	for i in range(len(json['methods'])):
		f.write('\n')
		nom=json['methods'][i]
		if nom[0]=='+':
			nom=json['methods'][i][1:]
			nom="public "+ nom
		if nom[0]=='-':
			nom=json['methods'][i][1:]
			nom="private "+ nom
		f.write(nom+"{\n\n\n}\n")

			
	f.write("\n\n}")