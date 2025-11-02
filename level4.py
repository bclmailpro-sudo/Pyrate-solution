nombre = 0
avancer()
message = lire_chaine()
while nombre < 5:
    nombre = nombre + 1
    if message == "gau":
        gauche()
    else: droite()
    avancer()
    avancer()
    if nombre != 5:
        message = lire_chaine()
avancer()
ouvrir()
