import random
import json

def fairedesgroupes(fichier, nbrpersonnemax):
    logfichier = ''
    logfichier += 'Les paramètres (nom de fichier + taille max des groupes) ont été entrés\n'
    logfichier += "le nom du fichier est {} et le taille maximale d'un groupe est de {} élèves \n".format(fichier, nbrpersonnemax)
    fichier = open(fichier, encoding="utf-8")
    fichier = fichier.readlines()
    logfichier += 'le fichier a été ouvert, et stockées sous forme de liste\n'
    tailleliste = len(fichier)
    logfichier += 'ce fichier contient les noms de {} élèves\n'.format(tailleliste)
    nbrgroupe = (tailleliste//nbrpersonnemax)+1
    nbrgroupecharge = tailleliste%nbrgroupe
    logfichier += 'on détermine le nombre de groupe total et le nombre de groupes pleins\n'
    result = [] # liste vide qui accueillera nos groupes finaux #############
    i=0
    while i < nbrgroupe:
        result.append([])
        i+=1
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
    logfichier += 'Répartition aléatoire des groupes effectuée'
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
    logfichier += 'Formalisation en JSON effectuée\n'
    with open('fichier.json', 'w', encoding="utf-8") as fichierenjson:
        json.dump(resultjson, fichierenjson, ensure_ascii=False)
    logfichier += 'Export en JSON => fichier.json effectué\n'
    with open('listetriée.txt', 'w', encoding="utf-8") as fichierentext:
        fichierentext.write(resulttext)
    logfichier += 'Export en TXT => listetriée.txt effectué\n'
    with open('fichier.txt', 'w', encoding="utf-8") as fichierlog:
        fichierlog.write(logfichier)

if __name__ == "__main__":
    import sys
    fairedesgroupes(sys.argv[1], int(sys.argv[2]))