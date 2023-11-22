def time_to_text(minutes):

    heure = int(minutes/60)
    minutes %= 60
    print (heure, "heures et", minutes,"minutes")

minutes = int(input(" Entrez un nombre entier de minutes :"))

horloge = time_to_text(minutes)


