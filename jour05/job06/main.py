    # /jour= 2 * hauteur_marche
    # /semaine = distance_journaliere * 7

    # distance_totale = distance_hebdomadaire * (nombre_marches + 1) 

    # distance_totale_en_metres = distance_totale / 100  


def guardian_walk(nombre_marches, hauteur_marche):

    total_distance = ((2 * hauteur_marche) * 7) * (nombre_marches + 1)/ 100  

    return "Pour", nombre_marches, "marches de", hauteur_marche, "cm, le gardien parcourt", total_distance, "m par semaine."


distance_totale = guardian_walk(250, 15)


print(*distance_totale)