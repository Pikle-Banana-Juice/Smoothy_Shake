import csv

def stock_ligne(fichier_csv):
    #Renvoie une liste des lignes du fichier_csv
    with open(fichier_csv, newline="") as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def afficher_ligne(fichier_csv, n):
    #retourne la ligne n du fichier_csv
    liste = stock_ligne(fichier_csv)
    return liste[n]

def separer_string_liste(fichier_csv, n):
    #transforme la ligne n du Fichier_csv en liste, sep = ";"
    #Si n=o, crée un fichier "info.txt" avec le nom de toutes les colonnes.
    i = str(afficher_ligne(fichier_csv, n))
    liste = i.split(";")
    if n == 0:
        f = open("info.txt", "w")
        for elm in liste:
            f.write(f"{elm}\n")
        f.close()
    return liste

def afficher_colonne(fichier_csv, n, c):
    #retourne la colonne C de la ligne n du fichier_csv
    i = separer_string_liste(fichier_csv, n)
    return i[c-1]

def index_colonne(fichier_csv, nom_colonne):
    #Donne l'index de la colonne "nom_colonne" de "fichier_csv"
    #"anneedeplantation" ==> index 19
    #"genre_bota" ==> index 13
    i = separer_string_liste(fichier_csv, 0)
    for elm in i:
        if elm == nom_colonne:
            return i.index(elm)

def extraire_all_colonne(fichier_csv, nom_colonne):
    #Renvoie une liste des elements de la colonne "nom_colonne" du fichier_csv
    #Pour obtenir l'ensemble des années de plantation, utiliser les argumnets ("data/trees.csv", "anneedeplantation")
    liste = stock_ligne(fichier_csv)
    liste_annee = []
    index_c = int(index_colonne(fichier_csv, nom_colonne))
    for row in liste:
        i = str(row)
        i2 = i.split(";")
        liste_annee.append(i2[index_c])
    return liste_annee

def afficher_50_premières_dernières(fichier_csv, nom_colonne):
    #affiche les 50 premiers & 50 derniers elements de la colonne "nom_colonne"
    #Pour avoir les 50 premières & dernières dates, utiliser les arguments ("data/trees.csv", "anneedeplantation")
    liste = extraire_all_colonne(fichier_csv, nom_colonne)
    l1 = liste[0:50]
    long = int(len(liste))
    l2 = liste[long-50:long]
    l3 = l1 + l2
    return l3

    #Il y a 31826 arbres reférencés dans le fichier trees.csv

def date_manquante(fichier_csv, nom_colonne, annee):
    #Retourne le nombre d'élément dont la colonne "nom_colonne" vaut "annee"
    #1998 arbres n'ont pas d'info sur leur date de plantation ("data/trees.csv", "anneedeplantation", "")
    #132 arbres ont été plantés l'année de ma naissance ("data/trees.csv", "anneedeplantation", "1993")
    liste = extraire_all_colonne(fichier_csv, nom_colonne)
    count = 0
    for elm in liste:
        if elm == annee:
            count +=1
    return count

def date_manquante2(fichier_csv, nom_colonne, annee):
    #Même fonction que celle au dessus.
    liste = extraire_all_colonne(fichier_csv, nom_colonne)
    count = liste.count(annee)
    return count

def date_ancienne_recente(fichier_csv):
    #Retourne la date de plantation la plus ancienne et la plus récente des arbres référencés dans "fichier_csv"
    #la date la plus ancienne est "1900" / la date la plus récente est "2022"
    liste = extraire_all_colonne(fichier_csv, "anneedeplantation")
    ancienne = int(liste[1])
    recente = int(liste[1])
    for elm in liste[1:len(liste)+1]:
            if elm != "":
                if int(elm) < int(ancienne):
                    ancienne = elm
                if int(elm) > int(recente):
                    recente = elm
    return ancienne, recente

def plante_par_annee(fichier_csv):
    #comptabilise le nombre d'arbres plantés chaque année.
    liste = extraire_all_colonne(fichier_csv, "anneedeplantation")
    dico = {}
    for elm in liste[1:len(liste)+1]:
        if elm not in dico:
            dico[elm] = 1
        else:
            dico[elm] += 1
    return dico

def moyenne_par_annee(fichier_csv):
    #Donne la moyenne d'arbre plantés chaque année.
    #En moyenne 475 arbres sont plantés chaque année.
    dico = plante_par_annee(fichier_csv)
    liste = []
    for key in dico:
        value = dico[key]
        liste.append(value)
    moyenne = int(sum(liste)/len(liste))
    return moyenne

def liste_tuple(fichier_csv):
    #Renvoie une liste composée de tuples ("anneedeplantation", "Nbr_arbre_plantés")
    dico = plante_par_annee(fichier_csv)
    liste = []
    for key in dico:
        value = dico[key]
        liste.append((key, value))
    return liste

def genre_annee(fichier_csv):
    #Renvoie une liste composée de tuples ("anneedeplantation", "genre_bota")
    liste = stock_ligne(fichier_csv)
    liste_genre_annee = []
    for elm in liste:
        i = str(elm)
        liste_elm = i.split(";")
        liste_genre_annee.append((liste_elm[19], liste_elm[13]))
    return liste_genre_annee

def info_manquante(fichier_csv, nom_colonne):
    #Renvoie le nombre d'information manquante pour la colonne "nom_colonne"
    #825 arbres n'ont pas d'information pour leur "genre_bota"
    liste = extraire_all_colonne(fichier_csv, nom_colonne)
    count = liste.count("")
    return count

def tri_genre_annee(fichier_csv):
    #Renvoie la liste triée par ordre décroissant d'année de ("anneedeplantation", "genre_bota")
    liste = genre_annee(fichier_csv)
    liste_tri = sorted(liste, key = lambda x: x[0], reverse = True)
    return liste_tri


