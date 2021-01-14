import random
import json

logfichier = ''
############### INPUT USER : FICHIER, TAILLE MAX GROUPE #################

fichier = input('Nom du fichier qui contient la liste des prénoms :\n')
nbrpersonnemax = int(input('Entrez la taille maximum des groupes :\n'))

logfichier += 'Les paramètres (nom de fichier + taille max des groupes) ont été entrés\n'
logfichier += "le nom du fichier est {} et le taille maximale d'un groupe est de {} élèves \n".format(fichier, nbrpersonnemax)
#########################################################################

############## OUVERTURE, LECTURE, MESURE DU FICHIER ####################

fichier = open(fichier, encoding="utf-8")
fichier = fichier.readlines()

logfichier += 'le fichier a été ouvert, et stockées sous forme de liste\n'

tailleliste = len(fichier)

logfichier += 'ce fichier contient les noms de {} élèves\n'.format(tailleliste)

#########################################################################

########## CALCUL NBR GROUPE TOTAL & NBR GROUPE PLEINS ##########################

nbrgroupe = (tailleliste//nbrpersonnemax)+1
nbrgroupecharge = tailleliste%nbrgroupe

logfichier += 'on détermine le nombre de groupe total et le nombre de groupes pleins\n'

#########################################################################

result = [] # liste vide qui accueillera nos groupes finaux #############

############### BOUCLE WHILE POUR CREER LES GROUPES DANS RESULT #########

i=0
while i < nbrgroupe:
    result.append([])
    i+=1

#########################################################################

"""######################################################################
Pour chaque groupe, on vérifie d'abord si c'est un groupe plein ou pas, 
si oui : on ajoute aléatoirment le nombre max de personne par groupe dedans
sinon : on ajoute le même nombre - 1 de personne toujours aléatoirement
une fois l'ajout terminé, afin de ne pas ajouter quelqu'un dans 2 groupe en même il est rétirer de la liste du fichier
"""

i=0
while i < len(result):
    if i < nbrgroupecharge:
        j = 0
        while j < nbrpersonnemax:
            elevechoisi = random.choice(fichier)
            result[i].append(elevechoisi)
            fichier.remove(elevechoisi)
            j+=1
    else:
        j = 0
        while j < nbrpersonnemax-1:
            elevechoisi = random.choice(fichier)
            result[i].append(elevechoisi)
            fichier.remove(elevechoisi)
            j+=1
    i+=1
###################################################################
#print(result)

#tout le code précédent a été écrit en pair programming avec Y4N1S & GogoDev <3

logfichier += 'Répartition aléatoire des groupes effectuée'
# pour chaque groupe on print (groupe (index+1)) puis chacun des élèves qu'il contient
# Conversion et stockage en JSON a la volée
# Conversion et stockage en TXT a la volée

resultjson = {
}
resulttext = ""

for groupe in result:
    nomdegroupe = "groupe"+str(result.index(groupe)+1)
    resulttext += nomdegroupe+"\n"
    resultjson[nomdegroupe] = []
    for eleve in groupe:
        resultjson[nomdegroupe].append(eleve.strip())
        resulttext += eleve.strip()+"\n"

#print(json.dumps(resultjson, ensure_ascii=False))

logfichier += 'Formalisation en JSON effectuée\n'

############### EXPORT EN JSON ####################################

with open('fichier.json', 'w', encoding="utf-8") as fichierenjson:
    json.dump(resultjson, fichierenjson, ensure_ascii=False)
    #fichierenjson.write(resultjson)

logfichier += 'Export en JSON => fichier.json effectué\n'
###################################################################
############### EXPORT EN TXT #####################################

with open('listetriée.txt', 'w', encoding="utf-8") as fichierentext:
    fichierentext.write(resulttext)

logfichier += 'Export en TXT => listetriée.txt effectué\n'

with open('fichier.txt', 'w', encoding="utf-8") as fichierlog:
    fichierlog.write(logfichier)

##################### CECARER #####################################