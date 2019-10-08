notes = [] # Saisir les notes
while 1:
    entrerNote = input("Entre la prochaine note (Ou 'fin' si il n'y a plus de note à entrer) : ")

    if entrerNote.lower() == "fin":
        break

    notes.append(float(entrerNote))
    print(f"La liste des notes actuelle est : {notes} \n")

coefs = [] # Saisir les Coefs
for i in range(0, len(notes)):
    entrerCoef = input("\n Entre le coef de la prochaine note : ")

    coefs.append(float(entrerCoef))
    print(f"La liste des coefficients actuelle est : {coefs} ")


noteTotale, coefTotal = 0, 0
for i in range(0, len(notes)):

    noteTotale += notes[i]*coefs[i]
    coefTotal += coefs[i]

moyenne = noteTotale/coefTotal
print(f"Ta moyenne actuelle est de : {round(moyenne, 2)} \n")

nouvelleMoyenne = float(input("Entre ta nouvelle moyenne (2 chiffres après la virgule) : "))


coefNoteInconnue = float(input("Entre le coefficient de la note inconnue : "))

moyenneThéorique, valeurTest = 0, 20.0
while moyenneThéorique != nouvelleMoyenne:
    moyenneThéorique = (noteTotale+(valeurTest*coefNoteInconnue)) / (coefTotal+coefNoteInconnue)
    valeurTest -= 0.25

    if round(moyenneThéorique, 2) == nouvelleMoyenne:
        print(f"\n D'après mes calculs absolument pas très précis, ta note devrait être un truc genre {valeurTest} \n " \
            "Généralement faut ajouter 0.25 à ce que ça dit, mais ça marche peut être pas dans TOUS les cas. Donc t'as surement 0.25 de plus que ça, mais rien n'est sûr.")

    if valeurTest == 0:
        print("C'est bizarre, y'a pas de note possible entre 0 et 20, ou alors ce programme est trop mal codé pour la trouver.")
        break
