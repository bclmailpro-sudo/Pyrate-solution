avancer()
sauter_haut()
for _ in range(5):
    hauteur = mesurer_hauteur()
    if hauteur == 0:
        avancer()
    elif hauteur == 1:
        sauter()
    else:
        sauter_haut()
    avancer()
    avancer()
ouvrir()
