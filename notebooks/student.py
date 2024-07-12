

def tri_valeur(liste_tuple):
    liste_tri = []
    while len(liste_tuple) > 0:
        i = None
        for elm in liste_tuple:
            if i == None:
                i == int(elm[0])
            else:
                if int(elm[0]) < i:
                    i == int(elm[0])
                else:
                    continue
        for elm in liste_tuple:
            if int(elm[0]) == i:
                liste_tuple.remove(elm)
                liste_tri.append(elm)
    return liste_tri
    
def tri_couleur(deck):
    keur = []
    pik = []
    caro = []
    trfl = []
    for elm in deck:
        if elm[1] == 1:
            keur.append(elm)
        elif elm[1] == 2:
            pik.append(elm)
        elif elm[1] == 3:
            caro.append(elm)
        elif elm[1] == 4:
            trfl.append(elm)
    return keur, pik, caro, trfl

def tri_deck(deck):
    keur = tri_valeur(tri_couleur(deck)[0])
    pik = tri_valeur(tri_couleur(deck)[1])
    caro = tri_valeur(tri_couleur(deck)[2])
    trfl = tri_valeur(tri_couleur(deck)[3])
    deck_tri = keur + pik + caro + trfl
    return deck_tri


deck_test = [(x, y) for y in range(1, 5) for x in range(1, 14)]
liste_keur = [(8, 1), (1, 1), (10, 1), (2, 1), (3, 1), (9, 1), (4, 1), (5, 1), (13, 1), (6, 1), (7, 1), (11, 1), (12, 1)]

print(tri_valeur(liste_keur))