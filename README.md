# group-setting
Dans ce dépot git vous trouverez 3 fichiers, le but du script est de pouvoir répartir une liste d'élèves aléatoirement dans des groupes:
groupealeatoire.py est un script qui prend 2 inputs (fichier a lire, nombre max de groupe) et qui renvoie 3 fichier, une liste triée au format txt, la même chose en JSON et un log qui permet de suivre ces opérations.

fonctiongroupagerandom.py est groupealeatoire.py sous forme de module, il peut être importé, mais aussi executé depuis le terminal de la façon suivante :
>python fonctiongroupagerandom.py promo.txt 5

(en supposant que fonctiongroupagerandom.py et promo.txt soit dans le même dossier)

et promo.txt est un fichier d'exemple qui contient déjà des noms d'élèves, n'hésitez pas à l'utiliser pour vos tests.

Enjoy it Guys & thanks to Y4N1S for his help !

