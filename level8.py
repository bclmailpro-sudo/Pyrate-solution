avancer()
obstacle = detecter_obstacle()
while obstacle == True:
    coup()
    obstacle = detecter_obstacle()
for _ in range(3):
    avancer()
droite()
for _ in range(5):
    avancer()
obstacle = detecter_obstacle()
while obstacle == True:
    coup()
    avancer()
    obstacle = detecter_obstacle()
ouvrir()
