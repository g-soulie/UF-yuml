# UF-yuml

Welcome in the User Friendly Yuml repository.

This is a short python programm which allows you to have a more "user-friandly" experience with yuml (http://yuml.me/).

The idea is to work with a quite Object Oriented way of thinking : 
You will create files, one class-file will correspond to one class, and the liaisons-file to the liaisons.

That seems to be more easy than struggle with a huge string :-)


<b> Installation </b>

First you need to install yuml 0.1 :
https://github.com/wandernauta/yuml/

then you only need to put the uf-yuml.py in the same folder.

<b> Utilisation </b>

Create a folder for your project.

<u> Creation of the class :</u> 
Create a folder 'class' in this folder, to store your class files.
create as many class as you want. One class correspond to one file in the class folder. 
The class format is :


      class name
      
      attribute1
      attribute2
      ...
      
      method1
      method2
      ...

<u> Creation of the liaisons :</u>
Create or modify any files whose name begin by 'liaisons' in your project folder, 'liaisons.txt' for example.
Each line correspond to a liaison, according to the following format :

      Classe1_name,-,Classe2_name

This will draw a simple line between Classe1, and Class2.
You can draw more elaborate liaisons, please visit http://yuml.me/diagram/scruffy/class/samples to see some samples.
As an example, 

      Classe1_name,->,Classe2_name
will draw a direction arrow with the line.

Then you have to draw. In a linux terminal :

    python uf-yuml.py folder/ methods output_format output_shape

methods indicate if you want to draw the methods. 'methods' will draw the methods, 'sdgfdsg' won't.
output_format can be png, pdf, jpg or svg 
output_shapes concern the appearance of your output. It can be scruffy, nofunky or plain.
For example, with the exemple folder of the repository, try :

    python uf-yuml.py exemple/ methods pdf plain

<b> Acknowledgement </b>

99.9% of the work is from the yuml repository on github : https://github.com/wandernauta/yuml/
