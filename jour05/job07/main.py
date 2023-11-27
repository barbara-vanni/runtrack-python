# Luke Skywalker, un professeur de Math, fait passer un test et décide de noter ses élèves
# sur une échelle allant de 0 à 100 inclus.
# Si un étudiant obtient moins de 40 sur 100, il échoue au test.
# S'il a plus de 40, il réussit le test. Luke est un professeur fort sympathique et décide
# donc d’arrondir à la hausse les notes des étudiants ayant réussi le test. Mais Luke n’est
# quand même pas trop gentil. Cet arrondi à la hausse ne bénéficiera qu’aux étudiants
# remplissant certains critères, car tout de même, il ne faut pas exagérer, sans blague.
# Le critère est simple : Si un étudiant a eu une note de moins de strictement 3 points de
# son prochain multiple de 5, alors sa note est arrondie à ce multiple de 5. Par exemple,
# un 83 sera arrondi à 85 alors qu’un 82 restera un 82.

# Pour simplifier le travail de Luke, écrivez une fonction qui prend en paramètre une liste
# de notes et qui renvoie une liste de notes, arrondies comme il se doit, quand cela est
# nécessaire.



notes = [78,45,92,32,67,89,14,53,76,41,60,85,23,94,50]

def round_five(notes: list) -> list:
    for i in range(len(notes)):
        rest = notes[i] % 5
        if rest > 0 and (5 - rest) < 3:
            notes[i] = notes[i] - rest + 5
    return notes

round_notes = round_five(notes)
print(round_notes)

win = ""
fail = ""
for i in range(len(round_notes)):
    if round_notes[i] > 40:
        win += str(round_notes[i]) + " "
    else:
        fail += str(round_notes[i]) + " "

print(len(win.split()), "élèves ont réussi :", win)
print(len(fail.split()), "élèves ont échoué :", fail)

